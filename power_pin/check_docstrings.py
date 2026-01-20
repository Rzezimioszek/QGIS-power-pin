with open("power_pin.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

in_docstring = False
count = 0
for i, l in enumerate(lines):
    if l.count('"""') % 2 == 1:
        count += 1
        in_docstring = not in_docstring
    if in_docstring and i > 570:
        print("Line", i+1, "Still in docstring!")
        break
