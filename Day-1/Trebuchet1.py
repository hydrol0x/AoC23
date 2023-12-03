with open('trebuchet1.in', 'r') as file:
    nums = []
    for line in file:
        num = ''
        for char in line:
            if char.isnumeric():
                num+=char
                break
        for char in line[::-1]:
            if char.isnumeric():
                num+=char
                break
        nums.append(int(num))

    print(nums)
    print(sum(nums))