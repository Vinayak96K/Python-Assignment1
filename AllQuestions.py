#function for question 1
def fun():
	print('Hello World\n')
#-------------------------------------------#

#function for question 2
def ChkNum(no):
	if(no%2==0):	
		print('The number is even\n')
	else:
		print('The number is odd\n')
#-------------------------------------------#

#function for question 3
def Add(no1,no2):
	return no1+no2
#-------------------------------------------#

#function for question 4
def gun():
	no=0;
	while(no<5):
		print('Marvellous')
		no=no+1;
	print('')
	return
#-------------------------------------------#

#function for question 5
def run():
	no=10;
	while(no>0):
		print(no),
		no=no-1;
	print('\n')
	return
#-------------------------------------------#

#function for question 6
def ChkInt(no):
	if(no>0):	
		print('Positive Number\n')
	elif(no<0):
		print('Negative Number\n')
	else:
		print('Zero\n')
#-------------------------------------------#

#function for question 7
def ChkNumX(no):
	if(no%5==0):	
		return True
	else:
		return False
#-------------------------------------------#

#function for question 8
def pattern1():
	no=5;
	while(no>0):
		print('* '),
		no=no-1;
	print('\n')
	return
#-------------------------------------------#

#function for question 9
def displayEvenX():
	no=1;
	while(no<=10):
		print(no*2),
		no=no+1
	print('\n')
	return
#-------------------------------------------#

#function for question 10
def strLenX(str):
	return len(str)
#-------------------------------------------#
	
###################################################################################################################
#Actual execution sequence
no1=None
no2=None

print("********** Question (1) ***********")
fun()

print("********** Question (2) ***********")
ChkNum(10)

print("********** Question (3) ***********")
no1=input('Enter first number:')
no2=input('Enter Second number:')
no1=Add(no1,no2)
print('Addition is:',no1)
print('')

print("********** Question (4) ***********")
gun()

print("********** Question (5) ***********")
run()

print("********** Question (6) ***********")
no1=input('Enter number:')
ChkInt(no1)

print("********** Question (7) ***********")
no1=input('Enter number:')
if(ChkNumX(no1)):
	print('Returned true\n')
else:
	print('Returned false\n')

print("********** Question (8) ***********")
pattern1()

print("********** Question (9) ***********")
displayEvenX()

print("********** Question (10) ***********")
no1=input('Enter string:')
no2=strLenX(no1)
print('Length:'),
print(no2)
