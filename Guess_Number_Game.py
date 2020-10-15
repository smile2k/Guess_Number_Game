print('--Xin chao cac ban den voi Guess Number Game--')
print('\nBan co 5 luot doan')
import random
import numpy as np
number = np.random.randint(low =1,high = 100)
print(number)
guess=input('Nhap so ban doan trong khoang tu (1,100): ')
guess = int(guess)
i=1
while(i!= 6):
	if(guess == number):
		print('\n --CHUC MUNG BAN DA DOAN DUNG--')
		i = 6
	elif(guess>number):
		print('\n Nhap so nho hon! ')
		guess= input('\n Nhap so: ')
		guess = int(guess)
		i = i+1
	elif(guess<number):
		print('\n Nhap so lon hon! ')	
		guess= input('\n Nhap so: ')
		guess = int(guess)
		i = i+1
if(guess==  number):
	print('\n --CHUC MUNG BAN DA DOAN DUNG--')
else:
	print('\n --Ban da loss-- ')		
