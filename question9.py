class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        zero_to_nine = ("1","2","3","4","5","6","7","8","9")
        print("Board 1")
        for i in range(0,len(board)):
            visited = []
            for j in range(0,len(board[0])):
                print(i,j)
                if board[i][j] in visited:
                    return False
                if board[i][j] !="." and board[i][j] in zero_to_nine:
                    visited.append(board[i][j])
                    print("V",visited)
        print("board 2")
        for j in range(0,len(board)):
            visited = []
            for i in range(0,len(board[0])):
                print(i,j)
                if board[i][j] in visited:
                    return False
                if board[i][j] !="." and board[i][j] in zero_to_nine:
                    visited.append(board[i][j])
                    print("V",visited)
        visited=[]
        for box_row in range(0, 9, 3):      # box_row = 0, 3, 6
            for box_col in range(0, 9, 3):  # box_col = 0, 3, 6
                visited = []
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != ".":
                            if val in visited:
                                return False
                            visited.append(val)
        return True