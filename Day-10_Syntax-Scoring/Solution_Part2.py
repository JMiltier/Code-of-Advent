# Syntax Scoring -- PART 2 --
# Finish out the incomplete lines, ignoring/removing the corrupted lines
# Possible sets of characters: <>, (), [], {}

TESTFILE = 'puzzle_input.txt'
# TESTFILE = 'sample_puzzle.txt'

'''
Objetives:
  1. Find and discard the corrupt lines, complete and score the incomplete lines.
  2. Score errors for each line. (each char is multiples line total by 5)
    ): 1 points
    ]: 2 points
    }: 3 points
    >: 4 points
  3. Return middle score
'''

def isCorrupted(line):
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
      else: return [], True
    else: stack.append(char)
  return stack, False

def scoreLine(line):
  # key, value for scoring
  scoring = {')': 1,
            ']': 2,
            '}': 3,
            '>': 4}
  score = 0
  for char in line:
    score *= 5
    score += scoring[char]
  return score

def main():
  # Expected syntax for open and close chars
  syntax = {'(': ')',
            '[': ']',
            '{': '}',
            '<': '>',}
  scoreTotals = []
  currupt = False
  currentLine = []
  closers = []

  # Open and read puzzle file
  with open(TESTFILE, 'r') as input:
    for line in input.read().splitlines():
      # Only accept incomplete lines
      currentLine, currupt = isCorrupted(line)
      if not currupt:
        while currentLine: # Reverse syntax to close
          closers.append(syntax[currentLine[-1]])
          currentLine.pop()
        scoreTotals.append(scoreLine(closers))
      closers.clear()

  print(sorted(scoreTotals)[len(scoreTotals) // 2])

if __name__ == "__main__":
  main()
