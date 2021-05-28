

def longest_similar_substring(first_array, second_array):

    # Get the lengths of two given arrays.
    first_array_length = len(first_array)
    second_array_length = len(second_array)

    longest_similar_substring_endpoint = 0
    longest_similar_substring_length = 0
  
    # 2D array to store result of two rows simultaneously.
    mat = [[0 for j in range(first_array_length)] for i in range(2)]
    
    # Indicates which of the two rows of the 2D array is the current row.
    current_row = 0
  
    # For a particular value of i and j, length[currRow][j] stores length
    # of longest similar substring in arrays first_array[0..i] and second_array[0..j].
    for i in range(0, first_array_length):
        for j in range(0, second_array_length):
            if (i == 0 or j == 0):
                mat[current_row][j] = 0
             
            elif (first_array[i - 1] == second_array[j - 1]):
                mat[current_row][j] = mat[1 - current_row][j - 1] + 1
                 
                if (mat[current_row][j] > longest_similar_substring_length):
                    longest_similar_substring_length = mat[current_row][j]
                    longest_similar_substring_endpoint = i - 1
            else:
                mat[current_row][j] = 0
  
        # Switch rows.
        current_row = 1 - current_row
  
    # In the case where there is no similar substring, return an empty array (i.e. list in python.)
    if (longest_similar_substring_length == 0):
        return tuple()
  
    # Return the longest similar substring.
    return tuple(first_array[longest_similar_substring_endpoint - longest_similar_substring_length + 1 : longest_similar_substring_endpoint + 1])

arr1 = [3, 6, 7, 4, 2, 7, 9, 1, 0, 3, 5, 6]
arr2 = [1, 5, 6, 9, 7, 4, 2, 7, 9, 9, 2, 1]
# Print output.
print(longest_similar_substring(arr1, arr2))
