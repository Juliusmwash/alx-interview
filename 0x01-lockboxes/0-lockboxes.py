#!/usr/bin/python3
"""
This module defines the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Determine if all locked boxes can be opened using their keys.

    Args:
        boxes (list of list): A list of boxes, where each box
        contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    def dfs(box_index, visited, n):
        """
        Perform depth-first search (DFS) to explore boxes
        and mark them as visited.

        Args:
            box_index (int): The index of the current box being explored.
            visited (list of bool): A list indicating whether each
            box has been visited.

            n (int): The total number of boxes.

        Returns:
            None
        """
        for box in boxes:
            if type(box) is not list:
                return False
        if box_index < n:
            if not boxes[box_index]:
                visited[box_index] = True
                dfs(box_index + 1, visited, n)
            else:
                visited[box_index] = True
            for key in boxes[box_index]:
                if key < n and not visited[key]:
                    dfs(key, visited, n)

    n = len(boxes)
    visited = [False] * n
    dfs(0, visited, n)
    return all(visited)
