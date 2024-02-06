def count_lengths(array):
    lengths = []
  
    for element in array:
        length = len(str(element))

        lengths.append(length)

    return lengths

input = ["abc", "apple", "orange"]
output = count_lengths(input)
print(output)

input = [12, 456, 9000]
output = count_lengths(input)
print(output)
