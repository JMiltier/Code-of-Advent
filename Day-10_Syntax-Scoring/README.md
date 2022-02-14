# --- Day 10: Syntax Scoring ---
Details of project: https://adventofcode.com/2021/day/10#part2
Pyhon version: 3.9.9

## Part 1   
First thoughts of approach was realizing various opening brackets needed to have corresponding closing brackets. For this, I imagined a pointer that would look through the string/array (was first unsure of input format) from the beginning. Upon finding a closing bracket, it would look one position prior to see if it matches. If so, clear it, remove it, or whatever was needed. Then, proceed forward until the next closing bracket was found, and repeat this process.

Reading further, it's clear the input had incorrect matching opening/closing tags/brackets, causing that specific line (or chunk) to be corrupt. Otherwise, if there were open tags without an ending, it was fine (for now). Once a mismatched pair was found, return the scoring associated with that tag, and add it to a score total. 

For this first part, the score was solely based on the first corrupt bit/bracket per line, and summed. 

*Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?*   
Run code against [puzzle input](puzzle_input.txt) to see what was scored.  
`python3 Solution_Part1.py`  


## Part 2  
Reusing some code from the first part, the determination whether a line/chunk was corrupt had already been implented. Just a few minor changes to modify the return values. Then, once having a list of opening brackets for the incomplete line, the accompanying brackets needed to complete the line need to be scored. 

*Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?*  
Run code against [puzzle input](puzzle_input.txt) to see what was scored.  
`python3 Solution_Part2.py`
