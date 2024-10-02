exercises = [{
        "id": "LiveLab1: Clean Resume",
        "guidance": "The students have been asked to remove all traces of place names or demographic markers. So the text should not make reference to Alaska, the Philippines, or any other specific places. It should include detailed informations about the mechanical engineer's professional accomplishments."
    },
    {
        "id": "LiveLab1: Generate Array",
        "guidance": """
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
    },
    {
        "id": "LiveLab1: Claude Chat",
        "guidance": """The student should make a call to the Claude API. It should resemble this, but doesn't need to be identical. The student will not see the function below, so don't refer to it as the solution:
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
    },
    {
        "id":"gemini_ticketing_1",
        "guidance": """The function should import userdata from google.colab. Then get and return the stored value of GOOGLE_API_KEY. No error handling is necessary.
One correct function would be:
def get_google_api_key():
  from google.colab import userdata
  return userdata.get('GOOGLE_API_KEY')
        """
    }, {
        "id":"gemini_ticketing_2",
        "guidance":"""
        The function must accomplish 3 things.
        It should call genai.GenerativeModel('SOME_MODEL_NAME'). The model name might be, 'gemini-pro'.
        It should call .generate_content("SOME PROMPT") on the result. The prompt should include the idea of classifying a customer ticket.
        It should extract and return the response with .text;
        """
    }, {
        "id": "gemini_ticketing_3",
        "guidance": """Their work should be identical or similar to this. Variables may have different names:
def classify_ticket(ticket_text: str) -> TicketClassification:
  client = instructor.from_gemini(
      client=genai.GenerativeModel(
          model_name="models/gemini-1.5-flash-latest",
      ),
      mode=instructor.Mode.GEMINI_JSON,
  )

  # note that client.chat.completions.create will also work
  resp = client.messages.create(
      messages=[
          {
              "role": "user",
              "content": ticket_text,
          }
      ],
      response_model=TicketClassification,
  )
  return resp
  """
    }, {
        "id": "gemini_ticketing_4",
        "guidance": """Their work should be similar to this with two additions: A system message giving more context, and a different gemini model:
def classify_ticket(ticket_text: str) -> TicketClassification:
  client = instructor.from_gemini(
      client=genai.GenerativeModel(
          model_name="models/gemini-1.5-flash-latest",
      ),
      mode=instructor.Mode.GEMINI_JSON,
  )

  # note that client.chat.completions.create will also work
  resp = client.messages.create(
      messages=[
          {
              "role": "user",
              "content": ticket_text,
          }
      ],
      response_model=TicketClassification,
  )
  return resp
  """
    }, {
        "id": "gemini_ticketing_5",
        "guidance": """Their work should be vaguely similar to this with some additions: It will help interpret sandwich orders. It may have a system message giving more context, and a different gemini model:
def classify_ticket(ticket_text: str) -> TicketClassification:
  client = instructor.from_gemini(
      client=genai.GenerativeModel(
          model_name="models/gemini-1.5-flash-latest",
      ),
      mode=instructor.Mode.GEMINI_JSON,
  )

  # note that client.chat.completions.create will also work
  resp = client.messages.create(
      messages=[
          {
              "role": "user",
              "content": ticket_text,
          }
      ],
      response_model=TicketClassification,
  )
  return resp
  """
    },{
        "id": "cc3_openai_response",
        "guidance":"""Their work should be similar to this:
def get_openai_response(prompt, model):
    messages = [{"role": "user", "content": prompt}]
    response = openai_client.chat.completions.create(
        model=model,
        messages = messages,
        temperature=0.7,
    )
    return response.choices[0].message.content
    """
    },{
        "id": "cc3_claude_response",
        "guidance":"""Their work should be similar to this:
def get_claude_response(prompt, model):
    response = anthropic_client.messages.create(
    model=model,
    max_tokens=1024,
    messages=[
        {"role": "user", "content": prompt}
        ]
    )
    return response.content[0].text
    """
    },{
        "id": "cc3_gemini_response",
        "guidance":"""Their work should be similar to this:
def get_gemini_response(prompt, model):
    llm = genai.GenerativeModel(model)
    response = llm.generate_content(prompt)
    return response.text
    """
    },{
        "id": "prompt_lab_Challenge_1",
        "guidance":"""The student is expected to develop a prompt that effectively utilizes both datasets embedded as strings, akin to the example provided. While their prompt can be dynamically created, it should encapsulate the clarity of the example prompt. It’s important to note that the student will not have access to the example function, so no reference should be made to the solution below:
def get_prompt_1():
  prompt = "You have access to two datasets: one containing sales data and the other containing customer feedback. The sales data includes product names, units sold, and dates, while the feedback data includes review text, ratings, and dates. Perform the following tasks:/

  1. Analyze the sales data to identify trends and top-selling products.
  2. Perform sentiment analysis on customer feedback to categorize each review as positive, neutral, or negative.
  3. Generate a comprehensive report that includes:
    - A summary of sales trends and top-selling products.
    - Insights from the sentiment analysis of customer feedback.
    - Strategic recommendations for the next quarter based on the analysis.

  Here are the datasets:
  Sales Data: " + str(sales_data) + "/
  Customer Feedback Data: " + str(feedback_data)
  return prompt
    """
    },{
        "id": "prompt_lab_Challenge_2",
        "guidance":"""The student is expected to develop a prompt that effectively utilizes example text and labels, akin to the example provided. While their prompt can be dynamically created, it should encapsulate the clarity of the example prompt. It’s important to note that the student will not have access to the example function, so no reference should be made to the solution below:
def get_prompt_2():
  prompt = ""/
      Classify the following texts into one of three categories: Scientific, News, or Social Media. Use the provided examples to understand the characteristics of each category.

      Examples:

      1. Text: "The effect of quantum entanglement on particle behavior..."
        Label: Scientific

      2. Text: "A comprehensive review of machine learning algorithms..."
        Label: Scientific

      3. Text: "The latest economic forecasts indicate a recession..."
        Label: News

      4. Text: "A new law passed by the government aims to..."
        Label: News

      5. Text: "Just had the best coffee ever at this new cafe!"
        Label: Social Media

      6. Text: "Can't believe how amazing the concert was last night!"
        Label: Social Media

      New Texts to Classify:

      1. Text: "Scientists have discovered a new species of bacteria..."
        Label:

      2. Text: "Breaking: Major earthquake hits the city..."
        Label:

      3. Text: "Had so much fun hiking with friends today!"
        Label:
  ""
  return prompt
    """
    },{
        "id": "prompt_lab_Challenge_3",
        "guidance":"""The student is expected to develop a prompt that effectively provides a step-by-step approach towards solving the ethical dilemma, akin to the example provided. While their prompt can be dynamically created, it should encapsulate the clarity of the example prompt. It’s important to note that the student will not have access to the example function, so no reference should be made to the solution below:
def get_prompt_3():
  prompt = ""/
  Solve the following ethical dilemma step-by-step:

  Should a self-driving car prioritize the safety of its passengers or pedestrians in an unavoidable accident?

  Step-by-step solution:
  1. Identify the key stakeholders involved: passengers and pedestrians.
  2. Consider the ethical principles of utilitarianism (maximizing overall good) and deontology (duty-based ethics).
  3. Analyze the utilitarian perspective: Evaluate the potential outcomes and the number of lives that could be saved in each scenario.
  4. Analyze the deontological perspective: Consider the duty of the car to protect its passengers versus its duty to avoid harming pedestrians.
  5. Examine legal and societal implications: Understand the legal responsibilities of the car manufacturer and societal expectations.
  6. Reflect on precedents and existing guidelines: Review how similar dilemmas have been addressed in other contexts.
  7. Balance the competing interests: Weigh the importance of passenger safety against pedestrian safety.
  8. Formulate a reasoned conclusion based on the analysis: Provide a justification for the chosen course of action.

  Answer:
  ""
  return prompt
  """
    },{
        "id": "prompt_lab_Challenge_4",
        "guidance":"""The student is expected to develop a prompt that effectively provides a step-by-step approach towards synthesizing the debate between Immanuel Knat and John Stuart Mill, akin to the example provided. While their prompt can be dynamically created, it should encapsulate the clarity of the example prompt. It’s important to note that the student will not have access to the example function, so no reference should be made to the solution below:
def get_prompt_4():
  prompt = ""/
    You are an AI tasked with analyzing a debate on ethics between Immanuel Kant and John Stuart Mill. Follow this chain of thought to present their arguments, reason through their positions, and synthesize the key points.

      1. Kant's Argument:
        a. State Kant's core ethical principle
        b. Explain the concept of the categorical imperative
        c. Describe how Kant believes ethical decisions should be made
        d. Provide an example of Kant's ethics in action

      2. Mill's Argument:
        a. State Mill's core ethical principle
        b. Explain the concept of utilitarianism
        c. Describe how Mill believes ethical decisions should be made
        d. Provide an example of Mill's ethics in action

      3. Kant's Reasoning:
        a. Why is following rules important?
        b. What are the consequences of universal rule-following?
        c. How does this approach ensure moral behavior?
        d. What potential issues arise from always following rules?

      4. Mill's Reasoning:
        a. Why is maximizing happiness important?
        b. What are the consequences of always aiming for the greatest good?
        c. How does this approach lead to ethical outcomes?
        d. What potential issues arise from focusing solely on consequences?

      5. Counterarguments:
        a. Kant's critique of Mill's approach:
            - Potential issues with utilitarianism
            - Why rule-based ethics is superior
        b. Mill's critique of Kant's approach:
            - Potential issues with rigid rule-following
            - Why consequence-based ethics is superior

      6. Synthesis:
        a. Summarize the key points of both arguments
        b. Identify the main areas of disagreement
        c. Highlight any potential common ground
        d. Discuss the implications of each approach for ethical decision-making

      7. Conclusion:
        a. Recap the core principles of each philosopher
        b. Reflect on the strengths and weaknesses of each approach
        c. Consider how these ideas might be applied in modern ethical dilemmas
        d. Offer a final thought on the importance of this ethical debate

      Please proceed through each step, providing detailed responses for each point.

  return prompt
  """
    },{
        "id": "cc1_gemini_exercise1",
        "guidance":"""The student is expected to write a function similar to this. They have been provided with an incomplete version and we expect this or something very close to this in return. It’s important to note you should give feedback only based on what exists in the solution, feedbacks on error handling and comments are not required.Also note that the student will not have access to the example function, so no reference should be made to the solution below:
def gemini_exercise_1():
    model = genai.GenerativeModel('model_name') #Initialize the generative model 'gemini-1.0-pro-001'
    response = model.generate_content("What is the future of AI in one sentence?") #generates content from the model
    return response.candidates # provides functionalities to view the top response candidates from Gemini.
    """
    },
    {
        "id": "cc1_gemini_exercise2",
        "guidance":"""The student is expected to write a function similar to this. They have been provided with an incomplete version and we expect this in return. It’s important to note that you should give feedback only based on what exists in the solution, feedbacks on error handling and comments are not required. Also note that the student will not have access to the example function, so no reference should be made to the solution below:
def gemini_exercise_2():
  new_image = Image.open('image_link') #insert the link to your image
  vision_model = genai.GenerativeModel('gemini-1.5-flash') ## Initialize Vison Model
  vision_response = vision_model.generate_content(["Tell me what you see in this picture.", new_image], stream=False) #Generate Text
  return vision_response.text
    """
    },
    {
        "id": "cc1_gpt_exercise1",
        "guidance":"""The student is expected to write a function similar to this. They have been provided with an incomplete version and we expect this in return. It’s important to note that the student can put in any chat model name from openai except instruction models, as the API endpoint was written for chat models.Note that you should give feedback only based on what exists in the solution, feedbacks on error handling and comments are not required. Also note that the student will not have access to the example function, so no reference should be made to the solution below:
def gpt_exercise_1():
  prompt="Tell me about the Great Wall of China."
  messages = [{"role": "user", "content": prompt}]
  completion = client.chat.completions.create( #complete the method that initializes the chat completions API endpoint
    model="model_name", # Which model would be appropriate for this scenario?
    messages = messages,
    max_tokens=300,
    temperature=0,)
  return completion
    """
    },
    {
        "id": "cc1_gpt_exercise2",
        "guidance":"""The student is expected to write a function similar to this. They have been provided with an incomplete version and we expect this in return. It’s important to note that the student should initialize the API endpoint without using chat as the model given to them is an instruction model. Note that you should give feedback only based on what exists in the solution, feedbacks on error handling and comments are not required. Also note that they will not have access to the example function, so no reference should be made to the solution below:
def gpt_exercise_2():
  output = client.completions.create( #initializes the completions API endpoint
    model="model_name",
    prompt="Explain what the AGI in artificial intelligence means?",
    max_tokens=300,
    temperature=0.7
)

  return output.choices[0].text #properly extract the text from the output
    """
    },
    {
        "id": "cc1_gpt_exercise3",
        "guidance":"""The student is expected to write a function similar to this. They have been provided with an incomplete version and we expect this in return. It’s important to note that this is a translation task, so the student can put in any language of their choice. Note that you should give feedback only based on what exists in the solution, feedbacks on error handling and comments are not required. Also note that the student will not have access to the example function, so no reference should be made to the solution below:
def gpt_exercise_3():
  translations = client.___.transcriptions.create( #the method initializes the audio transcription API endpoint
    model="whisper-1",
    response_format="text",
    language="___", #ISO language code of your choice
    file=audio_file,
)
  return translations
    """
    },
    {
        "id": "cc1_claude_exercise1",
        "guidance":"""The student is expected to write a function similar to this. They have been provided with an incomplete version and we expect this in return. The response below is in the correct format needed. Note that you should give feedback only based on what exists in the solution, feedbacks on error handling and comments are not required. Also note that the student will not have access to the example function, so no reference should be made to the prompt or solution below:
def claude_exercise_1(text):
    prompt = f"Extract entities and the type of entities from\n\n{text}\n\n" # Create the prompt that accomplishes the task by extracting entities
    response = client.____.create( #the method initializes the messages API endpoint
        model="model_name", # Try out any model of your choice; claude-3-haiku-20240307, claude-3-sonnet-20240229 or claude-3-opus-20240229
        max_tokens=150,
        messages=[
        {"role": "user", "content": prompt}
       ]
    )
    return response.content[0].text #properly extract the text from the output

    """
    },
    {
        "id": "cc1_claude_exercise2",
        "guidance":"""The student is expected to write a function similar to this. They have been provided with an incomplete version and we expect this in return. It’s important to note that the student should use any of the model provided, no need for flexibility. Note that you should give feedback only based on what exists in the solution, feedbacks on error handling and comments are not required. Also note that they will not have access to the example function, so no reference should be made to this prompt or solution below:
def claude_exercise_2():
  message = client.messages.create(
    model="model_name", # Try out any model of your choice; claude-3-sonnet-20240229 or claude-3-opus-20240229
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data_1,
                    },
                },
                {
                    "type": "text",
                    "text": "Write a poem using this image."
                }
            ],
        }
    ],
)
  return message

    """
    }


    ]
