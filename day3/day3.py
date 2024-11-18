import string

day = 3
map_value = {ch: idx + 1 for idx, ch in enumerate(string.ascii_lowercase)}
map_value.update({ch: idx + 27 for idx, ch in enumerate(string.ascii_uppercase)})

def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines


def get_priorities(line):
    play_values = list(map(lambda x: map_value.get(x, 0), line))
    # print(play_values)
    return play_values

#pockets = [('vJrwpWtwJgWr', 'hcsFMMfFFhFp')]
# updated to work with any number of tuples in the input list
def get_shared_items(input_list):
    shared_items = []
    for tup in input_list:
        # Find the intersection of characters across all elements in the tuple
        shared = set(tup[0]).intersection(*map(set, tup[1:]))
        if shared:
            # If there's a shared item, add the first one to the result list
            shared_items.append(shared.pop())
    # print(shared_items)
    return shared_items
    # shared_items = ['p']

def split_into_pockets(lines):
    pockets = []
    for line in lines:
        # Split the string into two halves
        mid = len(line) // 2
        pockets.append((line[:mid], line[mid:]))
    return pockets

def split_into_groups(lines):
    groups = []
    for i in range(0, len(lines), 3):
        # Group every 3 lines into a tuple
        groups.append((lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()))
    # print(groups)
    return groups


def part_a():
    filename = 'sample.txt'
    filename = f'../inputs/day{day}.txt'
    lines = read_file(filename)
    # split each line into tuples (first half, second half)
    pockets = split_into_pockets(lines)
    # determine which item is shared between each pocket
    # pockets = [('vJrwpWtwJgWr', 'hcsFMMfFFhFp')]
    shared_items = get_shared_items(pockets)
    # shared_items = ['p', 'L', 'P', 'v', 't', 's']
    # convert letters to numbers
    priorities = get_priorities(shared_items)
    # sum the priorities
    total_score = sum(priorities)
    print(f"The sum of priorities for items is: {total_score}")


def part_b():
    filename = 'sample.txt'
    filename = f'../inputs/day{day}.txt'
    lines = read_file(filename)
    # split each line into tuples (first half, second half)
    groups = split_into_groups(lines)
    # determine which item is shared between each pocket
    # groups = [('vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg')]
    shared_items = get_shared_items(groups)
    # shared_items = ['p', 'L', 'P', 'v', 't', 's']
    # convert letters to numbers
    priorities = get_priorities(shared_items)
    # sum the priorities
    total_score = sum(priorities)
    print(f"The sum of priorities for groups is: {total_score}")


def main():
    part_a()
    part_b()

if __name__ == "__main__":
    main()
