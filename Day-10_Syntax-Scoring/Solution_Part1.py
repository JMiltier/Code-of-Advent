# Syntax Scoring -- PART 1 --
# Find the corrupted lines (where start/end does not match)
# Possible sets of characters: <>, (), [], {}

TESTFILE = 'puzzle_input.txt'
# TESTFILE = 'sample_puzzle.txt'

'''
Objetives:
  1. Find and discard the corrupt lines; ignore incomplete.
  2. Score errors.
    ): 3 points
    ]: 57 points
    }: 1197 points
    >: 25137 points
'''

def analyzeLine(line):
  # key, value for scoring
  scoring = {')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137}
  # Expected syntax for open and close chars
  syntax = {')': '(',
            ']': '[',
            '}': '{',
            '>': '<',}
  closingSyntax = [')',']','}','>']
  stack = []

  for char in line:
    # check if closing character
    if char in closingSyntax:
      # clear out pairs (open/close)
      if syntax[char] == stack[-1]:
        stack.pop()
      else: return scoring[char]
    else: stack.append(char)
  return 0

def main():
  scoreTotal = 0
  lineScore = 0

  # Open and read puzzle file
  with open(TESTFILE, 'r') as input:
    for line in input.read().splitlines():
      lineScore = analyzeLine(line)
      # Add score; only positive value if corrupted
      scoreTotal += lineScore

  print(scoreTotal)

if __name__ == "__main__":
  main()
