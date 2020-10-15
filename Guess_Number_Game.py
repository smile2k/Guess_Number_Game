#Import section
import sys
import numpy as np

#Gioi thieu
print('--Xin chao cac ban den voi Guess Number Game--\nBan co 5 luot doan')
number = np.random.randint(low =1,high = 100)

#De debug
print(number) #Bo comment cau nay de debug

#Main program
guess=int(input('Nhap so ban doan trong khoang tu (1,100): ')) #Them int ben ngoai de chuyen sang dang int luon cho input
i=1
while(i!= 6):
    #Doan dung
	if(guess == number):
		print('\n       --CHUC MUNG BAN DA DOAN DUNG--')
		sys.exit() #Exit chuong trinh luon neu doan dung
	#Doan lon hon
	elif(guess>number):
		print('\n Nhap so nho hon! ')
		guess= int(input('\n Nhap so: '))
		i = i + 1
	#Doan nho hon
	elif(guess<number):
		print('\n Nhap so lon hon! ')	
		guess= int(input('\n Nhap so: '))
		i = i + 1

print('\n       --Ban da loss-- ')
