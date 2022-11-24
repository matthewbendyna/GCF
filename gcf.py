#gcf.py
#Finds the GCF of any two numbers inputted by a user.

import math, re;

def getGCF(numbers):
    #make sure the function has recieved a list
    if type(numbers) != list:
        raise TypeError("method gcf.getGCF() must recieve a list as it's parameter.\nPlease send it a list of numbers that are integers or can be cast into integers.");
    #make sure list is filled with only integers while leaving some flexibility for programmers to use various data types.
    for x in numbers:
        if type(x) != int:
            if type(x) == str: #will ease the job of programmers by allowing user inputs to be entered into this function as a string 
                is_int = re.compile(r"\d");
                for l in x:
                    if not re.match(is_int, l):
                        raise TypeError("each element in the list passed to gcf.getGCF() must be an integer or translatable to an integer.");
            if type(x) == float:
                raise TypeError("gcf.getGCF() cannot take the GCF of a floating point number.");
            try:
                x=int(x);
            except:
                raise TypeError("an element in the list sent to gcf.getGCF() is not of a type convertible to int")
    #now sort the list of numbers into ascending order
    numbers.sort(reverse=False);
    trial=int(numbers[0]); #initialize test case with smallest number in list
    #now loop through every possible divisor of the lowest number and see if the number shares a common factor with all higher numbers in list.
    while True:
        negative=False;
        for x in numbers:
            y=int(x);
            if y%trial != 0:
                negative=True;
                break;
        if negative==False:
            gcf=trial;
            return gcf;
        else:
            trial-=1;

def enterNumbers(): #A packaged user interface mechanism for enter integers as strings
    numbers=[];
    finishedRx=re.compile(r"finished|done", re.IGNORECASE);
    is_int=re.compile(r"\d");

    print("You will be prompted to enter integer numbers until you type 'done'.");
    number="init";
    print(re.match(finishedRx, number));

    while re.match(finishedRx, number) == None:
        number=input("Please enter an integer: ");
        if re.match(is_int, number):
            numbers.append(number);
        elif re.match(finishedRx, number):
            break;
        else:
            print("Please enter a valid number.");
    return numbers;