# Dice-Game
Text based 2 player dice game

OCR CS GCSE J277 NEA project choice 2

# Requirements
- The points rolled on each player’s dice are added to their score.
- If the total is an even number, an additional 10 points are added to their score.
- If the total is an odd number, 5 points are subtracted from their score.
- If they roll a double, they get to roll one extra die and get the number of points rolled added to their score.
- The score of a player cannot go below 0 at any point.
- The person with the highest score at the end of the 5 rounds wins.
- If both  players  have  the  same  score  at  the  end  of  the  5  rounds,  they  each  roll  1  die  and  whoever gets the highest score wins (this repeats until someone wins).

# How I made it
Text based program that uses functions for main systems

Uses an external file to store users and passwords, read from for verification

Uses an external file to store users and highest winning scores, read from to display top 5 highest scores

Handles all sorts of scenarios given by the prompt

# What I learnt
- r/w from and to .txt files
- functional programming
- combining knowledge upto that point
- creating a plan and iterative testing

# Improvements
Overall clean up of messy code would be initial improvements

I would make many more functions as currently there are multiple reusable sections of code all in a single function, and because I have since become more accustomed to decomposing before coding and creating functions.

Keeping it text based, I would add a dice rolling text art to signify the rolling of the dice, in order to make it more engaging for the user.

Further improvements could include creating a very basic GUI with a dice animation and visually indicating the game's progress.
