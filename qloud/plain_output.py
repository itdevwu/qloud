# Copyright (c) 20222 Zhenglong WU

from grover import freq

import sys


def main():
    experiment_iter = int(sys.argv[2])
    number = int(sys.argv[1])
    id = str(sys.argv[3])
    
    f = open(f"{id}.txt", "w")
    f.write(str(freq(number, experiment_iter)))
    f.close()


if __name__ == "__main__":
    main()
