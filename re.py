import re
import sys

def sumfile(path):
    summ = 0 # initialize sum to 0
    try:
        file = open(path) # opening the file
    except IOError as e:   
        print(e)
        sys.exit()
        
    for line in file: # looping over the file
        line = line.strip() 
        numbers = re.findall('[0-9]+',line) # find numbers
        if len(numbers) == 0 : continue # if there is no number pass
    
        numbers = list(map(int, numbers))  # convert numbers to int list

        summ = summ+sum(numbers) # calculate the sum
    file.close() # closing the file
    return summ
    
path = input('give me the file path :')

print(sumfile(path))
