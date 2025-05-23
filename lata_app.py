
import streamlit as st
import openai
import datetime

# Set up OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

# Function to generate lesson plan
def generate_lesson_plan():
    prompt = (
        "Create a weekly physical education lesson plan for children aged 4 to 7. "
        "Each day should include four activities: gymnastics, tag, ball game, and a free choice game."
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Streamlit app
st.title("LATA (Little Athletes Teacher Assistant)")
st.header("Weekly Physical Education Lesson Plan Generator")

if st.button("Generate Lesson Plan"):
    lesson_plan = generate_lesson_plan()
    st.text_area("Lesson Plan", lesson_plan, height=300)

    # Download button
    st.download_button(
        label="Download Lesson Plan",
        data=lesson_plan,
        file_name=f"lesson_plan_{datetime.date.today()}.txt",
        mime="text/plain"
    )
