
import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

def generate_lesson_plan():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Create a weekly lesson plan for physical education for children aged 4 to 7. Include four activities in each lesson plan: gymnastics, tag, ball game, and a game of your choice."}
        ]
    )
    return response['choices'][0]['message']['content']

st.title("LATA - Little Athletes Teacher Assistant")

if st.button("Generate Lesson Plan"):
    lesson_plan = generate_lesson_plan()
    st.text_area("Weekly Lesson Plan", lesson_plan, height=300)
    st.download_button("Download Lesson Plan", lesson_plan, file_name="lesson_plan.txt")
