# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        i =0
        j = 0
        matrix = [[-1] * n for _ in range(m)]
        curr = head
        currDir = 0
        directions = {
            0: lambda i,j:(j + 1 < len(matrix[0]) and matrix[i][j + 1] == -1, (i, j + 1)),
            1: lambda i,j: (i + 1 < len(matrix) and matrix[i+1][j] == -1, (i + 1,j)),
            2: lambda i, j: (j - 1 >= 0 and matrix[i][j-1] == -1, (i, j - 1)),
            3: lambda i,j: (i - 1 >= 0 and matrix[i-1][j] == -1, (i - 1, j))
        }
        # 0 = right, 1 = down, 2 = left, 3 = up
        def next(i, j, currDir):
            canMove, update= directions[currDir](i, j)
            if canMove:
                return update[0], update[1], currDir
            else:
                for direction in directions:
                    if direction != currDir:
                        canMove, update = directions[direction](i, j)
                        if canMove: return update[0], update[1], direction

        while curr:
            matrix[i][j] = curr.val
            update = next(i, j, currDir)
            if update:
                i, j,currDir = update
            curr = curr.next
        return matrix
