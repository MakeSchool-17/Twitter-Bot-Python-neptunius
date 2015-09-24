import sys
import random


def rearrange(words):
    random.shuffle(words)  # shuffle mutates the list in place!
    return ' '.join(words)

if __name__ == '__main__':
    args = sys.argv[1:]  # exclude script name in first argument
    print(rearrange(args))
