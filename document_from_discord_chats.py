import asyncio
import json
import time
from pathlib import Path
from typing import List, Dict, Any

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from langchain.prompts import ChatPromptTemplate

load_dotenv()

TOPIC_EXTRACTOR_PROMPT = """
    Extract tags for relevant topics that are discussed in this conversation.
    Create a list of topics separated by commas and wrapped in [[double brackets]] like so: 
    [[Topic Name]], [[Another topic name]], [[Yet another topic name]]

TEXT: 

 {text}

"""


def create_topic_extraction_chain():
    prompt = ChatPromptTemplate.from_template(TOPIC_EXTRACTOR_PROMPT)
    model = ChatOpenAI(temperature=0,
                       model_name="gpt-3.5-turbo-16k")
    chain = prompt | model
    return chain

SUMMARY_PROMPT = """
    Quickly summarize this conversation in a few sentences. 
    
    The summaries should focus on retaining information to be used in an academic paper with the following abstract:
    [Eye tracking technology has emerged as a valuable tool for studying motor control, balance, and coordination during
     complex movements. This review comprehensively surveys the literature on applications of eye tracking in motor control 
     research. Studies demonstrate that analyzing gaze patterns provides insights into the relationship between visual attention
      allocation and motor planning and execution. Literature review plays a crucial role in identifying knowledge gaps 
      and building upon existing findings, such as work elucidating the role of head movements in maintaining steady gaze. 
      Research in visual neuroscience reveals the relevance of eye tracking across domains including sports training and 
      video game design. Examining different types of eye movements via oculomotor control studies informs models of information 
      processing and cognitive functions. Applications in sports and in conjunction with EEG shed light on perceptual and 
      attentional processes under physical exertion. Coordinated eye movements involve multiple cranial nerves, making isolating 
      individual nerve function challenging. However, eye tracking interventions show promise for improving control and cognition 
      in developmental disorders. Technological advances enable video-based eye trackers to precisely track gaze in naturalistic 
      environments. Synthesis of the literature indicates a robust capacity for eye tracking techniques to advance comprehension 
      of the complex perceptual and neural processes underlying human balance, motor control, and goal-directed movement.]
      
      Be terse, precise, accurate, and academic.
 
 CONVERSATION TEXT: 
 
 {text}

"""


def create_component_summary_chain():
    prompt = ChatPromptTemplate.from_template(SUMMARY_PROMPT)
    model = ChatOpenAI(temperature=0,
                       model_name="gpt-3.5-turbo-16k")
    chain = prompt | model
    return chain


GLOBAL_SUMMARY_PROMPT = """
    Write a lengthy, precise, academic review article based on the LIST OF SUMMARIES TEXT.
    Be truthful, accurate, and precise. Do not make anything up. 
    Use the following outline:[
    I. Introduction
    A. Eye tracking technology provides insights into motor control and coordination during jumping movements
    B. Allows researchers to study relationship between gaze direction and balance
    II. Benefits of Eye Tracking in Motor Control Studies
    A. Tracks gaze direction which is crucial for motor planning and execution
    B. Analyzing gaze patterns provides understanding of visual attention allocation
    III. Importance of Literature Review
    A. Builds on previous findings and identifies knowledge gaps
    B. Example study on head movements supporting eye tracking in baseball batting
    IV. Visual Neuroscience
    A. Explores how brain processes visual information
    B. Relevant to sports training, video game design, etc.
    V. Oculomotor Control
    A. Neural system controlling eye movements
    B. Different types of eye movements studied
    C. Animal models like Hubel & Wiesel's cat research
    VI. Applications of Eye Tracking
    A. Sports - where people look during actions and exertion
    B. Cognitive processes - combined with EEG data
    VII. Role of Cranial Nerves
    A. Eye trackers track coordinated cranial nerve movements
    B. Insights into relationship between eye movements and cognition
    C. ADHD studies showing improved cognitive function after training
    VIII. Technical Aspects
    A. Video-based eye trackers like Pupil Labs
    B. Measuring corneal reflections and pupil reflexes
    C. Applications in UX, psychology, neuroscience, accessibility
    IX. Conclusion
    A. Comprehensive overview of eye tracking in motor control
    B. Highlights relationship between gaze and balance
    C. Emphasizes literature review and animal models
    D. Valuable insights for understanding human perception and movement]
    
LIST OF SUMMARIES TEXT: 
+++++ 
{text}
+++++

That was the SUMMARIES TEXT. As a reminder, we are writing an academic review article based on the SUMMARIES TEXT.
"""


def create_global_summary_chain():
    prompt = ChatPromptTemplate.from_template(GLOBAL_SUMMARY_PROMPT)

    model = ChatOpenAI(temperature=0,
                       model_name="gpt-3.5-turbo-16k")
    chain = prompt | model
    return chain


async def document_from_discord_chats(chats: List[Dict[str, Any]]):
    output_text = ""

    inputs = []
    all_texts = []
    for chat in chats.values():
        try:
            all_texts.append(chat["as_text"])
            inputs.append({"text": chat["as_text"]})
        except KeyError:
            print(f"WARNING: Could not find `as_text` key in chat: {chat}")

    component_topic_extraction_chain = create_topic_extraction_chain()
    component_summary_chain = create_component_summary_chain()
    global_summary_chain = create_global_summary_chain()

    print(f"Starting TOPIC EXTRACTION CHAIN: with {len(inputs)} chats...")

    all_topics = await component_topic_extraction_chain.abatch(inputs=inputs)
    for topic in all_topics:
        file_topics = (f"+++++++++++++++++++++++++++++++++++\n\n"
                        f"INDIVIDUAL CHAT TOPICS\n\n"
                        f"{topic.content}\n\n"
                        f"-----------------------------------\n\n")
        print(file_topics)
        output_text += file_topics

    all_summaries = await component_summary_chain.abatch(inputs=inputs)
    for summary in all_summaries:
        file_summary = (f"+++++++++++++++++++++++++++++++++++\n\n"
                        f"INDIVIDUAL CHAT SUMMARY\n\n"
                        f"{summary.content}\n\n"
                        f"-----------------------------------\n\n")
        print(file_summary)
        output_text += file_summary

    print(output_text)

    all_summaries_and_topics = []
    for summary, topic in zip(all_summaries, all_topics):
        all_summaries_and_topics.append(summary.content)
        all_summaries_and_topics.append(topic.content)
    all_summaries_and_topics = "\n".join(all_summaries_and_topics)
    clipped_text = all_summaries_and_topics[:15000]
    global_summary = global_summary_chain.invoke({"text": clipped_text}).content

    output_text += (f"=============================================================\n\n"
                    f"=============================================================\n\n"
                    f"\n\n GLOBAL SUMMARY OF SUMMARIES \n\n"
                    f"=============================================================\n\n"
                    f"{global_summary}\n\n")
    print(global_summary)

    document_file_name = f"document_summary.md"
    file_number=0
    while Path(document_file_name).is_file():
        document_file_name=f"document_summary{file_number}.md"
        file_number+=1
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
