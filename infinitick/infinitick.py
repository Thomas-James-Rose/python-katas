import sys

def moveRight(cells, index):
  next_index = index + 1
  if next_index >= len(cells):
    cells.append(0)
  return cells, next_index, None

def moveLeft(cells, index):
  previous_index = index - 1
  if previous_index < 0:
    cells.insert(0, 0)
    return cells, 0, None
  else:
    return cells, previous_index, None

def increment(cells, index):
  new_value = cells[index] + 1
  cells[index] = new_value if new_value <= 255 else 0
  return cells, index, None

def decrement(cells, index):
  new_value = cells[index] - 1
  cells[index] = new_value if new_value >= 0 else 255
  return cells, index, None

def output_ascii(cells, index):
  print(chr(cells[index]))
  return cells, index, None

def raise_error(cells, index):
  raise(InterruptedError)

def skip_if_zero(cells, index):
  return cells, index, "]" if cells[index] == 0 else None

def skip_if_non_zero(cells, index):
  return cells, index, "[" if cells[index] > 0 else None

def execute(code):
  tokens = [token for token in code]
  token_index = 0
  cells = [0]
  cell_index = 0

  token_parsers = {
    ">": moveRight,
    "<": moveLeft,
    "+": increment,
    "-": decrement,
    "*": output_ascii,
    "&": raise_error,
    "[": skip_if_zero,
    "]": skip_if_non_zero,
  }

  while(True):
    token = tokens[token_index]
    cells, cell_index, skip_to = token_parsers[token](cells, cell_index)  
    previous_tokens = tokens[0:token_index]
    
    if skip_to != None and previous_tokens.count('[') == previous_tokens.count(']'):
      token_index = tokens.index(skip_to, token_index)
    
    if token_index + 1 < len(tokens):
      token_index = token_index + 1 
    else:
      token_index = 0

file = sys.argv[1]
infinitick_code = open(file, "r").read()
execute(infinitick_code)
