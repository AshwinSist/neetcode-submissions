class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)

        for c in range(9):
            for r in range(9):
                if board[c][r] == ".":
                    continue
                elif (board[c][r] in rows[r] or 
                      board[c][r] in cols[c] or
                      board[c][r] in square[(c//3,r//3)]):
                      return False
                cols[c].add(board[c][r])
                rows[r].add(board[c][r])
                square[(c//3,r//3)].add(board[c][r])
        return True
        