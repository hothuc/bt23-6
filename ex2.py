def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if size < 1 or size > 26:
        return "Size must be between 1 and 26."

    # tạo mảng pattern ban đầu
    pattern = []
    
    for i in range(size):
        # tạo hàng
        s = "-".join(alphabet[size-1:i:-1] + alphabet[i:size])
        # căn giữa s và thêm dấu "-" ở đầu và cuối
        pattern.append(s.center(4*size - 3, "-"))
    
    # in các phần tử của mảng pattern
    print("\n".join(pattern[::-1] + pattern[1:]))

# Get user input for the size of the Rangoli
size = int(input("Enter the size of the diamond (0 < size < 27): "))
while size < 1 or size > 26:
    size = int(input("Reenter the size of the diamond (0 < size < 27): "))

# Print the Rangoli pattern
print_rangoli(size)

