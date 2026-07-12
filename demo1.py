# Reverse a string
def reverse_string(s):
    return s[::-1]

# Reverse a number
def reverse_number(n):
    return int(str(n)[::-1])

# Reverse a list
def reverse_list(lst):
    return lst[::-1]

# Demo
if __name__ == "__main__":
    text = "Hello World"
    number = 12345
    items = [1, 2, 3, 4, 5]

    print("Original text:", text)
    print("Reversed text:", reverse_string(text))

    print("Original number:", number)
    print("Reversed number:", reverse_number(number))

    print("Original list:", items)
    print("Reversed list:", reverse_list(items))
