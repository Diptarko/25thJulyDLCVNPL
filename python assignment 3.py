'''
1. Write a function to compute 5/0 and use try/except to catch the exceptions.
'''
def divide_two_nums():
    num1 = float(input('Enter num1: >'))
    num2 = float(input('Enter num2: >'))

    try:
        div_nums = num1/num2
        return float(div_nums)
    except ZeroDivisionError:
        print('Sorry, you cant divide by Zero.')
    

'''2. Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
'''
'''
Design Philosophy :-

1. Start with each element of the subjects list.
2. Each element of subjects loops through the list verb.
3. So, each element of subject, is concatenated with each and every elemnt of verbs list, in the form of a string concatenation.
4. Now each of these concatenated elements, further loops through the list objects.
5. Each of the concatenated elements from the previous step, is concatenated with each and every element of the list verb.

''' 


'''
Below function is used to concatenate a string , a list and a string again.

'''


def add_str(name,verb,obj):
		vrb = iter(verb)
		names_lst = []
		while True:
			try :
                                    
				current_verb = next(vrb)#Take each element from the verb list.
				for itr in obj: #Iterate through the objects list.
					names_lst.append(name+' '+current_verb+' '+itr)#Append the 
			except StopIteration:
				return names_lst


#Below function takes the subjects, verb and objects lists, and prints out all the elements.

def print_output(subjects,verb,objects):
	returns = []
	for itr in subjects:#Loop through the subjects list
		returns.append(add_str(itr,verb,objects))
	for itr in returns:
		for i in itr:
			print(i+'.')


if __name__ == '__main__':

    divide_two_nums()
    '''
    subjects=["Americans ","Indians"]
    verbs=["play","watch"]
    objects=["Baseball","Cricket"]
    print_output(subjects,verbs, objects)
    '''
