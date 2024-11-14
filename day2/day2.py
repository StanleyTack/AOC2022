def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

map_value = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3, }
rps_lookup = {
    (1, 2): 6,  # Rock vs Paper (Win)
    (2, 3): 6,  # Paper vs Scissors (Win)
    (3, 1): 6,  # Scissors vs Rock (Win)
    (1, 3): 0,  # Rock vs Scissors (Loss)
    (2, 1): 0,  # Paper vs Rock (Loss)
    (3, 2): 0   # Scissors vs Paper (Loss)
}
map_result = {'X': 0, 'Y': 3, 'Z': 6, 'A': 1, 'B': 2, 'C': 3, }
play_lookup = {
    #play, result: result
    (1, 0): 3,  # Rock, Loss -> Scissor
    (1, 6): 2,  # Rock, Win -> Paper
    (2, 0): 1,  # Paper, Loss -> Rock
    (2, 6): 3,   # Paper, Win -> Scissor
    (3, 0): 2,   # Scissors, Loss -> Paper
    (3, 6): 1,   # Scissors, Win -> Rock
}

def get_result(play_values):
    if play_values[0] == play_values[1]:
        return 3 # tie
    else:
        return rps_lookup.get((play_values[0], play_values[1]), "Invalid input")

def get_play(play_values):
    if play_values[1] == 3: #tie
        return play_values[0]
    else:
        return play_lookup.get((play_values[0], play_values[1]),"Invalid")


def calc_score(play_values):
    score = play_values[1] + play_values[2]
    return score

def get_scores_a(lines):
    scores = []
    for line in lines:
        play = line.split()
        play_values = list(map(lambda x: map_value.get(x, 0), play))
        result = get_result(play_values)
        play_values.append(result)
        scores.append(calc_score(play_values))
    return scores

def get_scores_b(lines):
    scores = []
    for line in lines:
        play = line.split()
        play_values = list(map(lambda x: map_result.get(x, 0), play))
        play = get_play(play_values)
        play_values.append(play)
        # print(play_values)
        scores.append(calc_score(play_values))
    return scores

def part_a():
    filename = 'sample.txt'
    filename = '../inputs/day2.txt'
    lines = read_file(filename)
    total_score = sum(get_scores_a(lines))
    print(f"The total score is: {total_score}")

def part_b():
    filename = 'sample.txt'
    filename = '../inputs/day2.txt'
    lines = read_file(filename)
    total_score = sum(get_scores_b(lines))
    print(f"The total score is: {total_score}")


def main():
    part_a()
    part_b()

if __name__ == "__main__":
    main()
