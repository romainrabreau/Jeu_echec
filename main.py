import chess


def print_board(board: chess.Board):
    print(board.unicode(invert_color=False))


def main():
    board = chess.Board()
    while not board.is_game_over():
        print_board(board)
        move_str = input(f"{'White' if board.turn == chess.WHITE else 'Black'} to move: ")
        try:
            move = chess.Move.from_uci(move_str.strip())
            if move in board.legal_moves:
                board.push(move)
            else:
                print("Illegal move. Try again.")
        except ValueError:
            print("Invalid format. Use UCI format like e2e4.")
    print_board(board)
    result = board.result(claim_draw=True)
    if board.is_checkmate():
        winner = 'White' if board.turn == chess.BLACK else 'Black'
        print(f"Checkmate! {winner} wins. Result: {result}")
    else:
        print(f"Game over. Result: {result}")


if __name__ == '__main__':
    main()
