# Pascal's Triangle Interview Project

## Overview

This project is a Python implementation of Pascal's Triangle and serves as a solution to a common interview question. Pascal's Triangle is a mathematical construct that produces a triangular array of binomial coefficients.

## Features

- Generates Pascal's Triangle up to a specified number of rows.
- Demonstrates the algorithmic approach to solve the problem efficiently.

## Requirements

- Python 2/3
- [Optional] Any IDE or text editor for code review

## Usage

1. Clone the repository:

   git clone https://github.com/Juliusmwash/alx-interview.git

2. Navigate to the project directory:

   cd alx-interview/0x00-pascal_triangle

3. Run the Python script:

   python 0-main.py or ./0-main.py

4. Open the 0-main.py on your favourite code editor and change the value of n to your liking. This value 'n' determines the length/height of the triangle.


## Example Usage

### 0-main.py

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

## Acknowledgments
Inspired by the Pascal's Triangle mathematical concept.
