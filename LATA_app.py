import streamlit as st
import google.generativeai as genai
import datetime
import os

# --- Configuration for API Key ---
# This part is crucial for Streamlit Cloud.
# We fetch the API key from Streamlit's secrets management.
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    st.error("Google API Key not found. Please add it to your Streamlit Cloud secrets.")
    st.stop() # Stop the app if API key is missing

genai.configure(api_key=API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-pro')

# --- Lesson Plan Generation Function ---
def generate_lesson_plan():
    """Generates a detailed weekly PE lesson plan for children 4-7 years old."""

    prompt = """
    You are an experienced and creative Physical Education teacher assistant for young children.
    Generate a detailed and engaging weekly PE lesson plan for children aged 4 to 7 years.
    The lesson plan should include four distinct activities, clearly labeled:
    1.  **Gymnastics Activity:** A simple, safe gymnastics-inspired activity suitable for this age group.
    2.  **Tag Game:** A fun and easy-to-understand tag game.
    3.  **Ball Game:** A basic ball game focusing on fundamental skills (e.g., rolling, throwing, catching).
    4.  **Creative Game Choice:** A unique, imaginative, and active game of your own creation (not gymnastics, tag, or ball-focused).

    For each activity, provide:
    * **Activity Name:** A catchy title.
    * **Equipment Needed:** List any required equipment.
    * **Instructions:** Clear, step-by-step instructions.
    * **Learning Outcomes:** What physical skills or concepts will the children develop?
    * **Safety Notes:** Any important safety considerations.

    Format the output clearly with headings for each activity and bullet points for details.
    Start with a friendly greeting and a brief intro to the lesson plan.
    """
    try:
        with st.spinner("Generating your weekly lesson plan..."):
            response = model.generate_content(prompt)
            return response.text
    except Exception as e:
        st.error(f"Failed to generate lesson plan: {e}. Please check your API key and try again.")
        return None

# --- Streamlit App Layout ---
st.set_page_config(
    page_title="Teacher Assistant AI: PE Lesson Plan Generator",
    page_icon="🤸",
    layout="centered"
)

st.title("🤸 Teacher Assistant AI")
st.markdown("### Weekly PE Lesson Plan Generator for 4-7 Year Olds")

st.info(
    "This AI assistant generates a fresh PE lesson plan every Sunday for children aged 4-7. "
    "Each plan includes a Gymnastics Activity, a Tag Game, a Ball Game, and a Creative Game Choice."
)

# Get current day
today = datetime.date.today()
is_sunday = (today.weekday() == 6)  # Monday is 0, Sunday is 6

# Session state for lesson plan
if "lesson_plan_content" not in st.session_state:
    st.session_state.lesson_plan_content = None

# Check if it's Sunday and if a plan hasn't been generated for this session yet
if is_sunday:
    st.success("🎉 Happy Sunday! It's time for your new weekly PE lesson plan!")
    if st.button("Generate This Week's Lesson Plan", key="generate_sunday"):
        st.session_state.lesson_plan_content = generate_lesson_plan()
else:
    st.markdown(f"It's currently **{today.strftime('%A, %B %d, %Y')}**. New lesson plans are automatically suggested on Sundays.")
    if st.button("Generate Lesson Plan Anyway (for testing)", key="generate_any_day"):
        st.session_state.lesson_plan_content = generate_lesson_plan()


# Display the lesson plan if available
if st.session_state.lesson_plan_content:
    st.markdown("---")
    st.subheader("Your Weekly PE Lesson Plan:")
    st.markdown(st.session_state.lesson_plan_content)

st.markdown("---")
st.caption("Powered by Google Gemini Pro")
