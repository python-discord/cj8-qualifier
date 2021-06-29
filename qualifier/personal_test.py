from qualifier import *


print("Odd Samples")
print(make_table(rows=[["a"], ["ab"], ["abc"]]))
print(make_table(rows=[["a"], ["ab"], ["abc"]], centered=True))
print(make_table(rows=[["a", "d"], ["ab", "de"], ["abc", "def"]], labels=["1", "2"]))
print(make_table(rows=[["a", "d"], ["ab", "de"], ["abc", "def"]], labels=["1", "2"], centered=True))

print("Even Samples")
print(make_table(rows=[["a"], ["ab"], ["abc"], ["abcd"]]))
print(make_table(rows=[["a"], ["ab"], ["abc"], ["abcd"]], centered=True))
print(make_table(rows=[["a", "d"], ["ab", "de"], ["abc", "def"], ["abcd", "defg"]], labels=["1", "2"]))
print(make_table(rows=[["a", "d"], ["ab", "de"], ["abc", "def"], ["abcd", "defg"]], labels=["1", "2"], centered=True))