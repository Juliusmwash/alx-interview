#!/usr/bin/python3
"""
This module defines the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Recursive function for finding keys that can open the locked boxes
    """
    def dfs(box_index, visited, n):
        visited[box_index] = True
        for key in boxes[box_index]:
            if key < n and not visited[key]:
                dfs(key, visited, n)

    n = len(boxes)
    visited = [False] * n
    dfs(0, visited, n)
    return all(visited)
