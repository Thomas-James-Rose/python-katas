import sys

def print_chess_board(board):
  for x in board[::-1]:
    for y in x: 
      sys.stdout.write(y)
    sys.stdout.write("\n")


def calculate_next_move(distance_to_end):

  # One move to finish!
  if(distance_to_end[0] == 2 and distance_to_end[1] == 1):
    return (2, 1)
  elif(distance_to_end[0] == 1 and distance_to_end[1] == 2):
    return (1, 2)
  if(distance_to_end[0] == 2 and distance_to_end[1] == -1):
    return (2, -1)
  elif(distance_to_end[0] == 1 and distance_to_end[1] == -2):
    return (1, -2)
  elif(distance_to_end[0] == -2 and distance_to_end[1] == 1):
    return (-2, 1)
  elif(distance_to_end[0] == -1 and distance_to_end[1] == 2):
    return (-1, 2)
  elif(distance_to_end[0] == -2 and distance_to_end[1] == -1):
    return (-2, -1)
  elif(distance_to_end[0] == -1 and distance_to_end[1] == -2):
    return (-1, -2)

  # Two moves to finish!
  elif(distance_to_end[0] == 0 and distance_to_end[1] == -2):
    return(2, -1)
  elif(distance_to_end[0] == 0 and distance_to_end[1] == 2):
    return(2, 1)
  elif(distance_to_end[0] == -2 and distance_to_end[1] == 0):
    return(-1, 2)
  elif(distance_to_end[0] == 2 and distance_to_end[1] == 0):
    return(1, 2)
  elif(distance_to_end[0] == 1 and distance_to_end[1] == 1):
    return(2, -1)
  elif(distance_to_end[0] == -1 and distance_to_end[1] == 1):
    return(-2, -1)
  elif(distance_to_end[0] == -1 and distance_to_end[1] == -1):
    return(1, -2)
  elif(distance_to_end[0] == 1 and distance_to_end[1] == -1):
    return(2, 1)

  # Three moves to finish!
  elif(distance_to_end[0] == 0 and distance_to_end[1] == 1):
    return(2, 1)
  elif(distance_to_end[0] == 0 and distance_to_end[1] == -1):
    return(2, -1)
  elif(distance_to_end[0] == 1 and distance_to_end[1] == 0):
    return(1, 2)
  elif(distance_to_end[0] == -1 and distance_to_end[1] == 0):
    return(-1, 2)


  # Other garbage
  elif(distance_to_end[0] > 2):
    return (2, 1)
  elif(distance_to_end[0] < -2):
    return (-2, 1)
  else:
    return (0, 0)

def move_knight(current_position, move): 
  return tuple(sum(t) for t in zip(current_position, move))

def knights_attack(start, end, obstacles):
  knight_pos = start
  distance_to_end = tuple(t[1] - t[0] for t in zip(knight_pos, end))

  chess_board = [["[ ]" for y in range(8)] for x in range(8)]
  chess_board[knight_pos[0]][knight_pos[1]] = "[♘]"
  chess_board[end[0]][end[1]] = "[👑]"
  print_chess_board(chess_board)

  move_num = 0
  while distance_to_end != (0, 0) and move_num < 20:
    move_num += 1
    print(f"\n Move {move_num}")
    chess_board[knight_pos[0]][knight_pos[1]] = "[ ]"
    knight_pos = move_knight(knight_pos, calculate_next_move(distance_to_end))
    chess_board[knight_pos[0]][knight_pos[1]] = "[♘]"
    distance_to_end = tuple(t[1] - t[0] for t in zip(knight_pos, end))
    print_chess_board(chess_board)

  print("\n Done!")
  
knights_attack((1,1), (1,2), [])