#!/usr/bin/python3

# stdlib imports
import argparse
import sys

# stdlib partial imports

# 3rd-party module imports

# 3rd-party module partial imports

# typing imports
from typing import Optional, Union

# Globals


# Classes
class Day01Solver():

  @property
  def first_column_lines(self) -> list[int]:
    if getattr(self, '_first_column_lines', None) is None:
      self._first_column_lines = self._parse_column(0)
      self.first_column_lines.sort()
    return self._first_column_lines

  @property
  def second_column_lines(self) -> Optional[list[int]]:
    if getattr(self, '_second_column_lines', None) is None:
      self._second_column_lines = self._parse_column(1)
      self._second_column_lines.sort()
    return self._second_column_lines

  def __init__(self, input_file: str) -> None:
    self.input_file: str = input_file

  def solve(self) -> None:
    self._solve_part_one()
    self._solve_part_two()

  def _parse_column(self, column_number: int) -> list[int]:
    with open(file=self.input_file, mode='r', encoding='utf-8') as input_file:
      lines: list[str] = input_file.readlines()

    column_lines: list[int] = []

    for line in lines:
      column_lines.append(int(line.split()[column_number]))

    return column_lines

  def _solve_part_one(self) -> None:
    total_distance: int = 0

    assert self.first_column_lines
    assert self.second_column_lines

    for pair in zip(self.first_column_lines, self.second_column_lines):
      distance: int = abs(pair[0] - pair[1])
      total_distance += distance

    print(f'Total distance of [ {len(self.first_column_lines)} ] pairs: {total_distance}')

  def _solve_part_two(self) -> None:
    similarity_score: int = 0

    assert self.first_column_lines
    assert self.second_column_lines

    for item in self.first_column_lines:
      if item not in self.second_column_lines:
        continue
      similarity_score += (item * self.second_column_lines.count(item))

    print(f'Similarity score: {similarity_score}')


# Exception classes


# Global functions
## Custom arg parser
def create_arg_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser(description='Meant to solve AoC 2024\'s day-01 puzzle.')

  parser.add_argument(
    '-f',
    '--file',
    action='store',
    default=None,
    dest='input_file',
    help='The filepath to the input',
    required=True,
  )

  return parser


## Main
def main() -> None:
  try:
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args()

    Day01Solver(input_file=args.input_file).solve()

  except KeyboardInterrupt:
    sys.exit(130)


if __name__ == '__main__':
  main()
