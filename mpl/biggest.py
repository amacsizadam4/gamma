#!/usr/bin/env python3
"""Very small utility: compare two integers and print which is biggest.

Usage:
  - Pass two integers as command-line args: `python biggest.py 3 5`
  - Or run with no args and follow the prompts.
"""

import sys


def biggest(a: int, b: int) -> str:
	if a > b:
		return f"{a} is bigger than {b}"
	if b > a:
		return f"{b} is bigger than {a}"
	return f"{a} and {b} are equal"


def main() -> None:
	if len(sys.argv) >= 3:
		try:
			a = int(sys.argv[1])
			b = int(sys.argv[2])
		except ValueError:
			print("Error: provide two integers, e.g. `python biggest.py 2 7`")
			sys.exit(1)
	else:
		try:
			a = int(input("Enter first integer: "))
			b = int(input("Enter second integer: "))
		except ValueError:
			print("Error: inputs must be integers.")
			sys.exit(1)

	print(biggest(a, b))


if __name__ == "__main__":
	main()
