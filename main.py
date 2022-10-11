
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

for i in range(len(num2)-len(num1)+1):
	if num1==num2[i:len(num1)]:
		print("True")
		break
	else:
		print("False")
# ******************************
# Make your Code
# ******************************

# print ('True') or ('False')
