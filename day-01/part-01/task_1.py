from __future__ import annotations


def read_input() -> list[int]:
    with open('input.txt', 'r') as f:
        return [int(line) for line in f.readlines()]

def main():
    
    vals = read_input()

    res = 0
    prev = max(vals)
    for val in vals:
        if prev < val:
            res += 1
        prev = val

    print(res)

if __name__ == '__main__':
    raise SystemExit(main())

# 1121