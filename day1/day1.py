def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def calculate_elf_loads(lines):
    """Calculates the sum of each group of lines, separated by blank lines."""
    elves = []
    elf_load = 0
    for line in lines:
        line = line.strip()  # Remove any whitespace and newline characters
        if line:  # If the line is not blank
            elf_load += int(line)  # Convert line to integer and add to current group sum
        else:
            # Blank line indicates end of current group
            if elf_load:
                elves.append(elf_load)
                elf_load = 0
    # Add the last group if it exists
    if elf_load:
        elves.append(elf_load)
    return elves

def find_largest_group_sum(elves):
    """Finds and returns the largest sum from the list of group sums."""
    return max(elves) if elves else 0

def top_three_sum(elves):
    """Return the sum of the largest 3 in the list"""
    elves.sort(reverse=True)
    return sum(elves[:3])

def part_a():
    filename = 'sample.txt'
    filename = '../input/day1.txt'
    lines = read_file(filename)
    sums = calculate_elf_loads(lines)
    largest_sum = find_largest_group_sum(sums)
    print(f"The total calories of the largest load is: {largest_sum}")

def part_b():
    # filename = 'sample.txt'
    filename = '../input/day1.txt'
    lines = read_file(filename)
    elves = calculate_elf_loads(lines)
    top_three = top_three_sum(elves)
    print(f"The total calories of the largest 3 loads is: {top_three}")

def main():
    part_a()
    part_b()

if __name__ == "__main__":
    main()
