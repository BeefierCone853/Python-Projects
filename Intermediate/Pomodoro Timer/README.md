# *Pomodoro timer*

A Pomodoro timer created using imports **tkinter** and **math**.
After 25 minutes have passed (work) the timer starts counting from 5 minutes (break).
The following is repeated 4 times after which the timer starts counting from 20 minutes, signifying a long break.
The program has the following functions :  

### *reset_timer*
 - Resets the timer and changes the text fields to their starting values, as well as restarts the rep count
 - Initiated once the **"Reset"** button is clicked

### *start_timer*
 - Starts the timer, checks and adds reps
 - Initiated once the **"Start"** button is clicked

### *count_down*
 - Counts down the time and adds checkmarks for every rep passed.
