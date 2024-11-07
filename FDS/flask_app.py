from flask import Flask, render_template, request, jsonify
from openai_interaction import ai_chat, chatcompletion
import os
from feedback_guidance import exercises

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Pierrepont Student!"


@app.route('/feedback', methods=['POST'])
def feedback_response():
    # Get parameters from the request
    id = request.form.get('id')
    text = request.form.get('text')

    guidance = "Students should write functional code"
    for exercise in exercises:
        if exercise["id"] == id:
            guidance = exercise["guidance"]

    prompt = guidance + "\n\nDiscuss how well this text acheives the goals above:\n\n" + text
    messages = [{"role": "system", 
                 "content": "You are a concise feedback assistant speaking to a student. Students begin with placeholder functions and must write a functional version. If the text appears to be a placeholder, tell the student that they haven't yet attempted a solution. They are working in Google Colab and some variables will already have been defined. The guidance should tell you what variable have already been defined, if any. Your job is to give them support without telling them the answer. You can describe edits, but do not write code for them nor reveal answers to them."}]
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




