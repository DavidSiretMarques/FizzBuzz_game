"""
Simple python script for the game of fizzbuzz.

It takes a number and if it's multiple of 3 turns it to fizz, multiple of 5 turns it to buzz, and multiple of both
(like 15) turns it to fizzbuzz.

It also supports adding new rules, like turning 7 to Whizz, adding to the rules
"""


def fizz_buzz(number: int, new_rules=None):
    rules = {3: 'Fizz', 5: 'Buzz'}
    if new_rules is not None:
        rules.update(new_rules)
    result = ''
    for key in rules:
        if number % key == 0:
            result += str(rules[key])
    if len(result) == 0:
        result = str(number)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for num in range(110):
        print(fizz_buzz(num,{7: 'Whizz'}))
