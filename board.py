import numpy as np

class Board():
    # 定数
    BLANK = 0
    BLACK = 1
    WHITE = -1
    BOARDSIZE = 8
    CHARACTERCONVERTINGTABLE = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

    def __init__(self):
        # 盤面を生成し、真ん中に石を置く
        self.board = np.zeros([self.BOARDSIZE,self.BOARDSIZE])
        self.board[3][3] = self.BLACK
        self.board[4][4] = self.BLACK
        self.board[3][4] = self.WHITE
        self.board[4][3] = self.WHITE

    # 盤面表示
    def dispBoard(self):
        for boardCols in self.board:
            for field in boardCols:
                if field == self.BLANK:
                    state = '×'
                elif field == self.BLACK:
                    state = '●'
                elif field == self.WHITE:
                    state = '○'
                print(state,end='')
            print('')

    # 石を盤面に置けるか
    def canPutStoneOnBoard(self,pos):
        pass

    # アドレスを配列のindexに変換する
    # A1→(1,1),B1→(1,2)
    def convertAddressToIndex(pos):
        pass

    def updateBoardStatus(self):
        pass
