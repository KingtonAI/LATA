
from openai import OpenAI

def generate_lesson_plan():
    # Initialize the OpenAI client with your API key
    client = OpenAI(api_key="YOUR_API_KEY_HERE")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Generate a lesson plan for teaching Python programming."}
        ]
    )

    lesson_plan = response.choices[0].message.content
    return lesson_plan

if __name__ == "__main__":
    lesson_plan = generate_lesson_plan()
    print(lesson_plan)
