#!/usr/bin/python3
"""
This module defines the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Recursive function for finding keys that can open the locked boxes
    """
    def dfs(box_index, visited):
        visited[box_index] = True
        for key in boxes[box_index]:
            if not visited[key]:
                dfs(key, visited)

    n = len(boxes)
    visited = [False] * n
    dfs(0, visited)
    return all(visited)
