import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_grid", type=int)
    parser.add_argument("--unit_grid", type=int)
    parser.add_argument("--unit_n", type=int)
    parser.add_argument("--positions", type=int, nargs='+')
    parser.add_argument("--outdir", type=str)
    parser.add_argument("--file_name", type=str)
    args = parser.parse_args()


if __name__ == "__main__":
    main()
