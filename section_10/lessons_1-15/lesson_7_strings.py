a_string = "this is\na string split\t\tand tabbed"
print("=" * 80)
print(a_string)
print("*" * 80)
print(f"{a_string=}")

raw_string = r"this is\na string split\t\tand tabbed"
print("=" * 80)
print(raw_string)
print("*" * 80)
print(f"{raw_string=}")

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print("=" * 80)
print(b_string)
print("*" * 80)
print(f"{b_string=}")

backslash_string = "this is a backslash \folowwed by some text"
print("=" * 80)
print(backslash_string)

backslash_string = "this is a backslash \\folowwed by some text"
print("=" * 80)
print(backslash_string)

error_string = r"this string ends with \\"