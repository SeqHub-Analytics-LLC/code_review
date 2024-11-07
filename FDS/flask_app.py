from flask import Flask, render_template, request, jsonify
from openai_interaction import ai_chat, chatcompletion
import os
from lab_prompts import *
from homework_prompts import *
from mapping import prompt_map

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Pierrepont Student!"


@app.route('/feedback', methods=['POST'])
def feedback_response():
    # Get parameters from the request
    assessment_name = request.form.get('assessment_name')
    id = request.form.get('id')
    text = request.form.get('text')

    guidance = "Students should write functional code"
    exercise = prompt_map[assessment_name]
    if exercise["id"] == id:
        guidance = exercise["guidance"]

    prompt = guidance + "\n\nGiven the guidelines above, review the student's attempt below:\n\n" + text
    messages = [{"role": "system", 
                 "content": "Evaluate the student’s attempt by considering the question, expected task, and review criteria. If the code appears to contain a placeholder (ellipsis), let the student know they haven’t yet started a functional solution. Keep in mind that you’re providing constructive support directly to the student—offer suggestions on edits and hints but avoid writing code or giving away the answer. Some variables may already be defined in Google Colab, as noted in the guidelines, so check those to ensure the student’s code is using them as expected."}]
    feedback = chatcompletion(prompt, messages)
    # Return the response
    return jsonify({'response': feedback})


@app.route('/get_feedback', methods=['POST'])
def get_feedback():
    data = request.json
    question = data.get('question')
    context = data.get('context')
    user_answer = data.get('user_answer')
    correct_answer = data.get('correct_answer')
    print(user_answer)
    messages=[
        {"role": "system", "content": f"Provide feedback on the possible answers based on the correct answer given the following context: {context}."},
    ]
    text = f"Question: {question}\nAn answer: {user_answer}\Another answer: {correct_answer}"
    result = chatcompletion(text, messages)
    print(result)
    return result

if __name__ == '__main__':
    app.run(debug=True)




