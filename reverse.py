def reverse_number(n):
    # Convert the number to a string and reverse it
    reversed_str = str(n)[::-1]
    
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)
    
    return reversed_num

# Example usage
number = 12345
reversed_number = reverse_number(number)
print("Original number:", number)
print("Reversed number:", reversed_number)
