import sys

def print_chess_board(board):
  for x in board[::-1]:
    for y in x: 
      sys.stdout.write(y)
    sys.stdout.write("\n")

def move_knight(current_position, move): 
  return tuple(sum(t) for t in zip(current_position, move))

def knights_attack(start, end, obstacles):
  knight_pos = start
  distance_to_end = tuple(t[1] - t[0] for t in zip(knight_pos, end))

  chess_board = [["[ ]" for x in range(8)] for y in range(8)]
  chess_board[knight_pos[0]][knight_pos[1]] = "[K]"
  chess_board[end[0]][end[1]] = "[O]"
  print_chess_board(chess_board)

  move_num = 0
  while distance_to_end != (0, 0):
    move_num += 1
    print(f"\n Move {move_num}")
    chess_board[knight_pos[0]][knight_pos[1]] = "[ ]"
    if(distance_to_end[0]) >= 2:
      knight_pos = move_knight(knight_pos, (2, 1))
    chess_board[knight_pos[0]][knight_pos[1]] = "[K]"
    distance_to_end = tuple(t[1] - t[0] for t in zip(knight_pos, end))
    print_chess_board(chess_board)

  print("\n Done!")
  
knights_attack((1,1), (3,2), [])