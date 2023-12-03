tokens_alpha = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

with open(r'trebuchet3.in', 'r') as file:
    nums = []
    for line in file:
        num = ''
        for i, char in enumerate(line):
            if char.isnumeric():
                num+=char
                break
            if i < len(line)-2:
                window = line[i:i+3]
                # print(f"[WINDOW 3] {window}")
                if window in tokens_alpha:
                    num+=tokens_alpha[window]
                    break
            if i < len(line)-3:
                window = line[i:i+4]
                # print(f"[WINDOW 4] {window}")
                if window in tokens_alpha:
                    num+=tokens_alpha[window]
                    break
            if i < len(line)-4:
                window = line[i:i+5]
                # print(f"[WINDOW 5] {window}")
                if window in tokens_alpha:
                    num+=tokens_alpha[window]
                    break
        for i, char in enumerate(line[::-1]):
            if char.isnumeric():
                num+=char
                break
            if i < len(line)-2:
                window = line[::-1][i:i+3]
                window = window[::-1]
                # print(f"[WINDOW 3 RVRS] {window}")
                if window in tokens_alpha:
                    num+=tokens_alpha[window]
                    break
            if i < len(line)-3:
                window = line[::-1][i:i+4]
                window = window[::-1]
                # print(f"[WINDOW 4 RVRS] {window}")
                if window in tokens_alpha:
                    num+=tokens_alpha[window]
                    break
            if i < len(line)-4:
                window = line[::-1][i:i+5]
                window = window[::-1]
                # print(f"[WINDOW 5 RVRS] {window}")
                if window in tokens_alpha:
                    num+=tokens_alpha[window]
                    break 
            
        if num:
            nums.append(int(num))

    print(sum(nums))