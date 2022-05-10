# *Quiz project*

Simple quiz game that requires the user to answer with **true** or **false**.  
The folder contains 4 python files : main, data, question_model and quiz_brain.  
*Data* python file contains a **list** inside which are **dictionaries** with questions and their true/false answers.    
*Question_model* contains the class **Question** with text (questions) and answer attributes.  
*Quiz_brain* file contains the class **QuizBrain** which has 3 attributes : number of questions, list of questions
and an attribute to keep track of the score. It also contains the following methods :
1. "still_has_questions" - checks whether all of the questions have been printed on the screen
2. "next_question" - prints the next question and asks the user input true/false
3. "check_answer" - checks whether the user answered right or wrong and prints out the current score


