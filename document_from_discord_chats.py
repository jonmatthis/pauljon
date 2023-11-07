import asyncio
import json
from pathlib import Path
from typing import List, Dict, Any

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from langchain.prompts import ChatPromptTemplate

load_dotenv()

SUMMARY_PROMPT = """
    You are a bot assistant for a university neuroscience course. 
    We are creating an academic paper based on a collection of conversations students had with AI chatbots. 
    Write a summary of each student chat, considering the academic paper that will be written based on their chats. 
    Be truthful, accurate, and precise. Do not make anything up. 
 
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
    You are a bot assistant for a university neuroscience course. 
    We are creating an academic paper based on a collection of summaries based on conversations students had with AI chatbots. 
    Write a professional, exceedingly rigorous academic paper from the collection of student chats. 
    Use lateral thinking to conceive of a unique, clever subject matter for the paper based on their chats. 
    Write the academic paper. Be truthful. Do not make anything up. 
    The paper should have the following basic structure:
        Title of Paper
        Abstract
        Title of Subsection
        Text of Subsection
        Repeat Subsection as many times as necessary.
        Conclusion
        Citations
             
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
    all_texts = []
    for chat in chats.values():
        try:
            all_texts.append(chat["as_text"])
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

    global_summary = global_summary_chain.invoke({"text": "\n".join(all_texts)}).content

    output_text += (f"=============================================================\n\n"
                    f"=============================================================\n\n"
                    f"\n\n GLOBAL SUMMARY OF SUMMARIES \n \n"
                    f"=============================================================\n\n"
                    f"{global_summary}\n\n")

    document_file_name = f"document_summary.md"
    with open(document_file_name, "w", encoding="utf-8") as file:
        file.write(output_text)


if __name__ == "__main__":
    target_channel_id = 1168937728637947914 #2023-10-31_in_class-eye-tracking
    # target_channel_id = 1158766012116783164  # Jumping project channel
    json_path = Path(
        # r"/Users/paul/Code/pauljon/classbot_database.chats_2023-11-06.json")
        "/Users/paul/Code/pauljon/eyetracking_channel_chats.json")
    all_chats = json.loads(json_path.read_text(encoding="utf-8"))
    #chats_to_use = []
    #for chat in all_chats:
     #   if "channel_id" in chat.keys():
      #      if int(chat["channel_id"]["$numberLong"]) == target_channel_id:
       #         chats_to_use.append(chat)

    asyncio.run(document_from_discord_chats(chats=all_chats))
