#GENERATE RANDOM PASSWORD

import random
import string

pass_len=9
charValues=string.ascii_letters+string.digits+string.punctuation


#list comprehension method
password="".join([random.choice(charValues) for i in range(pass_len)])

#normal loop method 
#password=""
#for i in range(pass_len):
#    password += random.choice(charValues)

print("Your random password is :",password )
