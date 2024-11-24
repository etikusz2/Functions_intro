def multiply(x, y):
    """
    Multiply two numbers and return the result.

    :param x: The first number to multiply.
    :type x: int or float
    :param y: The second number to multiply.
    :type y: int or float
    :return: The product of x and y.
    :rtype: int or float
    """
    result = x * y
    return result


def is_palindrome(string):
    """
    Check if a given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards, ignoring case.

    :param string: The string to check.
    :type string: str
    :return: True if the string is a palindrome, False otherwise.
    :rtype: bool
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    """
    Check if a sentence is a palindrome, considering only alphanumeric characters.

    This function removes all non-alphanumeric characters from the sentence,
    then checks if the remaining string is a palindrome.

    :param sentence: The sentence to check.
    :type sentence: str
    :return: True if the sentence is a palindrome, False otherwise.
    :rtype: bool
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

word = input("please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))