def part1(lines):
    arr1 = []
    arr2 = []

    for line in lines:
        vals = line.split("   ")
        arr1.append(int(vals[0]))
        arr2.append(int(vals[1]))

    arr1.sort()
    arr2.sort()

    diff = 0

    for i in range(len(arr1)):
        diff += abs(arr1[i] - arr2[i])

    return diff

