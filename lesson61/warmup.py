#  glob

from pathlib import Path

root = Path("demo61")
(root / "sub").mkdir(parents=True, exist_ok=True)
for name in ["b.txt", "a.txt", "c.log", "sub/d.txt"]:
    (root / name).write_text("x", encoding="utf-8")


for txt_file in sorted(root.glob("*.txt")):
    print(txt_file)

print(Path("a.txt").parent, Path("demo61/a.txt").parent)



#  pick_max 改写


import math as m
from math import inf
from statistics import mean
from statistics import median as mean


def pick_max(nums):
    """
    返回 nums 中的最大值；nums 为空时返回 None。"""
    if not nums:
        return None

    best = nums[0]
    for n in nums:
        if n > best:
            best = n
    return best


print(pick_max([-3, -1, -7]))
print(pick_max([]))
print(pick_max([0, -2]))


