#!/usr/bin/python3
"""
This module defines a function 'canUnlockAll'.
"""

def canUnlockAll(boxes):
    """
    Determine if all locked boxes can be opened using their keys.

    Args:
        boxes (list of list): A list of boxes, where each box contains
        keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]  # Initialize a stack for iterative DFS

    while stack:
        box_index = stack.pop()
        for key in boxes[box_index]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
