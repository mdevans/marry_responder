# Purpose: OpenAI GPT-3.5-turbo ChatCompletion classifier
import os
from time import sleep
import openai

# Set up your OpenAI API credentials
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


def classify_phrase_intent(text: str) -> str:
    # Generate a conversation with the GPT-3.5-turbo model
    conversation = [
        {
            "role": "system",
            "content": "You are an email classifier that classifies the intent of a phrase.",
        },
        {
            "role": "user",
            "content": f"Decide if the following is to tell me that my details have been shared, asking for permission to share my details or neither: '{text}'.\nOutput only one of the following options exactly as written in the set and do not explain your choice: [ask, shared, unclear]",
        },
    ]

    # Call the OpenAI API to generate the intent
    # Retry loop to handle timeouts & errors
    for i in range(3):
        # Call the OpenAI API to generate the intent
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                max_tokens=256,
                n=1,
                stop=None,
                temperature=0.0,
                top_p=1.0,
                timeout=20,
            )
        except:
            print("Error: OpenAI API call failed. Retrying ({i})...")
            sleep(i * 5)
            continue
        else:
            break

    # Extract the generated intent from the API response
    intent = response["choices"][0]["message"]["content"].strip().lower().replace(".", "")  # type: ignore

    if intent not in ["ask", "shared", "unclear"]:
        print("GPT-3.5-turbo returned an invalid intent: ", intent)
        intent = "unclear"

    sleep(1)  # rate limiting

    return intent
