# *Pong Game*

Pong game created with Python which has 3 additional modules and 3 additional classes: Paddle, Scoreboard and Ball.
All of the mentioned classes inherit the **Turtle** class from the import **turtle**. Classes and their methods:
### *Ball*
1. **move** - moves the ball
2. **bounce_y** - reverses the y axis of the ball and increases the movement speed of the ball
3. **bounce_x** - reverses the x axis of the ball and increases the movement speed of the ball
4. **reset_position** - resets the position of the ball and it's movement speed to the default value

### *Scoreboard*:
1. **update_scoreboard** - updates the score
2. **l_point** - increases the score for the player on the left side
3. **r_point** - increases the score for the player on the right side

### *Paddle*:
1. **go_up** - moves the paddle upward
2. **go_down** - moves the paddle downward