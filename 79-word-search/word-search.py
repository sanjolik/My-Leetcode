class Solution:
    def exist(self, board, word):
        def backtrack(i, j, k, visited):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited or board[i][j] != word[k]:
                return False
            
            visited.add((i, j))
            
            if (backtrack(i+1, j, k+1, visited) or 
                backtrack(i-1, j, k+1, visited) or 
                backtrack(i, j+1, k+1, visited) or 
                backtrack(i, j-1, k+1, visited)):
                return True
            
            visited.remove((i, j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backtrack(i, j, 0, set()):
                    return True
        return False


