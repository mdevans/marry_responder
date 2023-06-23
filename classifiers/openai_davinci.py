# Purpose: OpenAI text-davinci-003 text completion classifier
import os
from time import sleep
import openai

# Set up your OpenAI API credentials
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


def classify_phrase_intent(text: str) -> str:
    # Generate prompt for the GPT-3.5 model
    prompt = f"Classify if the intent of the following phrase is to inform me that my details have been shared, asking for permission to share or neither: '{text}'.\nOutput only one of the following options according to your choice: ask, shared, unclear.\nDo not explain your choice."

    # Call the OpenAI API to generate the intent
    # TODO: handle timeouts & errors
    for i in range(3):
        # Call the OpenAI API to generate the intent
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
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
    intent = response.choices[0].text.strip().lower().replace(".", "")  # type: ignore

    if intent not in ["ask", "shared", "unclear"]:
        print("text-davinci-003 returned an invalid intent: ", intent)
        intent = "unclear"

    sleep(1)  # rate limiting

    return intent
