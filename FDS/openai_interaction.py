import openai
import json
import os

##Import Open AI API key
openai_key = os.getenv("api_key")

openai.api_key = openai_key

# Function to complete chat input using OpenAI's GPT-3.5 Turbo
def chatcompletion(user_input, messages = [], temperature = 0.7, model="gpt-4o"):
    messages.append({"role": "user", "content": user_input})
    openai_response = openai.chat.completions.create(
        model = model,
        temperature = temperature,
        messages = messages
    )
    #print(openai_response)
    response_content = openai_response.choices[0].message.content
    #print("Raw response content:", response_content)

    try:
        result = json.loads(response_content)
    except json.JSONDecodeError:
        result = response_content  # If response is not JSON, return it as plain text

    print(result)
    return result

def get_function_response(prompt, function_object, function_call="required", model = "gpt-3.5-turbo"):
  response = openai.chat.completions.create(
    model = model,
    messages = [{"role": "user", "content": prompt}],
    functions = function_object,
    function_call = function_call
  )
  print(response)
  result = response.choices[0].message.function_call.arguments
  print(result)
  return result

def ai_chat(input, messages):
    return chatcompletion(input, messages)

