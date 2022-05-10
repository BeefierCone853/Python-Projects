# *Snake Game*

Snake game created with Python which has 3 additional modules and 3 additional classes: Food, Scoreboard and Snake.
All of the mentioned classes inherit the **Turtle** class from the import **turtle**.
The game also keeps track of the highest score and saves it into the **data.txt** file.  
*Food* contains the following method:
1. **refresh** - changes the position of food once picked eaten by the snake

*Scoreboard*:
1. **update_scoreboard** - updates the score when food is eaten by the snake
2. **increase_score** - increases the score once food is eaten
3. **game_over** - displays a message indicating the game is over

*Snake*:
1. **create_snake** - creates segments (squares) to form a snake
2. **move** - moves the snake forward
3. **extend** - calls upon the add_segment method to extend the snake by one square
4. **add_segment** - adds a segment (square) to the snake
5. **up**, **down**, **left**, **right** - move the snake in a certain direction, also the following changes of direction are not allowed: up to down and vice versa, left to right and vice versa

