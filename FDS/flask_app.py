from flask import Flask, render_template, request, jsonify
from pdf_handler import extract_text_from_pdf
from openai_interaction import generate_glossary, generate_summary, generate_quiz_function, ai_chat, chatcompletion
import os
from feedback_guidance import exercises

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads directory exists
if not os.path.exists(UPLOAD_FOLDER):
    print("making new uploads folder")
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')


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
    messages = [{"role": "system", "content": "You are a concise feedback assistant speaking to a student. Students begin with placeholder functions and must write a functional version. If the text appears to be a placeholder, tell the student that they haven't yet attempted a solution. They are working in Google Colab and some variables will already have been defined. The guidance should tell you what variable have already been defined, if any. Your job is to give them support without telling them the answer. You can describe edits, but do not write code for them."}]
    feedback = chatcompletion(prompt, messages)
    # Return the response
    return jsonify({'response': feedback})

@app.route('/test', methods=['POST'])
def test_response():
    # Get parameters from the request
    id = request.form.get('id')
    text = request.form.get('text')
    guidance = "Students should write functional code"

    if id == "LiveLab1: Clean Resume":
        guidance = "The students have been asked to remove all traces of place names or demographic markers. So the text should not make reference to Alaska, the Philippines, or any other specific places. It should include detailed informations about the mechanical engineer's professional accomplishments."
    elif id == "LiveLab1: Generate Array":
        guidance = """
            Students received the following instructions:
            So far, we have been able to extract the following:

            •    32 names (representing various races and genders)
            •    A resume for 1 occupation
            •    3 prompts
            •    1 Job description
            This gives us 96 possible combinations.

            The format looks like:
            names = [{"name": "Keisha Towns", "gender": "F", "race": "Black"}, ...]  # 32 such dictionaries
            prompts = prompts = {
                "Rating": "Rate this resume.",
                "Interview": "Rate the resume for interviewing.",
                "Hiring": "Rate the resume for hiring."
            }
            cleaned_mechanical_engineer_resume = "Your resume content here"

            The researchers repeated each combination 50 times. To simplify, let’s repeat ours 3 times, resulting in an array of length 288.

            To accomplish this, you need to define a generate_array function that produces an array containing these 288 objects (combinations). Each object/row in the array should look like this:

            {
              'Name': 'Keisha Towns',
              'Gender': 'F',
              'Race': 'Black',
              'Occupation': 'Mechanical Engineer',
              'Prompt Type': 'Rating',
              'Score': ''
            }
        """
    elif id == "LiveLab1: Claude Chat":
        guidance = """The student should make a call to the Claude API. It should resemble this, but doesn't need to be identical. The student will not see the function below, so don't refer to it as the solution:
            claude_response = client.messages.create(
                model = model,
                temperature = temperature,
                system = #Some string describing the task of evaluating a resume with a score,
                messages = [{'role': 'user', 'content': prompt}],
                max_tokens = # this is optional
              )
              result = claude_response.content[0].text
              return result
            """

    prompt = guidance + "\n\nDiscuss how well this text acheives the goals above:\n\n" + text
    messages = [{"role": "system", "content": "You are a concise feedback assistant speaking to a student. Students begin with placeholder functions and must write a functional version. If the text appears to be a placeholder, tell the student that they haven't yet attempted a solution. They are working in Google Colab and some variables will already have been defined. The guidance should tell you what variable have already been defined, if any. Your job is to give them support without telling them the answer. You can describe edits, but do not write code for them."}]
    feedback = chatcompletion(prompt, messages)
    # Return the response
    return jsonify({'response': feedback})

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        # Verify the file was saved correctly and is not empty
        size = os.path.exists(file_path) and os.path.getsize(file_path)
        if size > 0:
            result = extract_text_from_pdf(file_path)
            return jsonify(result)
        else:
            return jsonify({'error': 'File is empty or not saved correctly'}), 400
    return 'No file uploaded', 400

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    selected_text = data.get('selected_text')
    function = data.get('function')
    if function == 'glossary':
        result = generate_glossary(selected_text)
    elif function == 'summary':
        result = generate_summary(selected_text)
    elif function == 'quiz':
        result = generate_quiz_function(selected_text)
    #elif function == 'conversation':
    #    result = ai_conversation(selected_text)
    return jsonify({'result': result})

@app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    data = request.json
    selected_text = data.get('selected_text')
    result = generate_quiz_function(selected_text)
    return jsonify({'result': result})

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    #selected_text = data.get('selected_text')
    question = data.get('question')
    conversation = data.get('conversation', [])

    #system_prompt = f"The following is a text from a research paper: {selected_text}\nAnswer questions based on this text."
    #conversation.append({"role": "system", "content": system_prompt})
    #conversation.append({"role": "user", "content": question})
    answer = ai_chat(question, conversation);

    #conversation.append({"role": "assistant", "content": answer})
    return answer;

    #return jsonify({"answer": answer, "conversation": conversation})


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




