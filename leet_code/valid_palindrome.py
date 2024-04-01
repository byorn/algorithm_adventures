import re
# Input: s = "abba"
# Output: true
# Explanation: "abba" is a palindrome.
def is_palindrome(str_possible_palindrome: str) -> bool:
    pattern = re.compile(r'[^a-zA-Z0-9]')
    # Use sub() function to replace all non-alphanumeric characters with the replacement character
    str_possible_palindrome = re.sub(pattern, "", str_possible_palindrome)

    middle = len(str_possible_palindrome) / 2
    for index, char in enumerate(str_possible_palindrome):
        if index <= middle:
            if char.capitalize() != str_possible_palindrome[len(str_possible_palindrome) - index - 1].capitalize():
                return False
        else:
            break
    return True


# Test
print(is_palindrome("A man, a plan, a canal: Panama"))