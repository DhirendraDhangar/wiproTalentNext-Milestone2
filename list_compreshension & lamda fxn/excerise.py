#1
list_1 = [1,2,3,4,5,6,7,8,9]
cubed_list = [x**3 for x in list_1]
print(cubed_list)
# Output: [1, 8, 27, 64, 125, 216, 343, 512, 729]

#2
input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {x: x**3 for x in input_list if x % 2 != 0}
print(output_dict)

#3
import string
alphabet_dict = {letter: idx+1 for idx, letter in enumerate(string.ascii_lowercase)}
print(alphabet_dict)
