import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_grid", type=int)
    parser.add_argument("--unit_grid", type=int)
    parser.add_argument("--unit_n", type=int)
    parser.add_argument("--positions", type=int, nargs="+")
    parser.add_argument("--outdir", type=str)
    parser.add_argument("--file_name", type=str)
    args = parser.parse_args()

    if args.board_grid % args.unit_grid != 0:
        sys.exit()

    upper_value = (args.board_grid / args.unit_grid)**2
    if len(args.positions) == args.unit_n:
        if min(args.positions) < 1 or max(args.positions) > upper_value:
            sys.exit()
    else:
        sys.exit()

    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    with open(args.outdir + "/" + args.file_name + ".png", "w") as _:
        pass
    with open(args.outdir + "/" + args.file_name + ".mat", "w") as _:
        pass


if __name__ == "__main__":
    main()
