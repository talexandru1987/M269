#!/usr/bin/env python3
"""
Test file for M269 19J TMA01 Question 4.

Student version 1: 1/5/19
"""

from TMA01_Q4_stack import Stack
from TMA01_Q4 import reverse_to_list, is_palindrome

failed = 0
ran = 0


def test_reverse(name, stack, expected):
    """Report if test passed or failed."""
    global ran, failed

    old_size = stack.size()
    if old_size > 0:
        old_top = stack.peek()
    else:
        old_top = None

    actual = reverse_to_list(stack)

    new_size = stack.size()
    if new_size > 0:
        new_top = stack.peek()
    else:
        new_top = None
    same = old_size == new_size and old_top == new_top

    if actual == expected and same:
        print(name, 'OK')
    elif actual == expected:
        print(name, 'FAILED: output ok but input stack changed')
        failed += 1
    else:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    ran += 1

def test_palindrome(name, argument, expected):
    """Report if test passed or failed."""
    global ran, failed

    original = argument.copy()
    actual = is_palindrome(argument)
    if argument != original:
        print(name, 'FAILED: input changed from', original, 'to', argument)
        failed += 1
    elif actual == expected:
        print(name, 'OK')
    else:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    ran += 1


print('Setting up the stack to be reversed...')
print()
# Tests are written as assertions to not clutter the screen with messages.
# You don't need to add further tests for the Stack class.
s = Stack()
assert s.isEmpty() == True
assert s.size() == 0

s.push(0)
s.push(2)
s.push(4)
s.push(6)
assert s.isEmpty() == False
assert s.size() == 4

assert s.peek() == 6
assert s.isEmpty() == False
assert s.size() == 4

top = s.pop()
assert s.isEmpty() == False
assert s.size() == 3
assert s.peek() == 4

s.push(top)
assert s.isEmpty() == False
assert s.size() == 4
assert s.peek() == 6

# Part (d)

print('Tests for reverse_to_list')
print('=========================')

test_reverse('stack 5-6-6-5', s, [0,2,4,6])
print()

# Part (e)

print('Tests for is_palindrome')
print('=======================')
test_palindrome('palindrome, even items', ['a','n','n','a'], True)
test_palindrome('palindrome, odd items', ['a','n','a'], True)
test_palindrome('not palindrome, even items', ['a','n'], False)
test_palindrome('not palindrome, odd items', ['a','a','n'], False)
test_palindrome('single item', ['a'], True)
print()

print('Summary')
print('=======')
print('Ran', ran, 'tests:', ran - failed, 'OK,', failed, 'FAILED')

if failed == 0:
    print('''You passed all our tests. Well done! Now add YOUR tests.
Think of boundary values and other special cases for the inputs and output.''')
