import asyncio
import json
from pathlib import Path
from typing import List, Dict, Any

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from langchain.prompts import ChatPromptTemplate

load_dotenv()

SUMMARY_PROMPT = """
    You are a bot assistant for an open source software project. 
    We are working on giving the documentation for this project a complete overhaul.
    This will be an ongoing, iterative process.
    
    We are assessing each document as it currently exists to be reworked so that it fits into the Diataxis Documentation framework.
    The Diataxis Documentation framework can be summarized as follows:
        * The framework provides a systematic approach to create, organize and maintain technical documentation.
        * The goal is pragmatic improvement.
        * The framework divides documentation into 4 types based on 2 axes:
            1 - Theory vs Practice
            2 - Acquisition vs Application
        * The 4 types of Documentation:
            1 - Tutorials - Learning-oriented guides that provide lessons to teach users basic skills. Help users get started.
            2 - How-To Guides - Task-oriented guides that provide steps to accomplish specific goals. Help users solve problems.
            3 - Reference - Information-oriented technical descriptions of the product. Help users find factual information.
            4 - Explanation - Understanding-oriented discussion to provide context and illuminate concepts. Help users gain deeper knowledge.
        * Each type serves a distinct user need at different points in their journey using the product.
        * Keeping the types clearly separated improves quality by ensuring docs fit user needs.
        * Start small, assess and improve one part at a time to steadily enhance overall documentation.
        
    Your job as a bot assistant is to:
        * At the top of each document, add text identifying it so that it fits into the Diataxis framework
        * Summarize each document so that it considers the Diataxis Documentation framework.
 
 DOCUMENT DRAFT TEXT: 
 
 {text}

"""


def create_component_summary_chain():
    prompt = ChatPromptTemplate.from_template(SUMMARY_PROMPT)
    model = ChatOpenAI(temperature=0,
                       model_name="gpt-3.5-turbo-16k")
    chain = prompt | model
    return chain


GLOBAL_SUMMARY_PROMPT = """
    You are a bot assistant for an open source software project. 
    We are working on giving the documentation for this project a complete overhaul.
    This will be an ongoing, iterative process.
    
    We are assessing each document as it currently exists to be reworked so that it fits into the Diataxis Documentation framework.
    The Diataxis Documentation framework can be summarized as follows:
        * The framework provides a systematic approach to create, organize and maintain technical documentation.
        * The goal is pragmatic improvement.
        * The framework divides documentation into 4 types based on 2 axes:
            1 - Theory vs Practice
            2 - Acquisition vs Application
        * The 4 types of Documentation:
            1 - Tutorials - Learning-oriented guides that provide lessons to teach users basic skills. Help users get started.
            2 - How-To Guides - Task-oriented guides that provide steps to accomplish specific goals. Help users solve problems.
            3 - Reference - Information-oriented technical descriptions of the product. Help users find factual information.
            4 - Explanation - Understanding-oriented discussion to provide context and illuminate concepts. Help users gain deeper knowledge.
        * Each type serves a distinct user need at different points in their journey using the product.
        * Keeping the types clearly separated improves quality by ensuring docs fit user needs.
        * Start small, assess and improve one part at a time to steadily enhance overall documentation.
        
    Approach this as a second pass. Previously, we summarized each document individually in the repository. 
    For this pass, your job as a bot assistant is to:
        * I need you to combine the summaries of each file into a global report of the current state of the documentation. This should include:
            1. Identification of gaps that would complete an approach using the Diataxis Documentation framework.
            2. A prioritized list of what exists and where the gaps should most be addressed. 
             
 CURRENT PROPOSAL TEXT: 
 
{text}
"""


def create_global_summary_chain():
    prompt = ChatPromptTemplate.from_template(GLOBAL_SUMMARY_PROMPT)

    model = ChatAnthropic(temperature=0)
    chain = prompt | model
    return chain


async def document_from_discord_chats(chats: List[Dict[str, Any]]):
    output_text = ""

    component_summary_chain = create_component_summary_chain()
    global_summary_chain = create_global_summary_chain()
    inputs = []
    for chat in chats:
        try:
            inputs.append({"text": chat["as_text"]})
        except KeyError:
            print(f"WARNING: Could not find `as_text` key in chat: {chat}")

    all_summaries = await component_summary_chain.abatch(inputs=inputs)
    for summary in all_summaries:
        file_summary = (f"+++++++++++++++++++++++++++++++++++\n\n"
                        f"INDIVIDUAL CHAT SUMMARY\n\n"
                        f"{summary.content}\n\n"
                        f"-----------------------------------\n\n")
        print(file_summary)
        output_text += file_summary

    print(output_text)

    global_summary = global_summary_chain.invoke({"text": "\n".join(input_texts)}).content

    output_text += (f"=============================================================\n\n"
                    f"=============================================================\n\n"
                    f"\n\n GLOBAL SUMMARY OF SUMMARIES \n \n"
                    f"=============================================================\n\n"
                    f"{global_summary}\n\n")

    document_file_name = f"document_summary.md"
    with open("document_file_name", "w", encoding="utf-8") as file:
        file.write(output_text)


if __name__ == "__main__":
    # target_channel_id = 1168937728637947914 #2023-10-31_in_class-eye-tracking
    target_channel_id = 1158766012116783164  # Jumping project channel
    json_path = Path(
        r"C:\Users\jonma\syncthing_folders\jon_main_syncthing\jonbot_data\classbot_database\classbot_database.chats_2023-11-06.json")
    all_chats = json.loads(json_path.read_text(encoding="utf-8"))
    chats_to_use = []
    for chat in all_chats:
        if "channel_id" in chat.keys():
            if int(chat["channel_id"]["$numberLong"]) == target_channel_id:
                chats_to_use.append(chat)

    asyncio.run(document_from_discord_chats(chats=chats_to_use))
