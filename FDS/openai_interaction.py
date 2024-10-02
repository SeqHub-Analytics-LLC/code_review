import openai
import sensitiveData
import json

openai.api_key = sensitiveData.apiKey

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

def generate_glossary(text, age=15):
    prompt = f'Generate a glossary of the technical terms used in the following text. Imagine you are writing for a {age}-year-old:\n\n{text}'
    return chatcompletion(prompt);

def generate_summary(text, age=15):
    prompt = f'Paraphrase the following text for a {age}-year-old. Include a high level of technical detail.\n\n{text}'
    return chatcompletion(prompt);

def generate_quiz(text, age=15):
    prompt = f'Generate quiz questions for a {age}-year-old. Include a high level of technical detail.\n\n{text}'
    return chatcompletion(prompt);

def ai_chat(input, messages):
    return chatcompletion(input, messages)

def generate_quiz_function(text, age=15, type="single-word-answer", model="gpt-4o"):
    system_prompt = f"You are a tool to write {type} quizzes of 5 questions based on the provided text. The student is {age}-years-old"
    function_object = [
        {
            "name": "write_quiz",
            "description": system_prompt,
            "parameters": {
                "type": "object",
                "properties": {
                    "question_1": {
                        "type": "string",
                        "description": f"1st {type} question"
                    },
                    "answer_1": {
                        "type": "string",
                        "description": "answer to the 1st question"
                    },
                    "question_2": {
                        "type": "string",
                        "description": f"2nd {type} question"
                    },
                    "answer_2": {
                        "type": "string",
                        "description": "answer to the 2nd question"
                    },
                    "question_3": {
                        "type": "string",
                        "description": f"3rd {type} question"
                    },
                    "answer_3": {
                        "type": "string",
                        "description": "answer to the 3rd question"
                    },
                    "question_4": {
                        "type": "string",
                        "description": f"4th {type} question"
                    },
                    "answer_4": {
                        "type": "string",
                        "description": "answer to the 4th question"
                    },
                    "question_5": {
                        "type": "string",
                        "description": f"5th {type} question"
                    },
                    "answer_5": {
                        "type": "string",
                        "description": "answer to the 5th question"
                    },
                  }
                },
              "required": ["answer_1", "question_1", "answer_2", "question_2", "answer_3", "question_3", "answer_4", "question_4", "answer_5", "question_5"]
        }
    ]
    function_call = {"name": "write_quiz"}
    str_result =get_function_response(text, function_object, function_call, model)
    return str_result or ""
