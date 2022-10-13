
import sys

num1 = tuple(map(int, input().split()))
num2 = tuple(map(int, input().split()))
for i in range (0,2):
	if num1[0]==num2[i] and num1[1]==num2[i+1] and num1[2]==num2[i+2]:
		print("True")
		break
else:
	print("False")
# ******************************
# Make your Code
# ******************************

# print ('True') or ('False')
