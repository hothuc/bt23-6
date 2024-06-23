# Function to count overlapping occurrences
def count_overlapping(main_string, substring):
    count = start = 0
    main_lower = main_string.lower()  # Chuyển đổi main_string về chữ thường
    sub_lower = substring.lower()    # Chuyển đổi substring về chữ thường

    while start < len(main_string):
        start = main_lower.find(sub_lower, start)
        if start == -1:
            break
        count += 1
        start += 1  # Move to the next character to count overlapping
    return count
def main():
    main_string = input("keyword: ")
    name = input("name: ")
    score = 0
    substring_old = None  # To store the last entered substring for comparison
    while True:
        substring = input("word: ")
        if substring == substring_old or substring == "": #
            break
        count = count_overlapping(main_string, substring)
        score += count
        substring_old = substring    
    print(f"'{name}'' ' {score}")
if __name__ == "__main__":
    main()
