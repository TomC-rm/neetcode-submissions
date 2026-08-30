from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for column in range(9):
                val = board[row][column]
                box = (row // 3, column // 3)
                if val == ".":
                    continue
                if (val in rows[row] or val in columns[column] or val in boxes[box]):
                    return False
                rows[row].add(val)
                columns[column].add(val)
                boxes[box].add(val)
        return True