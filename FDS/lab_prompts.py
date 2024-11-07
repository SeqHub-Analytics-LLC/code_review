
lab01_prompts = [
      {
        "id": "lab1_Q1",
        "guidance":  """
                   **Question:** How many seconds are there between midnight January 1, 2010 and midnight January 1, 2020. Note that there are two leap years in this span of a decade. A non-leap year has 365 days and a leap year has 366 days.
                         
                   **Student's Task:** 
                   Assign the name `seconds_in_a_decade` to the number of seconds between midnight January 1, 2010 and midnight January 1, 2020.
                   
                   **Review Criteria:**
                   - The students are expected to fill `seconds_in_a_decade` in the `lab1_exercise_1` function. The value of seconds_in_a_decade when computed must yield the correct value. It could also be directly set to the actual value. 
                   - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                   - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again and give subtle hints without revealing the answer.
                   
                  **Expected Completed Function:** The completed function of the students should look like this with the value of `seconds_in_a_decade` set the actual value of seconds or a computation which yields the correct number of seconds.
                        ```
                        def lab1_exercise_1():
                            seconds_in_a_decade = (365 * 8 + 366 * 2) * 24 * 60 * 60
                            return seconds_in_a_decade
                        ```
                    """
      },
      {
        "id": "lab1_Q2",
        "guidance":    """
                   **Experiment Details:** To verify the accuracy of this law, we will calculate the difference between the predicted distance the hammer drops and the actual distance.  (If they are different, it might be because Newton's laws are wrong, or because our measurements are imprecise, or because there are other factors affecting the hammer for which we haven't accounted.)
                   Someone studied the video and estimated that the hammer was dropped 113 cm from the surface. Counting frames in the video, the hammer falls for 1.2 seconds (36 frames).
                         
                   **Question:** From the experiment details, what is the duration of the fall in the experiment, in seconds and estimated distance the hammer actually fell, in meters?
                   
                   **Student's Task:** You'll have to replace each variable in the math formula with the name we gave that number in function.                   
                   
                   **Review Criteria:**
                   - The students are expected to fill `estimated_distance_m` and `time` in the `lab1_exercise_2` function. Both values must be correct and converted to the appropriate units as specified by the question
                   - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                   - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again and give subtle hints without revealing the answer.
                   
                  **Expected Completed Function:** The completed function of the students should look like this with the value of `estimated_distance_m` and `time` set.
                        ```
                        def lab1_exercise_2():.
                          # t, the duration of the fall in the experiment, in seconds.
                          time = 1.2
                        
                          # The estimated distance the hammer actually fell, in meters.
                          estimated_distance_m = 1.13
                          return time,estimated_distance_m
                        ```
                    """
      },
      {
        "id": "lab1_Q3",
        "guidance":    """
                   **Experiment Details:** To verify the accuracy of this law, we will calculate the difference between the predicted distance the hammer drops and the actual distance.  (If they are different, it might be because Newton's laws are wrong, or because our measurements are imprecise, or because there are other factors affecting the hammer for which we haven't accounted.)
                   Someone studied the video and estimated that the hammer was dropped 113 cm from the surface. Counting frames in the video, the hammer falls for 1.2 seconds (36 frames).
                         
                   **Student's Task:** Complete the code in the function to compute the difference between the predicted and estimated distances (in meters) that the hammer fell in this experiment. This just means translating the formula above ($\frac{1}{2}G\frac{M}{R^2}t^2$) into Python code as the predicted distance.
                   
                   **Student's Task:** This just means translating the formula above ($\frac{1}{2}G\frac{M}{R^2}t^2$) into Python code.  You'll have to replace each variable in the math formula with the name we gave that number in Python code.             
                  
                   **Review Criteria:**
                   - The students are expected to fill `estimated_distance_m` and `time` in the `lab1_exercise_2` function. Both values must be correct and converted to the appropriate units as specified by the question
                   - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                   - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again and give subtle hints without revealing the answer.
                   
                  **Expected Completed Function:** The completed function of the students should look like this with the value of `estimated_distance_m` and `time` set.
                        ```
                        def lab1_exercise_3():.

                                # G, the universal constant measuring the strength of gravity.
                                gravity_constant = 6.674 * 10**-11
                              
                                # M, the moon's mass, in kilograms.
                                moon_mass_kg = 7.34767309 * 10**22
                              
                                # R, the radius of the moon, in meters.
                                moon_radius_m = 1.737 * 10**6
                              
                                # The distance the hammer should have fallen
                                # over the duration of the fall, in meters,
                                # according to Newton's law of gravity.
                                # The text above describes the formula
                                # for this distance given by Newton's law.
                                # **YOU FILL THIS PART IN.**
                                predicted_distance_m = 0.5 * gravity_constant * (moon_mass_kg / moon_radius_m**2) * time**2
                              
                                # Here we've computed the difference
                                # between the predicted fall distance and the distance we actually measured.
                                # If you've filled in the above code, this should just work.
                                difference = predicted_distance_m - estimated_distance_m
                              
                                return difference
                        ```
                    """
      },
      {
        "id": "homework1_Q4",
        "guidance": """
                         **Question:** When you run the following code block wrapped in triple backticks, Python will produce a cryptic error message.
                               ```
                               two = 3
                               six = two plus two
                               ```
                         **Student's Task:** 
                         Choose the best explanation of what's wrong with the code and assign 1, 2, 3, or 4 to `names_q2` below to indicate your answer.
      
                         1. The `plus` operation only applies to numbers, not the word "two".
                        
                         2. The name "two" cannot be assigned to the number 3.
                        
                         3. Two + two is four, not six.
                        
                         4. Python cannot interpret the name `two` followed directly by a name that has not been defined.
      
                         **Review Criteria:**
      
                         - The students are expected to place their choosen option as `names_q2` in the `hw1_exercise_4` function. The value of names_q2 must be set to the correct answer option given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                         - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again by providing subtle hints without revealing the answer.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with the correct answer choice set to `names_q2`.
                              ```
                              def hw1_exercise_4():
                                names_q2 = 4
                                return names_q2
                              ```
                  """
      },
      {
        "id": "homework1_Q5",
        "guidance": """
                         **Question:** When you run the following code block wrapped in triple backticks, Python will produce a cryptic error message.
                               ```
                               x = print(5)
                               y = x + 2
                               ```
                         **Student's Task:** 
                         Choose the best explanation of what's wrong with the code and assign 1, 2, or 3 to `names_q3` below to indicate your answer.
      
                         1. Python doesn't want `y` to be assigned.
                        
                         2. The `print` operation is meant for displaying values to the programmer, not for assigning values!
                        
                         3. Python can’t do addition between one name and one number. It has to be 2 numbers or 2 predefined names.
                         
                         **Review Criteria:**
      
                         - The students are expected to place their choosen option as `names_q3` in the `hw1_exercise_5` function. The value of names_q3 must be set to the correct answer option given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                         - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again by providing subtle hints without revealing the answer.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with the correct answer choice set to `names_q2`.
                              ```
                              def hw1_exercise_5():
                                names_q3 = 2
                                return names_q3
                              ```
                  """
      },
      {
        "id": "homework1_Q6",
        "guidance": """
                         **Question:** Which statement best describes the *treatment* and *control* groups for this study? 
                         
                         **Summary of study:** A study at UCLA investigated factors that might result in greater attention to the health and education of girls in rural India. One such factor is information about job opportunities for women. The idea is that if people know that educated women can get good jobs, they might take more care of the health and education of girls in their families, as an investment in the girls’ future potential as earners. Without the knowledge of job opportunities, the author hypothesizes that families do not invest in women’s well-being.
                         The study focused on 160 villages outside the capital of India, all with little access to information about call centers and similar organizations that offer job opportunities to women. In 80 of the villages chosen at random, recruiters visited the village, described the opportunities, recruited women who had some English language proficiency and experience with computers, and provided ongoing support free of charge for three years. In the other 80 villages, no recruiters visited and no other intervention was made.
                         At the end of the study period, the researchers recorded data about the school attendance and health of the children in the villages.
                         
                         **Student's Task:** 
                         Assign either 1, 2, or 3 to the name `jobs_q1` below to indicate your answer.
      
                         1. The treatment group was the 80 villages visited by recruiters, and the control group was the other 80 villages with no intervention.
      
                         2. The treatment group was the 160 villages selected, and the control group was the rest of the villages outside the capital of India.
                        
                         3. There is no clear notion of *treatment* and *control* group in this study.
      
                         **Review Criteria:**
      
                         - The students are expected to place their choosen option as `jobs_q1` in the `hw1_exercise_6` function. The value of jobs_q1 must be set to the correct answer option given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                         - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again by providing subtle hints without revealing the answer.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with the correct answer choice set to `jobs_q1`.
                              ```
                              def hw1_exercise_6():
                                jobs_q1 = 1
                                return jobs_q1
                              ```
                  """
      },
      {
        "id": "homework1_Q7",
        "guidance": """
                         **Question:** Was this an observational study or a randomized controlled experiment? 
                         
                         **Summary of study:** A study at UCLA investigated factors that might result in greater attention to the health and education of girls in rural India. One such factor is information about job opportunities for women. The idea is that if people know that educated women can get good jobs, they might take more care of the health and education of girls in their families, as an investment in the girls’ future potential as earners. Without the knowledge of job opportunities, the author hypothesizes that families do not invest in women’s well-being.
                         The study focused on 160 villages outside the capital of India, all with little access to information about call centers and similar organizations that offer job opportunities to women. In 80 of the villages chosen at random, recruiters visited the village, described the opportunities, recruited women who had some English language proficiency and experience with computers, and provided ongoing support free of charge for three years. In the other 80 villages, no recruiters visited and no other intervention was made.
                         At the end of the study period, the researchers recorded data about the school attendance and health of the children in the villages.
                         
                         **Student's Task:** 
                         Assign either 1, 2, or 3 to the name `jobs_q2` below to indicate your answer.
      
                         1. This was an observational study.
                        
                         2. This was a randomized controlled experiment.  
                        
                         3. This was a randomized observational study.
      
                         **Review Criteria:**
      
                         - The students are expected to place their choosen option as `jobs_q2` in the `hw1_exercise_7` function. The value of jobs_q2 must be set to the correct answer option given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                         - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again by providing subtle hints without revealing the answer.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with the correct answer choice set to `jobs_q2`.
                              ```
                              def hw1_exercise_7():
                                jobs_q2 = 2
                                return jobs_q2
                              ```
                  """
      },
      {
        "id": "homework1_Q7b",
        "guidance": """
                         **Question:** The study reported, "Girls aged 5-15 in villages that received the recruiting services were 3 to 5 percentage points more likely to be in school and experienced an increase in Body Mass Index, reflecting greater nutrition and/or medical care. However, there was no net gain in height. For boys, there was no change in any of these measures." Why do you think the author points out the lack of change in the boys? *Hint:* Remember the original hypothesis. The author believes that educating women in job opportunities will cause families to invest more in the women’s well-being.
                         
                         **Summary of study:** A study at UCLA investigated factors that might result in greater attention to the health and education of girls in rural India. One such factor is information about job opportunities for women. The idea is that if people know that educated women can get good jobs, they might take more care of the health and education of girls in their families, as an investment in the girls’ future potential as earners. Without the knowledge of job opportunities, the author hypothesizes that families do not invest in women’s well-being.
                         The study focused on 160 villages outside the capital of India, all with little access to information about call centers and similar organizations that offer job opportunities to women. In 80 of the villages chosen at random, recruiters visited the village, described the opportunities, recruited women who had some English language proficiency and experience with computers, and provided ongoing support free of charge for three years. In the other 80 villages, no recruiters visited and no other intervention was made.
                         At the end of the study period, the researchers recorded data about the school attendance and health of the children in the villages.
                         
                         **Student's Task:** 
                         Express your opinion and response as a string in `response` in the `hw1_exercise_7b` function.
      
                         **Review Criteria:**
      
                         - The students are expected to express their opinion as `response` in the `hw1_exercise_7b` function. Their response must be logical and reasonable given the context of the question, hints and summary of the study. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e "Your response here" still exists in the function block instead of an answer attempt.
                         - **Note:** Critique the students opinion or answer by pointing out the flaws if their answer is off point or acknowledging the points raised if correct. Give subtle hints if the response is not completely correct.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with their opinion or response set to `response`.
                              ```
                              def hw1_exercise_7b():
                                response = "Student's will express their opinion here"
                                return response
                              ```
                  """
      },
      {
        "id": "homework1_Q8",
        "guidance":  """
                         **Question:** Suppose you want to find the **biggest** absolute difference between the numbers of degree recipients in the two years, among the three majors.
                                            
                        **Context:** Berkeley’s Office of Planning and Analysis provides data on numerous aspects of the campus. Adapted from the OPA website, the table below displays the numbers of degree recipients in three majors in the academic years 2008-2009 and 2017-2018.
                        | Major                              | 2008-2009    | 2017-2018   |
                        |------------------------------------|--------------|-------------|
                        | Gender and Women's Studies         |      17      |    28       |
                        | Linguistics                        |      49      |    67       |
                        | Rhetoric                           |      113     |    56       |
      
                         **Student's Task:** 
                         In the cell below, compute this value and call it `biggest_change`. Use a single expression (a single line of code) to compute the answer. Let Python perform all the arithmetic (like subtracting 49 from 67) rather than simplifying the expression yourself. The built-in `abs` function takes a numerical input and returns the absolute value. The built-in `max` function can take in 3 arguments and returns the maximum of the three numbers.                   
      
                         **Review Criteria:**
                         - The students are expected to place their choosen option as `biggest_change` in the `hw1_exercise_8` function. The value of biggest_change when computed must result to 57.
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                         - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again by providing subtle hints without revealing the answer.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with `biggest_change` when computed equalling 57. Different ways can be used to achieve this.
                              ```
                              def hw1_exercise_8():
                                biggest_change = max(abs(17 - 28), abs(49 - 67), abs(113 - 56))                        
                                return biggest_change
                              ```
                  """
      },
      {
        "id": "homework1_Q9",
        "guidance": """
                         **Question:** Which of the three majors had the **smallest** absolute difference?
                         
                        **Context:** Berkeley’s Office of Planning and Analysis provides data on numerous aspects of the campus. Adapted from the OPA website, the table below displays the numbers of degree recipients in three majors in the academic years 2008-2009 and 2017-2018.
                        | Major                              | 2008-2009    | 2017-2018   |
                        |------------------------------------|--------------|-------------|
                        | Gender and Women's Studies         |      17      |    28       |
                        | Linguistics                        |      49      |    67       |
                        | Rhetoric                           |      113     |    56       |
      
                         **Student's Task:** 
                         Choose the number that corresponds to the major with the smallest absolute difference. Assign either 1, 2, or 3 to the name `smallest_change_major` below to indicate your answer. Where each number corresponds to the following major:
      
                         1: Gender and Women's Studies  
                         2: Linguistics  
                         3: Rhetoric
      
                         **Review Criteria:**
      
                         - The students are expected to place their choosen option as `smallest_change_major` in the `hw1_exercise_9` function. The value of smallest_change_major must be set to the correct answer option given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                         - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again by providing subtle hints without revealing the answer.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with the correct answer choice set to `smallest_change_major`.
                              ```
                              def hw1_exercise_9():
                                smallest_change_major = 1
                                return smallest_change_major
                              ```
                  """
      },
      {
        "id": "homework1_Q10",
        "guidance": """
                         **Question:** For each major, define the "relative change" to be the following: $\large{\frac{\text{absolute difference}}{\text{value in 2008-2009}} * 100}$
                         
                        **Context:** Berkeley’s Office of Planning and Analysis provides data on numerous aspects of the campus. Adapted from the OPA website, the table below displays the numbers of degree recipients in three majors in the academic years 2008-2009 and 2017-2018.
                        | Major                              | 2008-2009    | 2017-2018   |
                        |------------------------------------|--------------|-------------|
                        | Gender and Women's Studies         |      17      |    28       |
                        | Linguistics                        |      49      |    67       |
                        | Rhetoric                           |      113     |    56       |
      
                         **Student's Task:** 
                         Fill in the code below such that `gws_relative_change`, `linguistics_relative_change` and `rhetoric_relative_change` are assigned to the relative changes for their respective majors.
      
                         **Review Criteria:**
                         - The students are expected to provide appropriate computation for `gws_relative_change`, `linguistics_relative_change` and `rhetoric_relative_change` in the `hw1_exercise_10` function, given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                         - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again by providing subtle hints without revealing the answer.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with equivalent computations recorded for `gws_relative_change`, `linguistics_relative_change` and `rhetoric_relative_change`.
                              ```
                              def hw1_exercise_10():
                                gws_relative_change = (abs(28-17) / 17) * 100
                                linguistics_relative_change = (abs(67-49) / 49) * 100
                                rhetoric_relative_change = (abs(56-113) / 113) * 100
                                return gws_relative_change, linguistics_relative_change, rhetoric_relative_change
                              ```
                    """
      },
      {
        "id": "homework1_Q11",
        "guidance": """
                         **Question:** Which of the three majors had the **smallest** absolute difference?
                         
                        **Context:** Berkeley’s Office of Planning and Analysis provides data on numerous aspects of the campus. Adapted from the OPA website, the table below displays the numbers of degree recipients in three majors in the academic years 2008-2009 and 2017-2018.
                        | Major                              | 2008-2009    | 2017-2018   |
                        |------------------------------------|--------------|-------------|
                        | Gender and Women's Studies         |      17      |    28       |
                        | Linguistics                        |      49      |    67       |
                        | Rhetoric                           |      113     |    56       |
      
                         **Student's Task:** 
                         Choose the number that corresponds to the major with the biggest relative change. Assign `biggest_rel_change_major` to 1, 2, or 3 where each number corresponds to to the following:
      
                         1: Gender and Women's Studies  
                         2: Linguistics  
                         3: Rhetoric
      
                         **Review Criteria:**
      
                         - The students are expected to place their choosen option as `biggest_rel_change_major` in the `hw1_exercise_11` function. The value of biggest_rel_change_major must be set to the correct answer option given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e ellipsis still exists in the function block instead of an answer attempt.
                         - **Note:** The correct answer must not be referenced if a students gets the answer wrong. Instead prompt them to try again by providing subtle hints without revealing the answer.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with the correct answer choice set to `biggest_rel_change_major`.
                              ```
                              def hw1_exercise_11():
                                # Assign biggest_rel_change_major to the number corresponding to the major with the biggest relative change.
                                biggest_rel_change_major = 1
                                return biggest_rel_change_major
                              ```  
                    """
      },
      {
        "id": "homework1_Q12",
        "guidance": """
                         **Question:**  The data were gathered by the following procedure, reported in the study. "Between January and June 1998, parents of children aged 2-16 years [...] that were seen as outpatients in a university pediatric ophthalmology clinic completed a questionnaire on the child’s light exposure both at present and before the age of 2 years." Was this study observational, or was it a controlled experiment? Explain.
                         **Student's Task:** 
                         Express your opinion and response as a string in `response` in the `hw1_exercise_12` function.
      
                         **Review Criteria:**
      
                         - The students are expected to express their opinion as `response` in the `hw1_exercise_12` function. Their response must be logical and reasonable given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e "Your response here" still exists in the function block instead of an answer attempt.
                         - **Note:** Critique the students opinion or answer by pointing out the flaws if their answer is off point or acknowledging the points raised if correct. Give subtle hints if the response is not completely correct.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with their opinion or response set to `response`.
                              ```
                              def hw1_exercise_12():
                                response = "Student's will express their opinion here"
                                return response
                              ```
                  """
      },
      {
        "id": "homework1_Q13",
        "guidance": """
                         **Question:**  The study found that of the children who slept with a room light on before the age of 2, 55% were myopic. Of the children who slept with a night light on before the age of 2, 34% were myopic. Of the children who slept in the dark before the age of 2, 10% were myopic. The study concluded that, "The prevalence of myopia [...] during childhood was strongly associated with ambient light exposure during sleep at night in the first two years after birth."
                         Do the data support this statement? You may interpret "strongly" in any reasonable qualitative way.
                         
                         **Student's Task:** 
                         Express your opinion and response as a string in `response` in the `hw1_exercise_13` function.
      
                         **Review Criteria:**
      
                         - The students are expected to express their opinion as `response` in the `hw1_exercise_13` function. Their response must be logical and reasonable given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e "Your response here" still exists in the function block instead of an answer attempt.
                         - **Note:** Critique the students opinion or answer by pointing out the flaws if their answer is off point or acknowledging the points raised if correct. Give subtle hints if the response is not completely correct.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with their opinion or response set to `response`.
                              ```
                              def hw1_exercise_13():
                                response = "Student's will express their opinion here"
                                return response
                              ```
                  """
      },
      {
        "id": "homework1_Q14",
        "guidance": """
                         **Question:**  On May 13, 1999, CNN reported the results of this study under the headline, "Night light may lead to nearsightedness." Does the conclusion of the study claim that night light causes nearsightedness?
                         
                         **Student's Task:** 
                         Express your opinion and response as a string in `response` in the `hw1_exercise_14` function.
      
                         **Review Criteria:**
      
                         - The students are expected to express their opinion as `response` in the `hw1_exercise_14` function. Their response must be logical and reasonable given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e "Your response here" still exists in the function block instead of an answer attempt.
                         - **Note:** Critique the students opinion or answer by pointing out the flaws if their answer is off point or acknowledging the points raised if correct. Give subtle hints if the response is not completely correct.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with their opinion or response set to `response`.
                              ```
                              def hw1_exercise_14():
                                response = "Student's will express their opinion here"
                                return response
                              ```
                  """
      },
      {
        "id": "homework1_Q15",
        "guidance": """
                         **Question:**  The final paragraph of the CNN report said that "several eye specialists" had pointed out that the study should have accounted for heredity.
                         Myopia is passed down from parents to children. Myopic parents are more likely to have myopic children, and may also be more likely to leave lights on habitually (since the parents have poor vision). In what way does the knowledge of this possible genetic link affect how we interpret the data from the study
                         
                         **Student's Task:** 
                         Express your opinion and response as a string in `response` in the `hw1_exercise_15` function.
      
                         **Review Criteria:**
      
                         - The students are expected to express their opinion as `response` in the `hw1_exercise_15` function. Their response must be logical and reasonable given the context of the question. 
                         - **Note:** You can only claim that a student is yet to attempt the problem if the placeholders i.e "Your response here" still exists in the function block instead of an answer attempt.
                         - **Note:** Critique the students opinion or answer by pointing out the flaws if their answer is off point or acknowledging the points raised if correct. Give subtle hints if the response is not completely correct.
                         
                        **Expected Completed Function:** The completed function of the students should look like this with their opinion or response set to `response`.
                              ```
                              def hw1_exercise_15():
                                response = "Student's will express their opinion here"
                                return response
                              ```
                  """
      },
    ]

