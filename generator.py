import random, string, os
#random -> imports 'random' functions.
#string -> imports 'string' functions.
#os -> imports 'os' functions.

#we have to create 4 different randomized variables to get variety.
#i am doing that because i want to get all types of keys in one case.
# min. 1 - max. 3 || u can change it as you want.
digit1 = ''.join(random.choices(string.ascii_uppercase, k=random.randint(1,3)))
digit2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1,3)))
digit3 = ''.join(random.choices(string.digits, k=random.randint(1,3))) 
digit4 = ''.join(random.choices(string.punctuation, k=random.randint(1,3))) 

#randomly getting integer between 1-5.
#with that number we are randomly accessing methods.
random_method = random.randint(1,5)
#prints method for checking purposes.
print("method: ", random_method)

#i've created 5 methods from my mind to achieve more systematics.
if(random_method == 1):
   	print("output: ", digit1 + digit3 + digit2 + digit4)
if(random_method == 2):
   	print("output: ", digit2 + digit1 + digit4 + digit3)
if(random_method == 3):
    print("output: ", digit3 + digit4 + digit2 + digit1)
if(random_method == 4):
    print("output: ", digit1 + digit3 + digit4 + digit2)
if(random_method == 5):
	print("output: ", digit4 + digit2 + digit3 + digit1)
#pausing program through command prompt's pause function.
os.system("pause")
