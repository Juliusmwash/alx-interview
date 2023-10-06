#!/usr/bin/python3
"""
This module defines a function 'canUnlockAll'.
"""

def canUnlockAll(boxes):
    """
    Determine if all locked boxes can be opened using their keys.

    Args:
        boxes (list of list): A list of boxes, where each box contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    def dfs(box_index):
        """
        Recursive function to perform depth-first search (DFS) to unlock boxes.

        Args:
            box_index (int): Index of the current box.

        Returns:
            bool: True if all boxes can be opened, False otherwise.
        """
        if all(visited):
            return True  # All boxes are open, return True

        for key in boxes[box_index]:
            if key < n and not visited[key]:
                visited[key] = True
                if dfs(key):
                    return True

        return False

    return dfs(0)
