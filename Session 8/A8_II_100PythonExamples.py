## 100 Python scripts & functions

# write a python function to find and return nth element in a user provided list

def find_nth_element(the_list, n):
  nth_elem = the_list[n]    
  return nth_elem

# write a python function to sort an array using binary search algorithm

def createSorted(a: list, n: int): 
  
    # Auxiliary Array 
    b = [] 
    for j in range(n): 
  
        # if b is empty any element can be at 
        # first place 
        if len(b) == 0: 
            b.append(a[j]) 
        else: 
  
            # Perform Binary Search to find the correct 
            # position of current element in the 
            # new array 
            start = 0
            end = len(b) - 1
  
            # let the element should be at first index 
            pos = 0
            while start <= end: 
                mid = start + (end - start) // 2
  
                # if a[j] is already present in the new array 
                if b[mid] == a[j]: 
  
                    # add a[j] at mid+1. you can add it at mid 
                    b.insert(max(0, mid + 1), a[j]) 
                    break
  
                # if a[j] is lesser than b[mid] go right side 
                elif b[mid] > a[j]: 
  
                    # means pos should be between start and mid-1 
                    pos = end = mid - 1
                else: 
  
                    # else pos should be between mid+1 and end 
                    pos = start = mid + 1
  
                # if a[j] is the largest push it at last 
                if start > end: 
                    pos = start 
                    b.insert(max(0, pos), a[j]) 
  
                    # here max(0, pos) is used because sometimes 
                    # pos can be negative as smallest duplicates 
                    # can be present in the array 
                    break
  
    # Print the new generated sorted array 
    for i in range(n): 
        print(b[i], end=" ")

# write a python program to seperate each character in a string with '<space>'

string = "abcdef"
spaced_string = ""

for i in string:
    spaced_string += i + " "

print(spaced_string)

# write a python function to Calculate and return mean of user provided list of numbers

def get_mean(the_list):
  return sum(the_list)/len(the_list)

# write a python function to calculate and return standard deviation of user provided list of numbers 

def get_std(the_list):
  import math
  ave=sum(the_list)/len(the_list)
  diff=[x-ave for x in the_list]
  squares=[x**2 for x in diff]
  variance=sum(squares)/len(the_list)
  std =math.sqrt(variance)
  return std

# write a python function to Find and return min in a user provided list of numbers

def get_min(the_list):
  return min(the_list)

# write a python function to Join two user provided lists and return it

def join_lists(list1,list2):
  return list1+list2

# write a python function to empty an user provided list of items

def empty_this_list(the_list):
  the_list.clear()
  return the_list

# write a python function to remove nth item in a user provided list of items 

def remove_nth_item(the_list,n):
  del(the_list[n-1])
  return the_list

# write a python function to increase all items in user provided list by n

def increase_by_n(the_list,n):
  the_list=[x+n for x in the_list]
  return the_list

# write a python function to decrease all items in user provided list by n

def decrease_by_n(the_list,n):
  the_list=[x-n for x in the_list]
  return the_list

# write a python function to divide all items in user provided list by n

def divide_by_n(the_list,n):
  the_list=[x/n for x in the_list]
  return the_list

# write a python function to multiply all items in user provided list by n

def multiply_by_n(the_list,n):
  the_list=[x*n for x in the_list]
  return the_list

# write a python function to Find and return max in a user provider list of numbers

def get_max(the_list):
  return max(the_list)

# write a python function to Check if an item exists in user provided list

def check_item_exists(the_list,the_item):
  return the_item in the_list

# Write a Python function to Return a copy of a user provided list

def get_copy(the_list):
  return the_list.copy()

# Write a Python function to Extract even numbers from user provoded list 
def get_even(the_list):
  the_new_list=[x for x in the_list if x%2==0 ]
  return the_new_list

# Write a Python function to Extract odd numbers from user provoded list 
def get_odd(the_list):
  the_new_list=[x for x in the_list if x%2!=0 ]
  return the_new_list

# Write a python function to create and return a tuple from single user provided item
def get_tuple(the_item):
  return (the_item,)

# Write a python function to remove duplicates from a list
def remove_duplicates(the_list):
  return list(set(the_list))

# Write a python function to Check whether two user provided sets have an intersection or not
def has_intersection(set1,set2):
  return not (set1.isdisjoint(set2))

# write a python function to check and return if set A is subset of B
def is_subset(A,B):
  return A.issubset(B)


# write a python function to return a list of common items from two user provided lists 
def get_common_items(list1,list2):
  return list(set(list1).intersection(set(list2))) 

# Write a python function to combine and return only unique items from two user provided lists 
def get_combined_unique(list1,list2):
  return list(set(list1).union(set(list2))) 

# write a python program to check if word exists a sentence

def does_word_exist(sentnc,word):
  return word in sentnc 

# write a python program to print out number of non-space ( or non-whitespace) characters in sentence 

def get_char_count(sentnc):
  sentnc=sentnc.strip()
  sentnc1=sentnc.split(' ')
  s=sum([len(x) for x in sentnc1])

  return s
 

# write a python program to concatenate two strings 
sent1='This is string1'
sent2='This is string2'
concat_string=sent1+sent2
print(concat_string)

# write a python program to Replace a substring
str1='This is a about cats and dogs and monkeys'
str2='monkeys'
str3='donkeys'
str4=str1.replace(str2,str3)
print(str4)

# Write a python function to capitalize
from string import ascii_lowercase, ascii_uppercase


def capitalize(sentence: str) -> str:
    """
    This function will capitalize the first letter of a sentence or a word
    >>> capitalize("hello world")
    'Hello world'
    >>> capitalize("123 hello world")
    '123 hello world'
    >>> capitalize(" hello world")
    ' hello world'
    >>> capitalize("a")
    'A'
    >>> capitalize("")
    ''
    """
    if not sentence:
        return ""
    lower_to_upper = {lc: uc for lc, uc in zip(ascii_lowercase, ascii_uppercase)}
    return lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:]


# write a python program to Add element to a dictionary

dictionary = {"item1": "value1"}
dictionary["item2"] = "value2"


# write a python program to remove an element to a dictionary

dictionary = {'item1': 'value1', 'item2': 'value2'}
dictionary.pop("item2")


# Join two dictionaries

dict_a = {"item1": "value1"}
dict_b = {"item_2": "value2"}

dict_c = dict(dict_a, **dict_b)


# write a python function to find nth root of a number

import math 
import random 

def nthRoot(A,N): 
  
    # initially guessing a random number between 
    # 0 and 9 
    xPre = random.randint(1,101) % 10
   
    #  smaller eps, denotes more accuracy 
    eps = 0.001
   
    # initializing difference between two 
    # roots by INT_MAX 
    delX = 2147483647
   
    #  xK denotes current value of x 
    xK=0.0
   
    #  loop untill we reach desired accuracy 
    while (delX > eps): 
  
        # calculating current value from previous 
        # value by newton's method 
        xK = ((N - 1.0) * xPre +
              A/pow(xPre, N-1)) /N 
        delX = abs(xK - xPre) 
        xPre = xK; 
          
    return xK


# write a python program to find area of a rectangle given sides

l = 4
b = 5

area = l*b

print(area)


# write a python program to return velocity given displacement(m) and time(s)

displacement = 50
time = 34

velocity = displacement/time

print(velocity)


# write a python program to return accelaration given velocity(m/s) and time(s)

velocity = 24
time = 5

acceleration = velocity/time

print(acceleration)


# write a python function to return if one number is greater than other

def greater_than(a,b):
    if a>b:
        print(True)
    else:
        print(False)


