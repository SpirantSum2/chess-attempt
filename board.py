
class Board:
    def __init__(self, fen=None):
        if fen == None:
            self.board = self.from_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        else:
            self.board = self.from_fen(fen)


    def from_fen(self, fen):
        split_fen = fen.split(" ")
        board_data = split_fen[0]

        ranks = board_data.split("/")
        board = []
        for rank in ranks:
            for letter in rank:
                if letter.isnumeric(): # a number
                    board.extend([None for _ in range(int(letter))]) # this works because the number can be at max 8, meaning it can only be 1 char long
                else:
                    board.append(letter)
        
        return board

    
