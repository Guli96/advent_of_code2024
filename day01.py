def assemble_arrays(lines):
    arr1 = []
    arr2 = []

    for line in lines:
        vals = line.split("   ")
        arr1.append(int(vals[0]))
        arr2.append(int(vals[1]))

    arr1.sort()
    arr2.sort()

    return arr1, arr2

def part1(lines):
    arr1, arr2 = assemble_arrays(lines)

    diff = 0

    for i in range(len(arr1)):
        diff += abs(arr1[i] - arr2[i])

    return diff

def part2(lines):
    arr1, arr2 = assemble_arrays(lines)

    diff = 0

    nums_dict = dict()

    for num in arr2:
        if num not in nums_dict:
            nums_dict[num] = 1
        else:
            nums_dict[num] += 1

    for num in arr1:
        if num in nums_dict:
            diff += num * nums_dict[num]

    return diff