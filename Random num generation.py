// write a funtion that returns a list/array of length n of randomly generated values, from low to high (inclusive)

import random 

def Rand(start, end, num): 
    int_num = [] 
  
    for j in range(num): 
        int_num.append(random.randint(start, end)) 

    return int_num 

num = 5
start = 0
end = 20
print(Rand(start, end, num)) 
