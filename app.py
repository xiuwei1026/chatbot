import openai
import streamlit as st
from streamlit_chat import message


openai.api_key = st.secrets.api_key.key


# This function uses the OpenAI Completion API to generate a 
# response based on the given prompt. The temperature parameter controls 

def generate_response(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message



st.title("👧 openAI GPT-3 chatBot")

st.sidebar.header("Instructions")
st.sidebar.info(
    '''You are able to talk to AI Bot ChatGPT.
       Enter a **question** in the **text box** and **press enter** to receive 
       a **response** from the ChatGPT
       '''
    )





if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 


if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user',avatar_style="adventurer-neutral",seed="Tigger") 
        message(st.session_state["generated"][i], key=str(i),avatar_style="bottts",seed="Bob")


placeholder = st.empty()
user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


with placeholder.container():
    message(st.session_state.past[-1], is_user=True,avatar_style="adventurer-neutral",seed="Tigger") # display the latest message
    message(st.session_state.generated[-1], is_user=False,avatar_style="bottts",seed="Bob") # display the latest message
        
