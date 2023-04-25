s = "MCMXCIV"


def roman_to_integer(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer_value = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            integer_value -= roman[s[i]]
        else:
            integer_value += roman[s[i]]
    print(integer_value)
    return integer_value


roman_to_integer(s)
