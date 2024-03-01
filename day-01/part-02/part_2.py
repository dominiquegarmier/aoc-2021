from __future__ import annotations


def read_input() -> list[int]:
    with open('input.txt', 'r') as f:
        return [int(line) for line in f.readlines()]

def get_windows(vals: list[int]) -> list[int]:
    windows = []
    for i, _ in enumerate(vals):
        try:
            windows.append(sum(vals[i:i+3]))
        except Exception:
            break

    return windows


def main():
    
    vals = read_input()
    vals = get_windows(vals)

    res = 0
    prev = max(vals)
    for val in vals:
        if prev < val:
            res += 1
        prev = val

    print(res)

if __name__ == '__main__':
    raise SystemExit(main())

# 1065