with open('Day-2\\day2in.txt', 'r') as file:
    total = 0
    total_power = 0
    for line in file:
        game_id = line.split(': ')[0].split(" ")[1]
        rounds = line.split(': ')[1].strip().split('; ')
        
        possible = True
        mins = {'red': 0, 'green': 0, 'blue': 0}
        for round in rounds:
            color_freq = {'red': 0, 'green': 0, 'blue': 0}
            colors = round.split(", ")
            for color_group in colors:
                freq, color = color_group.split(" ")
                color_freq[color] += int(freq)
                mins[color] = max(mins[color], int(freq))
            
            if color_freq['blue'] > 14 or color_freq['red'] > 12 or color_freq['green'] > 13:
                possible = False
        
        power = 1
        for val in mins.values():
            power *= val        
        # print(f"Game {game_id} power: {power}")
        total_power += power
        
        if possible:
            total += int(game_id)

print(total)
print(f"total power: {total_power}")
