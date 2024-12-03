import re

def part1(lines):
    res = 0
    for line in lines:
        x = re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", line)
        for num_pair in x:
            res += int(num_pair[0])*int(num_pair[1])
    return res

def get_substrings(lines:list[str]):
    full_text = ''.join(lines)
    dos = [m.start() for m in re.finditer('do\(\)', full_text)]
    donts = [m.start() for m in re.finditer('don\'t\(\)', full_text)]

    substring_ranges = [range(0,donts[0])]
    donts.pop(0)



    print(dos)
    print(donts)

def part2(lines:list[str]):
    res = 0
    full_text = ''.join(lines)
    #full_text = "do()" + full_text #cheatyface
    print(get_substrings(lines))
    x = re.findall("do\(\)(.*)don't\(\)", full_text)
    print(full_text)
    for enabled in x:
        print(enabled)
        res += part1([enabled])
    return res