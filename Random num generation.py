# write a funtion that returns a list/array of length n of randomly generated values, from low to high (inclusive)

import random 

def rand_array(start, end, num): 
    int_num = [] 
  
    for j in range(num): 
        int_num.append(random.randint(start, end)) 

    return int_num 

num = 5
start = 0
end = 20
print(rand_array(start, end, num)) 


# Taking input values from the user and displaying it as a string.

str = input("Enter comma seperated elements: ")
list = str.split(",")
print ("List: ", list) 

# for example, input: cat, dog, bird ; output: ['cat' , 'dog', 'bird']