# write a python program to print absolute value of a number

n = 34

print(abs(n))


# write a python function to convert feets to meters

def feets_to_meters(feets):
    
    meters = 0.3048 * feets
    
    return meters


# write a python function to convert inches to centimeters

def inches_to_centimeters(inches):
    
    centimeters = 2.54 * inches
    
    return centimeters


# write a python function to convert miles to kilometers

def miles_to_kilometers(miles):
    
    kilometers = 1.60934 * miles
    
    return kilometers


# write a python function to convert celcius to farenheit

def celcius_to_farenheit(celcius):
    
    farenheit = (celcius * 9/5) + 32
    
    return farenheit


# write a python program insert number at specified position n of list

list1 = [ 1, 2, 3, 4, 5, 6, 7 ]  
  
# insert 10 at 4th index  
list1.insert(4, 10)  
print(list1)


# write a python program to reverse a list

list1 = [1,2,3,4,5,6,7]

print(list1[::-1])


# write a python function if a and b are equal

def a_equals_b(a, b):
    
    if a == b:
        print(True)
    else:
        print(False)


# write a python program to display current time

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)


# write a python function to check if a year is leap year or not

def is_leap_year(year):
    
    if (year % 4) == 0:
        print(True)
    else:
        print(False)

# write a python function to print volume of a sphere given the radius

def sphere_volume(radius):
    
    volume = 4/3 * (math.pi * radius ** 3)
    
    return volume

# write a python function to return volume of a cuboid given lenght, breadth and height

def cuboid_volume(length, breadth, height):

    volume = length * breadth * height

    return volume

# write a python function to check if a traingle is a right-angled triangle given sides a,b and c

def is_right_angled_traingle(a, b, c):
    
    x, y, z = sorted([a,b,c])
    
    if x**2+y**2==z**2:
        print(True)
    else:
        print(False)

# write a python function to print the type of a triangle by sides given sides a,b and c

def type_of_triangle(a, b, c):
    
    if a==b==c:
        print("Equilateral Triangle")
    elif a==b or b==c or a==c:
        print("Isosceles Trianfle")
    else:
        print("Scalene Triangle")


# write a python program that calculates weight of a person in moon given the person's weight on earth


weight_on_earth = 65

weight_on_moon = 0.165 * weight_on_earth

print(weight_on_moon)


# write a python program that calculates the time taken for the light(in seconds) to reach an object given its distance(km) from sun

distance_from_sun = 1600000
light_speed = 300000 # km/s

time_taken = distance_from_sun / light_speed

print(time_taken)


# write a python program to Calculate the time taken for a stone(in seconds) to reach the ground given the height(m) it is dropped from.

import math

dropped_from = 9000
initial_velocity = 0
acceleration_due_to_gravity = 9.8

time_taken = math.sqrt(dropped_from / (acceleration_due_to_gravity / 2)) # from equations of motions

print(time_taken)


# write a python function to return simple interest given p, n and r

def simple_interest(p, n, r):

    interest = (p*n*r) / 100
    
    return interest

# write a python funtion to return compound interest given principle, time and rate

def compound_interest(principle, time, rate):

    Amount = principle * (pow((1 + rate / 100), time)) 
    CI = Amount - principle
    
    return CI

# write a python function to return Return On Investment given first value, last value and number of years

def roi(first_value, last_value, time):
    
    return ((last_value/first_value)**(1/time)-1) * 100


# write a python program to Calculate the number of bricks required to construct a wall given brick and wall dimensions

import math

brick_length = 9
brick_breadth = 4
brick_height = 3

wall_length = 120
wall_breadth = 12
wall_height = 100

wall_volume = wall_length * wall_breadth * wall_height
brick_volume = brick_length * brick_breadth * brick_height

required_bricks = wall_volume / brick_volume

print(math.floor(required_bricks))


# write a python program to Calculate the amount of water harvested in an area due to rain given the surface area and the rainfall.

surface_area = 100
rainfall = 3

harvested_water = 3 * 100

print(harvested_water)


# write a python program to Calculate the time left for sunset(hours) given the angle of sun(degrees) from the horizon


degree_rate = 0.067  # hours taken per degree movement
sun_angle = 45

time_left_for_sunset = (180 - sun_angle) * degree_rate

print(time_left_for_sunset)


# write a python function to Calculate the distance travelled by a wheel given its radius, rpm and time(minutes)

import math

def distance_travelled(radius, rpm, time):

    perimeter = 2 * math.pi * radius
    
    distance_travelled = perimeter * rpm * time
    
    return distance_travelled


# write a python program to check if a fighter jet is super sonic or not

fighter_jet_speed = 300 # meters/sec
speed_of_sound = 343 # meters/sec

if fighter_jet_speed > speed_of_sound:
    print(True)
else:
    print(False)


# write a program to Calculate how old a fossil is, given its Carbon 14 percentage

import math

c14_percent = 0.2
c14_haflife = 5730

carbon_date = (math.log(c14_percent) / (-0.693)) * c14_haflife


# Write a python function to check anagrams
def check_anagrams(first_str: str, second_str: str) -> bool:
    """
    Two strings are anagrams if they are made of the same letters
    arranged differently (ignoring the case).
    >>> check_anagrams('Silent', 'Listen')
    True
    >>> check_anagrams('This is a string', 'Is this a string')
    True
    >>> check_anagrams('This is    a      string', 'Is     this a string')
    True
    >>> check_anagrams('There', 'Their')
    False
    """
    return (
        "".join(sorted(first_str.lower())).strip()
        == "".join(sorted(second_str.lower())).strip()
    )


# Wite a python function to check pangram
def check_pangram(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    """
    A Pangram String contains all the alphabets at least once.
    >>> check_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> check_pangram("Waltz, bad nymph, for quick jigs vex.")
    True
    >>> check_pangram("Jived fox nymph grabs quick waltz.")
    True
    >>> check_pangram("My name is Unknown")
    False
    >>> check_pangram("The quick brown fox jumps over the la_y dog")
    False
    >>> check_pangram()
    True
    """
    frequency = set()
    input_str = input_str.replace(
        " ", ""
    )  # Replacing all the Whitespaces in our sentence
    for alpha in input_str:
        if "a" <= alpha.lower() <= "z":
            frequency.add(alpha.lower())

    return True if len(frequency) == 26 else False





# Write a python function to check palindrome
def is_palindrome_check(s: str) -> bool:
    """
    Determine whether the string is palindrome
    :param s:
    :return: Boolean
    >>> is_palindrome("a man a plan a canal panama".replace(" ", ""))
    True
    >>> is_palindrome("Hello")
    False
    >>> is_palindrome("Able was I ere I saw Elba")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("Mr. Owl ate my metal worm?")
    True
    """
    # Since Punctuation, capitalization, and spaces are usually ignored while checking
    # Palindrome,  we first remove them from our string.
    s = "".join([character for character in s.lower() if character.isalnum()])
    return s == s[::-1]

# Wite a python function to check word occurences

from collections import defaultdict


def word_occurence(sentence: str) -> dict:
    """
    >>> from collections import Counter
    >>> SENTENCE = "a b A b c b d b d e f e g e h e i e j e 0"
    >>> occurence_dict = word_occurence(SENTENCE)
    >>> all(occurence_dict[word] == count for word, count
    ...     in Counter(SENTENCE.split()).items())
    True
    >>> dict(word_occurence("Two  spaces"))
    {'Two': 1, 'spaces': 1}
    """
    occurrence = defaultdict(int)
    # Creating a dictionary containing count of each word
    for word in sentence.split():
        occurrence[word] += 1
    return occurrence

# Write a python function for swap case


def swap_case(sentence: str) -> str:
    """
    This function will convert all lowercase letters to uppercase letters
    and vice versa.
    >>> swap_case('Algorithm.Python@89')
    'aLGORITHM.pYTHON@89'
    """
    new_string = ""
    for char in sentence:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            new_string += char

    return new_string

# Write a python function to reverse str

def reverse_words(input_str: str) -> str:
    """
    Reverses words in a given string
    >>> reverse_words("I love Python")
    'Python love I'
    >>> reverse_words("I     Love          Python")
    'Python Love I'
    """
    return " ".join(input_str.split()[::-1])

# Write a python function to reverse letters
def reverse_letters(input_str: str) -> str:
    """
    Reverses letters in a given string without adjusting the position of the words
    >>> reverse_letters('The cat in the hat')
    'ehT tac ni eht tah'
    >>> reverse_letters('The quick brown fox jumped over the lazy dog.')
    'ehT kciuq nworb xof depmuj revo eht yzal .god'
    >>> reverse_letters('Is this true?')
    'sI siht ?eurt'
    >>> reverse_letters("I   love       Python")
    'I evol nohtyP'
    """
    return " ".join([word[::-1] for word in input_str.split()])

# Write a python function to remove duplicates in sting
def remove_duplicates_str(sentence: str) -> str:
    """
    Remove duplicates from sentence
    >>> remove_duplicates("Python is great and Java is also great")
    'Java Python also and great is'
    >>> remove_duplicates("Python   is      great and Java is also great")
    'Java Python also and great is'
    """
    return " ".join(sorted(set(sentence.split())))

# write a python function for navie pattern search
def naive_pattern_search(s: str, pattern: str) -> list:
    """
    >>> naive_pattern_search("ABAAABCDBBABCDDEBCABC", "ABC")
    [4, 10, 18]
    >>> naive_pattern_search("ABC", "ABAAABCDBBABCDDEBCABC")
    []
    >>> naive_pattern_search("", "ABC")
    []
    >>> naive_pattern_search("TEST", "TEST")
    [0]
    >>> naive_pattern_search("ABCDEGFTEST", "TEST")
    [7]
    """
    pat_len = len(pattern)
    position = []
    for i in range(len(s) - pat_len + 1):
        match_found = True
        for j in range(pat_len):
            if s[i + j] != pattern[j]:
                match_found = False
                break
        if match_found:
            position.append(i)
    return position

# Write a code for calculating the most cost-efficient sequence for converting one string into another.
from typing import List, Tuple

"""
Algorithm for calculating the most cost-efficient sequence for converting one string
into another.
The only allowed operations are
--- Cost to copy a character is copy_cost
--- Cost to replace a character is replace_cost
--- Cost to delete a character is delete_cost
--- Cost to insert a character is insert_cost
"""


def compute_transform_tables(
    source_string: str,
    destination_string: str,
    copy_cost: int,
    replace_cost: int,
    delete_cost: int,
    insert_cost: int,
) -> Tuple[List[int], List[str]]:
    source_seq = list(source_string)
    destination_seq = list(destination_string)
    len_source_seq = len(source_seq)
    len_destination_seq = len(destination_seq)

    costs = [
        [0 for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)
    ]
    ops = [
        [0 for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)
    ]

    for i in range(1, len_source_seq + 1):
        costs[i][0] = i * delete_cost
        ops[i][0] = "D%c" % source_seq[i - 1]

    for i in range(1, len_destination_seq + 1):
        costs[0][i] = i * insert_cost
        ops[0][i] = "I%c" % destination_seq[i - 1]

    for i in range(1, len_source_seq + 1):
        for j in range(1, len_destination_seq + 1):
            if source_seq[i - 1] == destination_seq[j - 1]:
                costs[i][j] = costs[i - 1][j - 1] + copy_cost
                ops[i][j] = "C%c" % source_seq[i - 1]
            else:
                costs[i][j] = costs[i - 1][j - 1] + replace_cost
                ops[i][j] = "R%c" % source_seq[i - 1] + str(destination_seq[j - 1])

            if costs[i - 1][j] + delete_cost < costs[i][j]:
                costs[i][j] = costs[i - 1][j] + delete_cost
                ops[i][j] = "D%c" % source_seq[i - 1]

            if costs[i][j - 1] + insert_cost < costs[i][j]:
                costs[i][j] = costs[i][j - 1] + insert_cost
                ops[i][j] = "I%c" % destination_seq[j - 1]

    return costs, ops


def assemble_transformation(ops: List[str], i: int, j: int) -> List[str]:
    if i == 0 and j == 0:
        return []
    else:
        if ops[i][j][0] == "C" or ops[i][j][0] == "R":
            seq = assemble_transformation(ops, i - 1, j - 1)
            seq.append(ops[i][j])
            return seq
        elif ops[i][j][0] == "D":
            seq = assemble_transformation(ops, i - 1, j)
            seq.append(ops[i][j])
            return seq
        else:
            seq = assemble_transformation(ops, i, j - 1)
            seq.append(ops[i][j])
            return seq


if __name__ == "__main__":
    _, operations = compute_transform_tables("Python", "Algorithms", -1, 1, 2, 2)

    m = len(operations)
    n = len(operations[0])
    sequence = assemble_transformation(operations, m - 1, n - 1)

    string = list("Python")
    i = 0
    cost = 0

    with open("min_cost.txt", "w") as file:
        for op in sequence:
            print("".join(string))

            if op[0] == "C":
                file.write("%-16s" % "Copy %c" % op[1])
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost -= 1
            elif op[0] == "R":
                string[i] = op[2]

                file.write("%-16s" % ("Replace %c" % op[1] + " with " + str(op[2])))
                file.write("\t\t" + "".join(string))
                file.write("\r\n")

                cost += 1
            elif op[0] == "D":
                string.pop(i)

                file.write("%-16s" % "Delete %c" % op[1])
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost += 2
            else:
                string.insert(i, op[1])

                file.write("%-16s" % "Insert %c" % op[1])
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost += 2

            i += 1

        print("".join(string))
        print("Cost: ", cost)

        file.write("\r\nMinimum cost: " + str(cost))

# Write a python function to convert the entire string to lowecase letters
def lower(word: str) -> str:
    """
    Will convert the entire string to lowecase letters
    >>> lower("wow")
    'wow'
    >>> lower("HellZo")
    'hellzo'
    >>> lower("WHAT")
    'what'
    >>> lower("wh[]32")
    'wh[]32'
    >>> lower("whAT")
    'what'
    """

    # converting to ascii value int value and checking to see if char is a capital
    # letter if it is a capital letter it is getting shift by 32 which makes it a lower
    # case letter
    return "".join(chr(ord(char) + 32) if "A" <= char <= "Z" else char for char in word)

# Write a python function to calculate levenstein distance

def levenshtein_distance(first_word: str, second_word: str) -> int:
    """Implementation of the levenshtein distance in Python.
    :param first_word: the first word to measure the difference.
    :param second_word: the second word to measure the difference.
    :return: the levenshtein distance between the two words.
    Examples:
    >>> levenshtein_distance("planet", "planetary")
    3
    >>> levenshtein_distance("", "test")
    4
    >>> levenshtein_distance("book", "back")
    2
    >>> levenshtein_distance("book", "book")
    0
    >>> levenshtein_distance("test", "")
    4
    >>> levenshtein_distance("", "")
    0
    >>> levenshtein_distance("orchestration", "container")
    10
    """
    # The longer word should come first
    if len(first_word) < len(second_word):
        return levenshtein_distance(second_word, first_word)

    if len(second_word) == 0:
        return len(first_word)

    previous_row = range(len(second_word) + 1)

    for i, c1 in enumerate(first_word):

        current_row = [i + 1]

        for j, c2 in enumerate(second_word):

            # Calculate insertions, deletions and substitutions
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            # Get the minimum to append to the current row
            current_row.append(min(insertions, deletions, substitutions))

        # Store the previous row
        previous_row = current_row

    # Returns the last element (distance)
    return previous_row[-1]

# Write a python function to check palindrome for list
def is_palindrome_List(head):
    if not head:
        return True
    # split the list to two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None  # Don't forget here! But forget still works!
    # reverse the second part
    node = None
    while second:
        nxt = second.next
        second.next = node
        node = second
        second = nxt
    # compare two parts
    # second part has the same or one less node
    while node:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True

# Write a python function to check palindrome for dict
def is_palindrome_dict(head):
    if not head or not head.next:
        return True
    d = {}
    pos = 0
    while head:
        if head.val in d.keys():
            d[head.val].append(pos)
        else:
            d[head.val] = [pos]
        head = head.next
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in d.values():
        if len(v) % 2 != 0:
            middle += 1
        else:
            step = 0
            for i in range(0, len(v)):
                if v[i] + v[len(v) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True

# Write a python function to calculate bisection
from typing import Callable


def bisection(function: Callable[[float], float], a: float, b: float) -> float:
    """
    finds where function becomes 0 in [a,b] using bolzano
    >>> bisection(lambda x: x ** 3 - 1, -5, 5)
    1.0000000149011612
    >>> bisection(lambda x: x ** 3 - 1, 2, 1000)
    Traceback (most recent call last):
    ...
    ValueError: could not find root in given interval.
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 0, 2)
    1.0
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 2, 4)
    3.0
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 4, 1000)
    Traceback (most recent call last):
    ...
    ValueError: could not find root in given interval.
    """
    start: float = a
    end: float = b
    if function(a) == 0:  # one of the a or b is a root for the function
        return a
    elif function(b) == 0:
        return b
    elif (
        function(a) * function(b) > 0
    ):  # if none of these are root and they are both positive or negative,
        # then this algorithm can't find the root
        raise ValueError("could not find root in given interval.")
    else:
        mid: float = start + (end - start) / 2.0
        while abs(start - mid) > 10 ** -7:  # until precisely equals to 10^-7
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end - start) / 2.0
        return mid

# Write a python function to Implementing Secant method in Python


from math import exp


def f(x):
    """
    >>> f(5)
    39.98652410600183
    """
    return 8 * x - 2 * exp(-x)


def SecantMethod(lower_bound, upper_bound, repeats):
    """
    >>> SecantMethod(1, 3, 2)
    0.2139409276214589
    """
    x0 = lower_bound
    x1 = upper_bound
    for i in range(0, repeats):
        x0, x1 = x1, x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    return x1


print(f"The solution is: {SecantMethod(1, 3, 2)}")

# Write a python function to calculate intersection

import math
from typing import Callable


def intersection(function: Callable[[float], float], x0: float, x1: float) -> float:
    """
    function is the f we want to find its root
    x0 and x1 are two random starting points
    >>> intersection(lambda x: x ** 3 - 1, -5, 5)
    0.9999999999954654
    >>> intersection(lambda x: x ** 3 - 1, 5, 5)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: float division by zero, could not find root
    >>> intersection(lambda x: x ** 3 - 1, 100, 200)
    1.0000000000003888
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 0, 2)
    0.9999999998088019
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 2, 4)
    2.9999999998088023
    >>> intersection(lambda x: x ** 2 - 4 * x + 3, 4, 1000)
    3.0000000001786042
    >>> intersection(math.sin, -math.pi, math.pi)
    0.0
    >>> intersection(math.cos, -math.pi, math.pi)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: float division by zero, could not find root
    """
    x_n: float = x0
    x_n1: float = x1
    while True:
        if x_n == x_n1 or function(x_n1) == function(x_n):
            raise ZeroDivisionError("float division by zero, could not find root")
        x_n2: float = x_n1 - (
            function(x_n1) / ((function(x_n1) - function(x_n)) / (x_n1 - x_n))
        )
        if abs(x_n2 - x_n1) < 10 ** -5:
            return x_n2
        x_n = x_n1
        x_n1 = x_n2

# Write a python function for bitwise operator example
def binary_or(a: int, b: int):
    """
    Take in 2 integers, convert them to binary, and return a binary number that is the
    result of a binary or operation on the integers provided.
    >>> binary_or(25, 32)
    '0b111001'
    >>> binary_or(37, 50)
    '0b110111'
    >>> binary_or(21, 30)
    '0b11111'
    >>> binary_or(58, 73)
    '0b1111011'
    >>> binary_or(0, 255)
    '0b11111111'
    >>> binary_or(0, 256)
    '0b100000000'
    >>> binary_or(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: the value of both input must be positive
    >>> binary_or(0, 1.1)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> binary_or("0", "1")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0 or b < 0:
        raise ValueError("the value of both input must be positive")
    a_binary = str(bin(a))[2:]  # remove the leading "0b"
    b_binary = str(bin(b))[2:]
    max_len = max(len(a_binary), len(b_binary))
    return "0b" + "".join(
        str(int("1" in (char_a, char_b)))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )

# Write a python function for cipher_text
from string import ascii_uppercase

dict1 = {char: i for i, char in enumerate(ascii_uppercase)}
dict2 = {i: char for i, char in enumerate(ascii_uppercase)}


# This function generates the key in
# a cyclic manner until it's length isn't
# equal to the length of original text
def generate_key(message: str, key: str) -> str:
    """
    >>> generate_key("THE GERMAN ATTACK","SECRET")
    'SECRETSECRETSECRE'
    """
    x = len(message)
    i = 0
    while True:
        if x == i:
            i = 0
        if len(key) == len(message):
            break
        key += key[i]
        i += 1
    return key


# This function returns the encrypted text
# generated with the help of the key
def cipher_text(message: str, key_new: str) -> str:
    """
    >>> cipher_text("THE GERMAN ATTACK","SECRETSECRETSECRE")
    'BDC PAYUWL JPAIYI'
    """
    cipher_text = ""
    i = 0
    for letter in message:
        if letter == " ":
            cipher_text += " "
        else:
            x = (dict1[letter] - dict1[key_new[i]]) % 26
            i += 1
            cipher_text += dict2[x]
    return cipher_text


# This function decrypts the encrypted text
# and returns the original text
def original_text(cipher_text: str, key_new: str) -> str:
    """
    >>> original_text("BDC PAYUWL JPAIYI","SECRETSECRETSECRE")
    'THE GERMAN ATTACK'
    """
    or_txt = ""
    i = 0
    for letter in cipher_text:
        if letter == " ":
            or_txt += " "
        else:
            x = (dict1[letter] + dict1[key_new[i]] + 26) % 26
            i += 1
            or_txt += dict2[x]
    return or_txt


def main():
    message = "THE GERMAN ATTACK"
    key = "SECRET"
    key_new = generate_key(message, key)
    s = cipher_text(message, key_new)
    print(f"Encrypted Text = {s}")
    print(f"Original Text = {original_text(s, key_new)}")

main()

# Write a python function for base64 encoding and decoding
import base64


def base64_enc_dec():
    inp = input("->")
    encoded = inp.encode("utf-8")  # encoded the input (we need a bytes like object)
    a85encoded = base64.a85encode(encoded)  # a85encoded the encoded string
    print(a85encoded)
    print(base64.a85decode(a85encoded).decode("utf-8"))  # decoded it

main()

# Write a python function for base32 encoding
import base64


def base32_enc():
    inp = input("->")
    encoded = inp.encode("utf-8")  # encoded the input (we need a bytes like object)
    b32encoded = base64.b32encode(encoded)  # b32encoded the encoded string
    print(b32encoded)

# Write a python function for base16 encoding

import base64


def encode_to_b16(inp: str) -> bytes:
    """
    Encodes a given utf-8 string into base-16.
    >>> encode_to_b16('Hello World!')
    b'48656C6C6F20576F726C6421'
    >>> encode_to_b16('HELLO WORLD!')
    b'48454C4C4F20574F524C4421'
    >>> encode_to_b16('')
    b''
    """
    encoded = inp.encode("utf-8")  # encoded the input (we need a bytes like object)
    b16encoded = base64.b16encode(encoded)  # b16encoded the encoded string
    return b16encoded

# Write a python function RSA prime factor algorithm.

"""
An RSA prime factor algorithm.
The program can efficiently factor RSA prime number given the private key d and
public key e.
Source: on page 3 of https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf
More readable source: https://www.di-mgt.com.au/rsa_factorize_n.html
large number can take minutes to factor, therefore are not included in doctest.
"""
from __future__ import annotations

import math
import random


def rsafactor(d: int, e: int, N: int) -> [int]:
    """
    This function returns the factors of N, where p*q=N
      Return: [p, q]
    We call N the RSA modulus, e the encryption exponent, and d the decryption exponent.
    The pair (N, e) is the public key. As its name suggests, it is public and is used to
        encrypt messages.
    The pair (N, d) is the secret key or private key and is known only to the recipient
        of encrypted messages.
    >>> rsafactor(3, 16971, 25777)
    [149, 173]
    >>> rsafactor(7331, 11, 27233)
    [113, 241]
    >>> rsafactor(4021, 13, 17711)
    [89, 199]
    """
    k = d * e - 1
    p = 0
    q = 0
    while p == 0:
        g = random.randint(2, N - 1)
        t = k
        while True:
            if t % 2 == 0:
                t = t // 2
                x = (g ** t) % N
                y = math.gcd(x - 1, N)
                if x > 1 and y > 1:
                    p = y
                    q = N // y
                    break  # find the correct factors
            else:
                break  # t is not divisible by 2, break and choose another g
    return sorted([p, q])

# Write a Python program to implement Morse Code Translator

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "&": ".-...",
    "@": ".--.-.",
    ":": "---...",
    ",": "--..--",
    ".": ".-.-.-",
    "'": ".----.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    # Exclamation mark is not in ITU-R recommendation
    "!": "-.-.--",
}


def encrypt(message: str) -> str:
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += "/ "

    # Remove trailing space added on line 64
    return cipher[:-1]


def decrypt(message: str) -> str:
    decipher = ""
    letters = message.split(" ")
    for letter in letters:
        if letter != "/":
            decipher += list(MORSE_CODE_DICT.keys())[
                list(MORSE_CODE_DICT.values()).index(letter)
            ]
        else:
            decipher += " "

    return decipher


# def main():
#     message = "Morse code here"
#     result = encrypt(message.upper())
#     print(result)

#     message = result
#     result = decrypt(message)
#     print(result)


if __name__ == "__main__":
    main()

# Write a Python program to implement mono_alphabetic_ciphers

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def translate_message(key, message, mode):
    """
    >>> translate_message("QWERTYUIOPASDFGHJKLZXCVBNM","Hello World","encrypt")
    'Pcssi Bidsm'
    """
    chars_a = LETTERS if mode == "decrypt" else key
    chars_b = key if mode == "decrypt" else LETTERS
    translated = ""
    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in chars_a:
            # encrypt/decrypt the symbol
            sym_index = chars_a.find(symbol.upper())
            if symbol.isupper():
                translated += chars_b[sym_index].upper()
            else:
                translated += chars_b[sym_index].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
    return translated


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "Hello World")
    'Pcssi Bidsm'
    """
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "Hello World")
    'Itssg Vgksr'
    """
    return translate_message(key, message, "decrypt")


# def main():
#     message = "Hello World"
#     key = "QWERTYUIOPASDFGHJKLZXCVBNM"
#     mode = "decrypt"  # set to 'encrypt' or 'decrypt'

#     if mode == "encrypt":
#         translated = encrypt_message(key, message)
#     elif mode == "decrypt":
#         translated = decrypt_message(key, message)
#     print(f"Using the key {key}, the {mode}ed message is: {translated}")

# main()

# Write a Python program to implement mixed_keyword_cypher
def mixed_keyword(key: str = "college", pt: str = "UNIVERSITY") -> str:
    """
    For key:hello
    H E L O
    A B C D
    F G I J
    K M N P
    Q R S T
    U V W X
    Y Z
    and map vertically
    >>> mixed_keyword("college", "UNIVERSITY")  # doctest: +NORMALIZE_WHITESPACE
    {'A': 'C', 'B': 'A', 'C': 'I', 'D': 'P', 'E': 'U', 'F': 'Z', 'G': 'O', 'H': 'B',
     'I': 'J', 'J': 'Q', 'K': 'V', 'L': 'L', 'M': 'D', 'N': 'K', 'O': 'R', 'P': 'W',
     'Q': 'E', 'R': 'F', 'S': 'M', 'T': 'S', 'U': 'X', 'V': 'G', 'W': 'H', 'X': 'N',
     'Y': 'T', 'Z': 'Y'}
    'XKJGUFMJST'
    """
    key = key.upper()
    pt = pt.upper()
    temp = []
    for i in key:
        if i not in temp:
            temp.append(i)
    len_temp = len(temp)
    # print(temp)
    alpha = []
    modalpha = []
    for i in range(65, 91):
        t = chr(i)
        alpha.append(t)
        if t not in temp:
            temp.append(t)
    # print(temp)
    r = int(26 / 4)
    # print(r)
    k = 0
    for i in range(r):
        t = []
        for j in range(len_temp):
            t.append(temp[k])
            if not (k < 25):
                break
            k += 1
        modalpha.append(t)
    # print(modalpha)
    d = {}
    j = 0
    k = 0
    for j in range(len_temp):
        for i in modalpha:
            if not (len(i) - 1 >= j):
                break
            d[alpha[k]] = i[j]
            if not k < 25:
                break
            k += 1
    print(d)
    cypher = ""
    for i in pt:
        cypher += d[i]
    return cypher


print(mixed_keyword("college", "UNIVERSITY"))

# Write a python function to decrypt caesar with chi_squared


from typing import Tuple


def decrypt_caesar_with_chi_squared(
    ciphertext: str,
    cipher_alphabet: str = None,
    frequencies_dict: str = None,
    case_sensetive: bool = False,
) -> Tuple[int, float, str]:
    """
    Basic Usage
    ===========
    Arguments:
    * ciphertext (str): the text to decode (encoded with the caesar cipher)
    Optional Arguments:
    * cipher_alphabet (list): the alphabet used for the cipher (each letter is
      a string separated by commas)
    * frequencies_dict (dict): a dictionary of word frequencies where keys are
      the letters and values are a percentage representation of the frequency as
      a decimal/float
    * case_sensetive (bool): a boolean value: True if the case matters during
      decryption, False if it doesn't
    Returns:
    * A tuple in the form of:
      (
        most_likely_cipher,
        most_likely_cipher_chi_squared_value,
        decoded_most_likely_cipher
      )
      where...
      - most_likely_cipher is an integer representing the shift of the smallest
        chi-squared statistic (most likely key)
      - most_likely_cipher_chi_squared_value is a float representing the
        chi-squared statistic of the most likely shift
      - decoded_most_likely_cipher is a string with the decoded cipher
        (decoded by the most_likely_cipher key)
    The Chi-squared test
    ====================
    The caesar cipher
    -----------------
    The caesar cipher is a very insecure encryption algorithm, however it has
    been used since Julius Caesar. The cipher is a simple substitution cipher
    where each character in the plain text is replaced by a character in the
    alphabet a certain number of characters after the original character. The
    number of characters away is called the shift or key. For example:
    Plain text: hello
    Key: 1
    Cipher text: ifmmp
    (each letter in hello has been shifted one to the right in the eng. alphabet)
    As you can imagine, this doesn't provide lots of security. In fact
    decrypting ciphertext by brute-force is extremely easy even by hand. However
     one way to do that is the chi-squared test.
    The chi-squared test
    -------------------
    Each letter in the english alphabet has a frequency, or the amount of times
    it shows up compared to other letters (usually expressed as a decimal
    representing the percentage likelihood). The most common letter in the
    english language is "e" with a frequency of 0.11162 or 11.162%. The test is
    completed in the following fashion.
    1. The ciphertext is decoded in a brute force way (every combination of the
       26 possible combinations)
    2. For every combination, for each letter in the combination, the average
       amount of times the letter should appear the message is calculated by
       multiplying the total number of characters by the frequency of the letter
       For example:
       In a message of 100 characters, e should appear around 11.162 times.
     3. Then, to calculate the margin of error (the amount of times the letter
        SHOULD appear with the amount of times the letter DOES appear), we use
        the chi-squared test. The following formula is used:
        Let:
        - n be the number of times the letter actually appears
        - p be the predicted value of the number of times the letter should
          appear (see #2)
        - let v be the chi-squared test result (referred to here as chi-squared
          value/statistic)
        (n - p)^2
        --------- = v
           p
    4. Each chi squared value for each letter is then added up to the total.
       The total is the chi-squared statistic for that encryption key.
    5. The encryption key with the lowest chi-squared value is the most likely
       to be the decoded answer.
    Further Reading
    ================
    * http://practicalcryptography.com/cryptanalysis/text-characterisation/chi-squared-
        statistic/
    * https://en.wikipedia.org/wiki/Letter_frequency
    * https://en.wikipedia.org/wiki/Chi-squared_test
    * https://en.m.wikipedia.org/wiki/Caesar_cipher
    Doctests
    ========
    >>> decrypt_caesar_with_chi_squared(
    ...    'dof pz aol jhlzhy jpwoly zv wvwbshy? pa pz avv lhzf av jyhjr!'
    ... )  # doctest: +NORMALIZE_WHITESPACE
    (7, 3129.228005747531,
     'why is the caesar cipher so popular? it is too easy to crack!')
    >>> decrypt_caesar_with_chi_squared('crybd cdbsxq')
    (10, 233.35343938980898, 'short string')
    >>> decrypt_caesar_with_chi_squared(12)
    Traceback (most recent call last):
    AttributeError: 'int' object has no attribute 'lower'
    """
    alphabet_letters = cipher_alphabet or [chr(i) for i in range(97, 123)]
    frequencies_dict = frequencies_dict or {}

    if frequencies_dict == {}:
        # Frequencies of letters in the english language (how much they show up)
        frequencies = {
            "a": 0.08497,
            "b": 0.01492,
            "c": 0.02202,
            "d": 0.04253,
            "e": 0.11162,
            "f": 0.02228,
            "g": 0.02015,
            "h": 0.06094,
            "i": 0.07546,
            "j": 0.00153,
            "k": 0.01292,
            "l": 0.04025,
            "m": 0.02406,
            "n": 0.06749,
            "o": 0.07507,
            "p": 0.01929,
            "q": 0.00095,
            "r": 0.07587,
            "s": 0.06327,
            "t": 0.09356,
            "u": 0.02758,
            "v": 0.00978,
            "w": 0.02560,
            "x": 0.00150,
            "y": 0.01994,
            "z": 0.00077,
        }
    else:
        # Custom frequencies dictionary
        frequencies = frequencies_dict

    if not case_sensetive:
        ciphertext = ciphertext.lower()

    # Chi squared statistic values
    chi_squared_statistic_values = {}

    # cycle through all of the shifts
    for shift in range(len(alphabet_letters)):
        decrypted_with_shift = ""

        # decrypt the message with the shift
        for letter in ciphertext:
            try:
                # Try to index the letter in the alphabet
                new_key = (alphabet_letters.index(letter) - shift) % len(
                    alphabet_letters
                )
                decrypted_with_shift += alphabet_letters[new_key]
            except ValueError:
                # Append the character if it isn't in the alphabet
                decrypted_with_shift += letter

        chi_squared_statistic = 0.0

        # Loop through each letter in the decoded message with the shift
        for letter in decrypted_with_shift:
            if case_sensetive:
                if letter in frequencies:
                    # Get the amount of times the letter occurs in the message
                    occurrences = decrypted_with_shift.count(letter)

                    # Get the excepcted amount of times the letter should appear based
                    # on letter frequencies
                    expected = frequencies[letter] * occurrences

                    # Complete the chi squared statistic formula
                    chi_letter_value = ((occurrences - expected) ** 2) / expected

                    # Add the margin of error to the total chi squared statistic
                    chi_squared_statistic += chi_letter_value
            else:
                if letter.lower() in frequencies:
                    # Get the amount of times the letter occurs in the message
                    occurrences = decrypted_with_shift.count(letter)

                    # Get the excepcted amount of times the letter should appear based
                    # on letter frequencies
                    expected = frequencies[letter] * occurrences

                    # Complete the chi squared statistic formula
                    chi_letter_value = ((occurrences - expected) ** 2) / expected

                    # Add the margin of error to the total chi squared statistic
                    chi_squared_statistic += chi_letter_value

        # Add the data to the chi_squared_statistic_values dictionary
        chi_squared_statistic_values[shift] = [
            chi_squared_statistic,
            decrypted_with_shift,
        ]

    # Get the most likely cipher by finding the cipher with the smallest chi squared
    # statistic
    most_likely_cipher = min(
        chi_squared_statistic_values, key=chi_squared_statistic_values.get
    )

    # Get all the data from the most likely cipher (key, decoded message)
    most_likely_cipher_chi_squared_value = chi_squared_statistic_values[
        most_likely_cipher
    ][0]
    decoded_most_likely_cipher = chi_squared_statistic_values[most_likely_cipher][1]

    # Return the data on the most likely shift
    return (
        most_likely_cipher,
        most_likely_cipher_chi_squared_value,
        decoded_most_likely_cipher,
    )

# Write a python function of deterministic_miller_rabin



def miller_rabin(n: int, allow_probable: bool = False) -> bool:
    """Deterministic Miller-Rabin algorithm for primes ~< 3.32e24.
    Uses numerical analysis results to return whether or not the passed number
    is prime. If the passed number is above the upper limit, and
    allow_probable is True, then a return value of True indicates that n is
    probably prime. This test does not allow False negatives- a return value
    of False is ALWAYS composite.
    Parameters
    ----------
    n : int
        The integer to be tested. Since we usually care if a number is prime,
        n < 2 returns False instead of raising a ValueError.
    allow_probable: bool, default False
        Whether or not to test n above the upper bound of the deterministic test.
    Raises
    ------
    ValueError
    Reference
    ---------
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
    if n == 2:
        return True
    if not n % 2 or n < 2:
        return False
    if n > 5 and n % 10 not in (1, 3, 7, 9):  # can quickly check last digit
        return False
    if n > 3_317_044_064_679_887_385_961_981 and not allow_probable:
        raise ValueError(
            "Warning: upper bound of deterministic test is exceeded. "
            "Pass allow_probable=True to allow probabilistic test. "
            "A return value of True indicates a probable prime."
        )
    # array bounds provided by analysis
    bounds = [
        2_047,
        1_373_653,
        25_326_001,
        3_215_031_751,
        2_152_302_898_747,
        3_474_749_660_383,
        341_550_071_728_321,
        1,
        3_825_123_056_546_413_051,
        1,
        1,
        318_665_857_834_031_151_167_461,
        3_317_044_064_679_887_385_961_981,
    ]

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for idx, _p in enumerate(bounds, 1):
        if n < _p:
            # then we have our last prime to check
            plist = primes[:idx]
            break
    d, s = n - 1, 0
    # break up n -1 into a power of 2 (s) and
    # remaining odd component
    # essentially, solve for d * 2 ** s == n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for prime in plist:
        pr = False
        for r in range(s):
            m = pow(prime, d * 2 ** r, n)
            # see article for analysis explanation for m
            if (r == 0 and m == 1) or ((m + 1) % n == 0):
                pr = True
                # this loop will not determine compositeness
                break
        if pr:
            continue
        # if pr is False, then the above loop never evaluated to true,
        # and the n MUST be composite
        return False
    return True


def test_miller_rabin() -> None:
    """Testing a nontrivial (ends in 1, 3, 7, 9) composite
    and a prime in each range.
    """
    assert not miller_rabin(561)
    assert miller_rabin(563)
    # 2047

    assert not miller_rabin(838_201)
    assert miller_rabin(838_207)
    # 1_373_653

    assert not miller_rabin(17_316_001)
    assert miller_rabin(17_316_017)
    # 25_326_001

    assert not miller_rabin(3_078_386_641)
    assert miller_rabin(3_078_386_653)
    # 3_215_031_751

    assert not miller_rabin(1_713_045_574_801)
    assert miller_rabin(1_713_045_574_819)
    # 2_152_302_898_747

    assert not miller_rabin(2_779_799_728_307)
    assert miller_rabin(2_779_799_728_327)
    # 3_474_749_660_383

    assert not miller_rabin(113_850_023_909_441)
    assert miller_rabin(113_850_023_909_527)
    # 341_550_071_728_321

    assert not miller_rabin(1_275_041_018_848_804_351)
    assert miller_rabin(1_275_041_018_848_804_391)
    # 3_825_123_056_546_413_051

    assert not miller_rabin(79_666_464_458_507_787_791_867)
    assert miller_rabin(79_666_464_458_507_787_791_951)
    # 318_665_857_834_031_151_167_461

    assert not miller_rabin(552_840_677_446_647_897_660_333)
    assert miller_rabin(552_840_677_446_647_897_660_359)
    # 3_317_044_064_679_887_385_961_981
    # upper limit for probabilistic test


if __name__ == "__main__":
    test_miller_rabin()

# Write a python function to implement brute_force_caesar_cipher

def decrypt_brute_force_caesar_cipher(message: str) -> None:
    """
    >>> decrypt('TMDETUX PMDVU')
    Decryption using Key #0: TMDETUX PMDVU
    Decryption using Key #1: SLCDSTW OLCUT
    Decryption using Key #2: RKBCRSV NKBTS
    Decryption using Key #3: QJABQRU MJASR
    Decryption using Key #4: PIZAPQT LIZRQ
    Decryption using Key #5: OHYZOPS KHYQP
    Decryption using Key #6: NGXYNOR JGXPO
    Decryption using Key #7: MFWXMNQ IFWON
    Decryption using Key #8: LEVWLMP HEVNM
    Decryption using Key #9: KDUVKLO GDUML
    Decryption using Key #10: JCTUJKN FCTLK
    Decryption using Key #11: IBSTIJM EBSKJ
    Decryption using Key #12: HARSHIL DARJI
    Decryption using Key #13: GZQRGHK CZQIH
    Decryption using Key #14: FYPQFGJ BYPHG
    Decryption using Key #15: EXOPEFI AXOGF
    Decryption using Key #16: DWNODEH ZWNFE
    Decryption using Key #17: CVMNCDG YVMED
    Decryption using Key #18: BULMBCF XULDC
    Decryption using Key #19: ATKLABE WTKCB
    Decryption using Key #20: ZSJKZAD VSJBA
    Decryption using Key #21: YRIJYZC URIAZ
    Decryption using Key #22: XQHIXYB TQHZY
    Decryption using Key #23: WPGHWXA SPGYX
    Decryption using Key #24: VOFGVWZ ROFXW
    Decryption using Key #25: UNEFUVY QNEWV
    """
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for key in range(len(LETTERS)):
        translated = ""
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print(f"Decryption using Key #{key}: {translated}")


# def main():
#     message = input("Encrypted message: ")
#     message = message.upper()
#     decrypt_brute_force_caesar_cipher(message)

# main()

# Write a python function to compare string
  
def compare_string(string1: str, string2: str) -> str:
    """
    >>> compare_string('0010','0110')
    '0_10'
    >>> compare_string('0110','1101')
    -1
    """
    l1 = list(string1)
    l2 = list(string2)
    count = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            count += 1
            l1[i] = "_"
    if count > 1:
        return -1
    else:
        return "".join(l1)

# Write a python functio to Convert a Decimal Number to a Binary Number.


def decimal_to_binary(num: int) -> str:

    """
    Convert an Integer Decimal Number to a Binary Number as str.
    >>> decimal_to_binary(0)
    '0b0'
    >>> decimal_to_binary(2)
    '0b10'
    >>> decimal_to_binary(7)
    '0b111'
    >>> decimal_to_binary(35)
    '0b100011'
    >>> # negatives work too
    >>> decimal_to_binary(-2)
    '-0b10'
    >>> # other floats will error
    >>> decimal_to_binary(16.16) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> # strings will error as well
    >>> decimal_to_binary('0xfffff') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'str' object cannot be interpreted as an integer
    """

    if type(num) == float:
        raise TypeError("'float' object cannot be interpreted as an integer")
    if type(num) == str:
        raise TypeError("'str' object cannot be interpreted as an integer")

    if num == 0:
        return "0b0"

    negative = False

    if num < 0:
        negative = True
        num = -num

    binary = []
    while num > 0:
        binary.insert(0, num % 2)
        num >>= 1

    if negative:
        return "-0b" + "".join(str(e) for e in binary)

    return "0b" + "".join(str(e) for e in binary)

# Write a python function to Convert a positive Decimal Number to Any Other Representation


def decimal_to_any(num: int, base: int) -> str:
    """
    Convert a positive integer to another base as str.
    >>> decimal_to_any(0, 2)
    '0'
    >>> decimal_to_any(5, 4)
    '11'
    >>> decimal_to_any(20, 3)
    '202'
    >>> decimal_to_any(58, 16)
    '3A'
    >>> decimal_to_any(243, 17)
    'E5'
    >>> decimal_to_any(34923, 36)
    'QY3'
    >>> decimal_to_any(10, 11)
    'A'
    >>> decimal_to_any(16, 16)
    '10'
    >>> decimal_to_any(36, 36)
    '10'
    >>> # negatives will error
    >>> decimal_to_any(-45, 8)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: parameter must be positive int
    >>> # floats will error
    >>> decimal_to_any(34.4, 6) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: int() can't convert non-string with explicit base
    >>> # a float base will error
    >>> decimal_to_any(5, 2.5) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> # a str base will error
    >>> decimal_to_any(10, '16') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'str' object cannot be interpreted as an integer
    >>> # a base less than 2 will error
    >>> decimal_to_any(7, 0) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: base must be >= 2
    >>> # a base greater than 36 will error
    >>> decimal_to_any(34, 37) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: base must be <= 36
    """
    if isinstance(num, float):
        raise TypeError("int() can't convert non-string with explicit base")
    if num < 0:
        raise ValueError("parameter must be positive int")
    if isinstance(base, str):
        raise TypeError("'str' object cannot be interpreted as an integer")
    if isinstance(base, float):
        raise TypeError("'float' object cannot be interpreted as an integer")
    if base in (0, 1):
        raise ValueError("base must be >= 2")
    if base > 36:
        raise ValueError("base must be <= 36")
    # fmt: off
    ALPHABET_VALUES = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F',
                       '16': 'G', '17': 'H', '18': 'I', '19': 'J', '20': 'K', '21': 'L',
                       '22': 'M', '23': 'N', '24': 'O', '25': 'P', '26': 'Q', '27': 'R',
                       '28': 'S', '29': 'T', '30': 'U', '31': 'V', '32': 'W', '33': 'X',
                       '34': 'Y', '35': 'Z'}
    # fmt: on
    new_value = ""
    mod = 0
    div = 0
    while div != 1:
        div, mod = divmod(num, base)
        if base >= 11 and 9 < mod < 36:
            actual_value = ALPHABET_VALUES[str(mod)]
            mod = actual_value
        new_value += str(mod)
        div = num // base
        num = div
        if div == 0:
            return str(new_value[::-1])
        elif div == 1:
            new_value += str(div)
            return str(new_value[::-1])

    return new_value[::-1]

# Write a python function to convert any binary string to the octal equivalent.


def bin_to_octal(bin_string: str) -> str:
    if not all(char in "01" for char in bin_string):
        raise ValueError("Non-binary value was passed to the function")
    if not bin_string:
        raise ValueError("Empty string was passed to the function")
    oct_string = ""
    while len(bin_string) % 3 != 0:
        bin_string = "0" + bin_string
    bin_string_in_3_list = [
        bin_string[index : index + 3]
        for index, value in enumerate(bin_string)
        if index % 3 == 0
    ]
    for bin_group in bin_string_in_3_list:
        oct_val = 0
        for index, val in enumerate(bin_group):
            oct_val += int(2 ** (2 - index) * int(val))
        oct_string += str(oct_val)
    return oct_string


# Write a function to Convert International System of Units (SI) and Binary prefixes
from enum import Enum
from typing import Union


class SI_Unit(Enum):
    yotta = 24
    zetta = 21
    exa = 18
    peta = 15
    tera = 12
    giga = 9
    mega = 6
    kilo = 3
    hecto = 2
    deca = 1
    deci = -1
    centi = -2
    milli = -3
    micro = -6
    nano = -9
    pico = -12
    femto = -15
    atto = -18
    zepto = -21
    yocto = -24


class Binary_Unit(Enum):
    yotta = 8
    zetta = 7
    exa = 6
    peta = 5
    tera = 4
    giga = 3
    mega = 2
    kilo = 1


def convert_si_prefix(
    known_amount: float,
    known_prefix: Union[str, SI_Unit],
    unknown_prefix: Union[str, SI_Unit],
) -> float:
    """
    Wikipedia reference: https://en.wikipedia.org/wiki/Binary_prefix
    Wikipedia reference: https://en.wikipedia.org/wiki/International_System_of_Units
    >>> convert_si_prefix(1, SI_Unit.giga, SI_Unit.mega)
    1000
    >>> convert_si_prefix(1, SI_Unit.mega, SI_Unit.giga)
    0.001
    >>> convert_si_prefix(1, SI_Unit.kilo, SI_Unit.kilo)
    1
    >>> convert_si_prefix(1, 'giga', 'mega')
    1000
    >>> convert_si_prefix(1, 'gIGa', 'mEGa')
    1000
    """
    if isinstance(known_prefix, str):
        known_prefix: SI_Unit = SI_Unit[known_prefix.lower()]
    if isinstance(unknown_prefix, str):
        unknown_prefix: SI_Unit = SI_Unit[unknown_prefix.lower()]
    unknown_amount = known_amount * (10 ** (known_prefix.value - unknown_prefix.value))
    return unknown_amount


def convert_binary_prefix(
    known_amount: float,
    known_prefix: Union[str, Binary_Unit],
    unknown_prefix: Union[str, Binary_Unit],
) -> float:
    """
    Wikipedia reference: https://en.wikipedia.org/wiki/Metric_prefix
    >>> convert_binary_prefix(1, Binary_Unit.giga, Binary_Unit.mega)
    1024
    >>> convert_binary_prefix(1, Binary_Unit.mega, Binary_Unit.giga)
    0.0009765625
    >>> convert_binary_prefix(1, Binary_Unit.kilo, Binary_Unit.kilo)
    1
    >>> convert_binary_prefix(1, 'giga', 'mega')
    1024
    >>> convert_binary_prefix(1, 'gIGa', 'mEGa')
    1024
    """
    if isinstance(known_prefix, str):
        known_prefix: Binary_Unit = Binary_Unit[known_prefix.lower()]
    if isinstance(unknown_prefix, str):
        unknown_prefix: Binary_Unit = Binary_Unit[unknown_prefix.lower()]
    unknown_amount = known_amount * (
        2 ** ((known_prefix.value - unknown_prefix.value) * 10)
    )
    return unknown_amount



# Write a function to convert roman to int
def roman_to_int(roman: str) -> int:
    """
    LeetCode No. 13 Roman to Integer
    Given a roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.
    https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500, "MMMCMXCIX": 3999}
    >>> all(roman_to_int(key) == value for key, value in tests.items())
    True
    """
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    place = 0
    while place < len(roman):
        if (place + 1 < len(roman)) and (vals[roman[place]] < vals[roman[place + 1]]):
            total += vals[roman[place + 1]] - vals[roman[place]]
            place += 2
        else:
            total += vals[roman[place]]
            place += 1
    return total



# Write a function to convert celsius to kelvin
def celsius_to_kelvin(celsius: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Celsius to Kelvin and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    >>> celsius_to_kelvin(273.354, 3)
    546.504
    >>> celsius_to_kelvin(273.354, 0)
    547.0
    >>> celsius_to_kelvin(0)
    273.15
    >>> celsius_to_kelvin(20.0)
    293.15
    >>> celsius_to_kelvin("40")
    313.15
    >>> celsius_to_kelvin("celsius")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'celsius'
    """
    return round(float(celsius) + 273.15, ndigits)


# Write a function to convert celsius to rankiine
def celsius_to_rankine(celsius: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Celsius to Rankine and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    >>> celsius_to_rankine(273.354, 3)
    983.707
    >>> celsius_to_rankine(273.354, 0)
    984.0
    >>> celsius_to_rankine(0)
    491.67
    >>> celsius_to_rankine(20.0)
    527.67
    >>> celsius_to_rankine("40")
    563.67
    >>> celsius_to_rankine("celsius")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'celsius'
    """
    return round((float(celsius) * 9 / 5) + 491.67, ndigits)


# Write a function to convert fahrenheit_to_kelvin
def fahrenheit_to_kelvin(fahrenheit: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Fahrenheit to Kelvin and round it to 2 decimal places.
    """
    return round(((float(fahrenheit) - 32) * 5 / 9) + 273.15, ndigits)
