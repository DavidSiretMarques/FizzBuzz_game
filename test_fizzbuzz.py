"""
Tests for the fizzbuzz script: tests the conversion to fizz, buzz, fizzbuzz and the addition of new rules
(7 turns to whizz)-> testing also whizz, fizzwhizz, buzzwhizz and fizzbuzzwhizz
"""
import fizzbuzz as fb


def test_number():
    assert fb.fizz_buzz(2) == '2'


def test_fizz():
    assert fb.fizz_buzz(3) == 'Fizz'


def test_buzz():
    assert fb.fizz_buzz(5) == 'Buzz'


def test_fizzbuzz():
    assert fb.fizz_buzz(15) == 'FizzBuzz'


def test_whizz():
    assert fb.fizz_buzz(7, {7: 'Whizz'}) == 'Whizz'


def test_fizzwhizz():
    assert fb.fizz_buzz(21, {7: 'Whizz'}) == 'FizzWhizz'


def test_buzzwhizz():
    assert fb.fizz_buzz(35, {7: 'Whizz'}) == 'BuzzWhizz'


def test_fizzbuzzwhizz():
    assert fb.fizz_buzz(105, {7: 'Whizz'}) == 'FizzBuzzWhizz'
