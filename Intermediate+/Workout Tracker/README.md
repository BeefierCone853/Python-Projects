# *Workout Tracker*

Asks for user input on which exercise they've done. Once entered, if the exercise can be found on the 
**exercise_endpoint** using API, it is entered into a google sheet (date, time, exercise, average duration, average calories burned). 
The google sheet is accessed with an API using *"Sheety"*. API keys, IDs, endpoints and tokens are all stored as environment variables.
