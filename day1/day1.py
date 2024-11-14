def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def group_sums(lines):
    """Calculates the sum of each group of lines, separated by blank lines."""
    sums = []
    current_sum = 0
    for line in lines:
        line = line.strip()  # Remove any whitespace and newline characters
        if line:  # If the line is not blank
            current_sum += int(line)  # Convert line to integer and add to current group sum
        else:
            # Blank line indicates end of current group
            if current_sum:
                sums.append(current_sum)
                current_sum = 0
    # Add the last group if it exists
    if current_sum:
        sums.append(current_sum)
    return sums

def find_largest_group_sum(sums):
    """Finds and returns the largest sum from the list of group sums."""
    return max(sums) if sums else 0

# Main function to execute the script
def main():
    filename = 'day1/sample.txt'
    lines = read_file(filename)
    sums = group_sums(lines)
    largest_sum = find_largest_group_sum(sums)
    print(f"The largest group sum is: {largest_sum}")

# Run the script
if __name__ == "__main__":
    main()
