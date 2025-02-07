import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openai import OpenAI



def prepare_prompt(user_prompt,history_info):
    
    pass
    
    return 


def chat_with_gpt(user_input):
    '''
    description: 
        this function call openai api to make users able to interact with chatgpt within this website

    parameters:
        None
    
    output:
        print the response from chat-gpt

    '''
    client = OpenAI(
    api_key="API-KEY",
    )
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    try:
        conversation.append({"role": "user", "content": user_input})
        chat_completion = client.chat.completions.create(
            messages=conversation,
            model="gpt-4o-mini",
                    )
        assistant_reply = chat_completion.choices[0].message.content
        conversation.append({"role": "assistant", "content": assistant_reply})
        return assistant_reply

    except TimeoutError:
        print("error")


