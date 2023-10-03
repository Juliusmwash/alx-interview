# Can Unlock All Boxes

This Python program checks if all the locked boxes in a set of boxes can be opened using their keys. It employs a recursive depth-first search (DFS) algorithm to determine if all boxes are accessible starting from the first box.

## Table of Contents

- [Usage](#usage)
- [Algorithm](#algorithm)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Usage

To use this program, you can call the `canUnlockAll` function in your Python code and provide a list of boxes as input. The function will return `True` if all boxes can be opened and `False` otherwise.

```python
from can_unlock_boxes import canUnlockAll

boxes = [[1], [2], [3], [4], []]
result = canUnlockAll(boxes)
print(result)  # Output: True
```

## Algorithm

The program employs a depth-first search (DFS) algorithm to explore the boxes. Here's how it works:

1. Start from the first box (index 0), mark it as visited.
2. For each key in the current box, if the corresponding box hasn't been visited yet, recursively explore that box.
3. Continue this process until all reachable boxes have been visited.
4. Finally, check if all boxes have been visited. If they have, return `True`; otherwise, return `False`.

## Example

```python
from can_unlock_boxes import canUnlockAll

boxes = [[1], [2], [3], [4], []]
result = canUnlockAll(boxes)
print(result)  # Output: True
```

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository, make changes, and submit a pull request. We welcome improvements and bug fixes
