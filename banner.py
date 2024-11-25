def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Display a string as a banner with a customizable screen width.

    The function centers the given text within a banner surrounded by `**`.
    If the `text` is "*", it prints a row of asterisks filling the entire width.
    The `text` must fit within the available width of the banner.

    :param text: The string to display in the banner. Default is a single space.
    :type text: str
    :param screen_width: The total width of the banner, including borders. Default is 80.
    :type screen_width: int
    :raises ValueError: If the text length exceeds the available width (screen_width - 4).
    :return: None
    :rtype: None
    """
    if len(text) > screen_width -4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*")
banner_text(" Always look on the bright side of life... ")
banner_text("If life seems jolly rotten,")
banner_text(" There's something you've forgotten ")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text()
banner_text("When you/re feeling in the dumps,", 80)
banner_text("Don't be silly chumps ", 66)
banner_text("Just purse you lips and whistle - that's the thing! ", 66)
banner_text("And...always look on the bright side of life... ", 66)
banner_text("*", 66)

result = banner_text("Nothing is returned", 66)
print(result)

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort())