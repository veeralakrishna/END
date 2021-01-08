# Submitted By:

| **Name**                  |  **CanvasID**                                                                    									             |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Saravana Alagar           | sarvan0506@gmail.com                                                                                      |
| Ravindra Bharathi         | srbharathee@gmail.com                                                               									    |
| Veerala Hari Krishna      | veeralakrishna@gmail.com                                                            									    |
| Dinesh Reddy              | dinereddy1717@gmail.com                                                             									    |

# Part 1: Create a Seq2Seq model using a Encoder-Decoder Architecture to translate English to German

Refer the notebook `Sequence_to_Sequence_Learning_with_Neural_Networks.ipynb`

## Model

```
Seq2Seq(  
  (encoder): Encoder(  
    (embedding): Embedding(5893, 256)  
    (rnn): LSTM(256, 512, num_layers=3, dropout=0.5)  
    (dropout): Dropout(p=0.5, inplace=False)  
  )  
  (decoder): Decoder(  
    (embedding): Embedding(7855, 256)  
    (rnn): LSTM(256, 512, num_layers=3, dropout=0.5)  
    (fc_out): Linear(in_features=512, out_features=7855, bias=True)  
    (dropout): Dropout(p=0.5, inplace=False)  
  )  
)  
```

## Training Log

```
Epoch: 01 | Time: 0m 52s  
	Train Loss: 5.231 | Train PPL: 186.910  
	 Val. Loss: 4.990 |  Val. PPL: 146.906  
Epoch: 02 | Time: 0m 52s  
	Train Loss: 4.813 | Train PPL: 123.042  
	 Val. Loss: 5.086 |  Val. PPL: 161.743  
Epoch: 03 | Time: 0m 53s  
	Train Loss: 4.569 | Train PPL:  96.419  
	 Val. Loss: 5.040 |  Val. PPL: 154.480  
Epoch: 04 | Time: 0m 52s  
	Train Loss: 4.417 | Train PPL:  82.845  
	 Val. Loss: 4.942 |  Val. PPL: 140.092  
Epoch: 05 | Time: 0m 52s  
	Train Loss: 4.309 | Train PPL:  74.399  
	 Val. Loss: 4.914 |  Val. PPL: 136.203  
Epoch: 06 | Time: 0m 52s  
	Train Loss: 4.187 | Train PPL:  65.793  
	 Val. Loss: 5.089 |  Val. PPL: 162.155  
Epoch: 07 | Time: 0m 53s  
	Train Loss: 4.114 | Train PPL:  61.161  
	 Val. Loss: 4.942 |  Val. PPL: 140.055  
Epoch: 08 | Time: 0m 52s  
	Train Loss: 3.992 | Train PPL:  54.159  
	 Val. Loss: 4.767 |  Val. PPL: 117.587  
Epoch: 09 | Time: 0m 52s  
	Train Loss: 3.885 | Train PPL:  48.645  
	 Val. Loss: 4.526 |  Val. PPL:  92.355  
Epoch: 10 | Time: 0m 52s  
	Train Loss: 3.700 | Train PPL:  40.431  
	 Val. Loss: 4.516 |  Val. PPL:  91.486  
Epoch: 11 | Time: 0m 53s  
	Train Loss: 3.548 | Train PPL:  34.756  
	 Val. Loss: 4.386 |  Val. PPL:  80.286  
Epoch: 12 | Time: 0m 53s  
	Train Loss: 3.456 | Train PPL:  31.679  
	 Val. Loss: 4.328 |  Val. PPL:  75.775  
Epoch: 13 | Time: 0m 53s  
	Train Loss: 3.296 | Train PPL:  27.005  
	 Val. Loss: 4.246 |  Val. PPL:  69.835  
Epoch: 14 | Time: 0m 53s  
	Train Loss: 3.187 | Train PPL:  24.212  
	 Val. Loss: 4.145 |  Val. PPL:  63.119  
Epoch: 15 | Time: 0m 52s  
	Train Loss: 3.057 | Train PPL:  21.257  
	 Val. Loss: 4.067 |  Val. PPL:  58.353  
Epoch: 16 | Time: 0m 52s  
	Train Loss: 2.935 | Train PPL:  18.820  
	 Val. Loss: 4.095 |  Val. PPL:  60.047  
Epoch: 17 | Time: 0m 52s  
	Train Loss: 2.838 | Train PPL:  17.089  
	 Val. Loss: 4.036 |  Val. PPL:  56.607  
Epoch: 18 | Time: 0m 52s  
	Train Loss: 2.747 | Train PPL:  15.591  
	 Val. Loss: 4.060 |  Val. PPL:  57.952  
Epoch: 19 | Time: 0m 52s  
	Train Loss: 2.674 | Train PPL:  14.500  
	 Val. Loss: 3.945 |  Val. PPL:  51.684  
Epoch: 20 | Time: 0m 52s  
	Train Loss: 2.586 | Train PPL:  13.270  
	 Val. Loss: 3.978 |  Val. PPL:  53.404  
```

## Perplexity

<img src="assets/perplexity.png" width="600">


# Part 2: Create 100 python programs with description and code.

Please find the descriptions of the program below. Refer `sample.py` for code

1. write a python function to find and return nth element in a user provided list
2. write a python function to sort an array using binary search algorithm
3. write a python program to seperate each character in a string with <space>
4. write a python function to Calculate and return mean of user provided list of numbers
5. write a python function to calculate and return standard deviation of user provided list of numbers 
6. write a python function to Find and return min in a user provided list of numbers
7. write a python function to Join two user provided lists and return it
8. write a python function to empty an user provided list of items
9. write a python function to remove nth item in a user provided list of items 
10. write a python function to increase all items in user provided list by n
11. write a python function to decrease all items in user provided list by n
12. write a python function to divide all items in user provided list by n
13. write a python function to multiply all items in user provided list by n
14. write a python function to Find and return max in a user provider list of numbers
15. write a python function to Check if an item exists in user provided list
16. Write a Python function to Return a copy of a user provided list
17. Write a Python function to Extract even numbers from user provoded list 
18. Write a Python function to Extract odd numbers from user provoded list 
19. Write a python function to create and return a tuple from single user provided item
20. Write a python function to remove duplicates from a list
21. Write a python function to Check whether two user provided sets have an intersection or not
22. write a python function to check and return if set A is subset of B
23. write a python function to check and return if set A is superset of B
24. write a python function to return a list of common items from two user provided lists 
25. Write a python function to combine and return only unique items from two user provided lists 
26. write a python program to check if word exists a sentence
27. write a python program to print out number of non-space ( or non-whitespace) characters in sentence 
28. write a python program to concatenate two strings 
29. write a python program to Replace a substring
30. Write a python function to capitalize
31. write a python program to Add element to a dictionary
32. write a python program to remove an element to a dictionary
33. Join two dictionaries
34. write a python function to find nth root of a number
35. write a python program to find area of a rectangle given sides
36. write a python program to return velocity given displacement(m) and time(s)
37. write a python program to return accelaration given velocity(m/s) and time(s)
38. write a python function to return if one number is greater than other
39. write a python program to print absolute value of a number
40. write a python function to convert feets to meters
41. write a python function to convert inches to centimeters
42. write a python function to convert miles to kilometers
43. write a python function to convert celcius to farenheit
44. write a python program insert number at specified position n of list
insert 10 at 4th index  
45. write a python program to reverse a list
46. write a python function if a and b are equal
47. write a python program to display current time
datetime object containing current date and time
48. write a python function to check if a year is leap year or not
49. write a python function to print volume of a sphere given the radius
50. write a python function to return volume of a cuboid given lenght, breadth and height
51. write a python function to check if a traingle is a right-angled triangle given sides a,b and c
52. write a python function to print the type of a triangle by sides given sides a,b and c
53. write a python program that calculates weight of a person in moon given the person's weight on earth
54. write a python program that calculates the time taken for the light(in seconds) to reach an object given its distance(km) from sun
55. write a python program to Calculate the time taken for a stone(in seconds) to reach the ground given the height(m) it is dropped from.
56. write a python function to return simple interest given p, n and r
57. write a python funtion to return compound interest given principle, time and rate
58. write a python function to return Return On Investment given first value, last value and number of years
59. write a python program to Calculate the number of bricks required to construct a wall given brick and wall dimensions
60. write a python program to Calculate the amount of water harvested in an area due to rain given the surface area and the rainfall.
61. write a python program to Calculate the time left for sunset(hours) given the angle of sun(degrees) from the horizon
62. write a python function to Calculate the distance travelled by a wheel given its radius, rpm and time(minutes)
63. write a python program to check if a fighter jet is super sonic or not
64. write a program to Calculate how old a fossil is, given its Carbon 14 percentage
65. Write a python function to check anagrams
66. Wite a python function to check pangram
67. Write a python function to check palindrome
68. Wite a python function to check word occurences
69. Write a python function for swap case
70. Write a python function to reverse str
71. Write a python function to reverse letters
72. Write a python function to remove duplicates in sting
73. write a python function for navie pattern search
74. Write a code for calculating the most cost-efficient sequence for converting one string into another.
75. Write a python function to convert the entire string to lowecase letters
76. Write a python function to calculate levenstein distance
77. Write a python function to check palindrome for list
78. Write a python function to check palindrome for dict
79. Write a python function to calculate bisection
80. Write a python function to Implementing Secant method in Python
81. Write a python function to calculate intersection
82. Write a python function for bitwise operator example
83. Write a python function for cipher_text
84. Write a python function for base64 encoding and decoding
85. Write a python function for base32 encoding
86. Write a python function for base16 encoding
87. Write a python function RSA prime factor algorithm.
88. Write a Python program to implement Morse Code Translator
89. Write a Python program to implement mono_alphabetic_ciphers
90. Write a Python program to implement mixed_keyword_cypher
91. Write a python function to decrypt caesar with chi_squared
92. Write a python function of deterministic_miller_rabin
93. Write a python function to implement brute_force_caesar_cipher
94. Write a python function to compare string
95. Write a python functio to Convert a Decimal Number to a Binary Number.
96. Write a python function to Convert a positive Decimal Number to Any Other Representation
97. Write a python function to convert any binary string to the octal equivalent.
98. Write a python function to convert roman to int
99. Write a python function to convert celsius to kelvin
100. Write a python function to convert celsius to rankiine
