class player():
    # 定数
    BLACK = 1
    WHITE = -1
    
    # 初めに駒の色を設定する
    def __init__(self,color):
        if color == BLACK:
            myStones = BLACK
        else:
            myStones = WHITE

    # 石を置く
    def setStoneOnBoard(self,address):
