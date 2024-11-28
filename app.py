import re
OPERATIONS = {
    "плюс": "+",
    "минус": "-",
    "умножить на": "*",
    "разделить на": "/"
}
WORDS_TO_NUMS = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6,
    "семь": 7, "восемь": 8, "девять": 9, "десять": 10, "одиннадцать": 11, "двенадцать": 12,
    "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15, "шестнадцать": 16,
    "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19, "двадцать": 20,
    "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70,
    "восемьдесят": 80, "девяносто": 90, "сто": 100
}
NUMS_TO_WORDS = {v: k for k, v in WORDS_TO_NUMS.items()}
def number_to_words(number):
    '''The function converts an integer value to a text format.

    Args:
        number (int): integer response.

    Returns:
        ... (str): a list connected to a string using spaces.
    '''

    if number < 0:
        return "минус " + number_to_words(-number)
    if number in NUMS_TO_WORDS:
        return NUMS_TO_WORDS[number]
    parts = []
    if number >= 20:
        tens = (number // 10) * 10
        parts.append(NUMS_TO_WORDS[tens])
        number %= 10
    if number > 0:
        parts.append(NUMS_TO_WORDS[number])
    return " ".join(parts)

def words_to_number(text):
    '''Converts a number written in text format to an integer value.

    Args:
        text (str): a string with a number written in text format.

    Returns:
        total (int): the result of the number translation.
    '''

    parts = text.split()
    total = 0
    for part in parts:
        if part in WORDS_TO_NUMS:
            total += WORDS_TO_NUMS[part]
    return total

def text_to_math(expression):
    '''Converts a text expression into a mathematical form.

    Args:
        expression (str): an easy-to-format string with a text record of an arithmetic operation.

    Returns:
        ... (str): a list with formatted text combined into a string.
    '''

    for word, symbol in OPERATIONS.items():
        expression = expression.replace(word, symbol)
    words = expression.split()
    new_expression = []
    i = 0
    while i < len(words):
        if words[i] in WORDS_TO_NUMS:
            if i + 1 < len(words) and words[i + 1] in WORDS_TO_NUMS:
                number = words_to_number(f"{words[i]} {words[i + 1]}")
                new_expression.append(str(number))
                i += 2
            else:
                new_expression.append(str(WORDS_TO_NUMS[words[i]]))
                i += 1
        else:
            new_expression.append(words[i])
            i += 1
    return " ".join(new_expression)

def calculate(expression):
    '''Сounts the values of an arithmetic operation.

    Args:
        expression (str): an easy-to-format string with a text record of an arithmetic operation.

    Returns:
        result (str): the result of executing the eval function.
        e (Exception): calculation error.
    '''

    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка вычисления: {e}"

def main():
    '''The main function that is called when the code is run.

    The function works as a procedure, it does not accept or return values.
    '''

    print("Для выхода введите 'выход'.")

    while True:
        text_expression = input("Ваше выражение: ")

        if text_expression.lower() == "выход":
            print("До свидания!")
            break
        text_expression = re.sub(r"(умножить на|разделить на)", r" \1 ", text_expression)
        math_expression = text_to_math(text_expression)
        result = calculate(math_expression)
        if isinstance(result, (int, float)):
            result_text = number_to_words(int(result)) if result == int(result) else str(result)
            print(f"Результат: {result_text}")
        else:
            print(f"Результат: {result}")
if __name__ == "__main__":
    main()

