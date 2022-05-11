# *Flashcard App*

A Python flashcard app for learning french words. Words are imported using pandas from a csv (english and french).
All of the words that were known (tick image clicked) are removed from a dictionary and exported into another csv.
After running the application again, the newly created csv is used instead of the original one.
The project was created using **tkinter**, **random**, and **pandas** imports.
It has the following functions :  
### *next_card*
- shows the next card with a new french word
- called when the **"cross"** image is clicked or at the end of the **is_known** function

### *flip_card*:
- flips the card after the timer runs out and shows the english translation
- called automatically after the timer runs out (3 seconds)

### *is_known*:
- calls the **next_card** function and removes the word from the dictionary
- called when the **"tick"** image is clicked
