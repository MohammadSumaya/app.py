import streamlit as st
from dotenv import load_dotenv
import os 
from google import genai
#load environment variables
load_dotenv()
#get API KEY
api_key=os.getenv("GEMINI_API_KEY")

#create gemini client 
client=genai.Client()
st.set_page_config(page_title="Gemini AI Chatbot",page_icon="🤖",layout="centered")
st.title("🤖 Gemini AI Chatbot")
st.write("Ask Gemini anything!")

#user prompt
prompt=st.text_area(
    "enter your prompt:",
    placeholder="explain artificial intelligence in simple words..."
)

#generate button
if st.button("generate response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response=client.models.generate_content(model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.success("response generated!")
        st.write(response.text)
    else:
        st.warning("please enter a prompt.")