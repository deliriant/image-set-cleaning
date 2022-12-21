with open('titles.txt') as f_a, open('imagetitles.txt') as f_b:
    a_lines = set(f_a.read().splitlines())
    b_lines = set(f_b.read().splitlines())
for line in a_lines:
    print(line, '->', line in b_lines)