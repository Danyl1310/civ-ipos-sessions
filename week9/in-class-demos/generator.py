# Our generator
def get_lines(filename):
    print("Opening file...")
    with open(filename) as f:
        for line in f:
            print("Reading line from disk")
            yield line.strip()


for line in get_lines("./large_data.txt"):
    print("Processing:", line)
    # break


    def get_even_numbers(limit):
        break
        for num in range(limit + 1):
            if num % 2 == 0:
                yield num
