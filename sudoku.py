# -*- codeing: utf-8 -*-

# [Sudoku Analyser]
# Author : Yuichiro SUGA
# Last update : 2016-12-04
# This program analyses a sudoku problem with the input into Icells 2nd
# order list. Even when you get instisfiying result, you may have a proper one
# after changing the order of algorithm in "decide" module.
# This program is designed to be run on the macintosh terminal.


import os
N = 9
Num = set([1,2,3,4,5,6,7,8,9])
Nums = [[Num.copy() for i in range(N)] for i in range(N)]
#Icells = [
#		[0,8,0,5,7,0,2,0,0],
#		[0,0,9,6,0,0,0,0,0],
#		[4,0,1,0,9,0,0,0,0],
#		[9,0,4,0,0,3,0,0,0],
#		[0,0,0,0,0,0,3,0,0],
#		[0,5,0,0,0,0,0,7,8],
#		[0,9,0,0,0,7,5,0,0],
#		[2,0,0,0,0,0,0,6,4],
#		[0,0,0,0,0,6,0,2,9]
#		]
Icells = [
		[3,0,4,2,9,0,7,8,1],
		[1,5,0,7,0,4,6,0,9],
		[0,9,7,6,1,8,0,3,5],
		[8,4,0,0,2,9,5,0,3],
		[7,1,0,5,0,3,2,6,0],
		[0,2,3,4,7,6,0,9,8],
		[9,0,2,3,4,0,8,5,6],
		[4,8,0,0,6,7,3,1,0],
		[6,3,0,8,5,2,9,0,7],
		]
NbAns = 0
NbGiv = 0
NbAnsDet = 0
Max = 50

def main():
	global Icells, Nums, NbAns, Max
	print('--- Sudoku Analyser ---')
	m = 0
	while NbAns < N*N and m < 6:
		init()
		for n in range(Max):
			for x in range(N):
				for y in range(N):
					searchHV(x,y)
					searchS(x,y)
					check(x,y)
			if (m%6 == 0):
				decideS()
				decideH()
				decideV()
			elif(m%6 == 1):
				decideV()
				decideS()
				decideH()
			elif(m%6 == 2):
				decideS()
				decideH()
				decideV()
				print 'SHV'
			elif(m%6 == 3):
				decideS()
				decideV()
				decideH()
			elif(m%6 == 4):
				decideH()
				decideS()
				decideV()
			elif(m%6 == 5):
				decideH()
				decideV()
				decideS()
		m += 1
		#print m, NbAns




def init():
	global Icells, NbAns, NbGiv
	NbAns = 0
	for y in range(N):
		for x in range(N):
			if Icells[x][y] != 0 :
				answer(x,y,Icells[x][y])
				NbGiv += 1

#Search vertically and Horizontally
#Search the same number in the same line and row
#If find the same numver, remove it from Nums
def searchHV(x,y):
	for n in range(N):
			remove(x,y,n,y)
			remove(x,y,x,n)

#Search in Square
def searchS(x,y):
	sx = x-x%3
	sy = y-y%3
	for xn in range(sx,sx+3):
		for yn in range(sy,sy+3):
			remove(x,y,xn,yn)

def check(x,y):
	global Nums
	if type(Nums[x][y]) == set and len(Nums[x][y]) == 1:
		answer(x,y,Nums[x][y].pop())

#Compare vertically
def decideV():
	global Nums
	for xn in range(N):
		nbi = [0 for i in range(N)]#nomber of apparation i 
		for yn in range(N):
			for i in range(N):
				if type(Nums[xn][yn]) == int :
					continue
				if i+1 in Nums[xn][yn]:
					nbi[i] += 1
		for i in range(N):
			if nbi[i] != 1:
				nbi[i] = 0
		for yn in range(N):
			for i in range(N):
				if type(Nums[xn][yn]) == int :
					continue
				if nbi[i]==1 and i+1 in Nums[xn][yn]:
					answer(xn,yn,i+1)

#Compare holizontally
def decideH():
	global Nums
	for yn in range(N):
		nbi = [0 for i in range(N)]#nomber of apparation i 
		for xn in range(N):
			for i in range(N):
				if type(Nums[xn][yn]) == int :
					continue
				if i+1 in Nums[xn][yn]:
					nbi[i] += 1
		for i in range(N):
			if nbi[i] != 1:
				nbi[i] = 0
		for xn in range(N):
			for i in range(N):
				if type(Nums[xn][yn]) == int :
					continue
				if nbi[i]==1 and i+1 in Nums[xn][yn]:
					answer(xn,yn,i+1)

#Compare within square
def decideS():
	global Nums
	for sx in range(3):
		for sy in range(3):
			nbi = [0 for i in range(N)]
			for yn in range(sx*3,sx*3+3):
				for xn in range(sy*3,sy*3+3):
					for i in range(N):
						if type(Nums[xn][yn]) == int :
							continue
						if i+1 in Nums[xn][yn]:
							nbi[i] += 1
			for i in range(N):
				if nbi[i] != 1:
					nbi[i] = 0
			for xn in range(sx*3,sx*3+3):
				for yn in range(sx*3,sx*3+3):
					for i in range(N):
						if type(Nums[xn][yn]) == int :
							continue
						if nbi[i]==1 and i+1 in Nums[xn][yn]:
							answer(xn,yn,i+1)

#remove function
# x,  y: coordinate of reference number
#xn, yn: coordinate of cell to delete
def remove(x,y,xn,yn):
	global Icells, Nums
	if type(Nums[xn][yn]) == int or Icells[x][y] == 0:
		return
	Nums[xn][yn].discard(Icells[x][y])

def answer(x,y,i):
	global Nums, NbAns
	Nums[x][y] = i
	NbAns += 1
	for xn in range(N):
		for yn in range(N):
			if type(Nums[xn][y]) == set:
				Nums[xn][y].discard(i)
			if type(Nums[x][yn]) == set:
				Nums[x][yn].discard(i)
	sx = x-x%3
	sy = y-y%3
	for xn in range(sx,sx+3):
		for yn in range(sy,sy+3):
			if type(Nums[xn][yn]) == set:
				Nums[xn][yn].discard(i)

def show():
	global Icells,Nums,NbAns,NbGiv
	print  '\033[31m' + 'Red' + '\033[0m' + ': Given numbers'
	print  '\033[32m' + 'Red' + '\033[0m' + ': Numbers for blank spaces'
	print '[Given problem]   [Analysis result]'
	print " +---+---+---+     +---+---+---+"
	for x in range(N):
		row = str() + " |"
		for y in range(N):
			if Icells[x][y] != 0 :
				row += '\033[31m' + str(Icells[x][y]) + '\033[0m'
			else :
				row += str('*')
			if y%3 == 2:
				row += "|"
		if x == 4:
			row += " ==> |"
		else :
			row += "     |"
		for y in range(N):
			if type(Nums[x][y]) == set:
				row += '*'
			elif Icells[x][y] != Nums[x][y]:
				row += '\033[32m' + str(Nums[x][y]) + '\033[0m'
			else :
				row += '\033[31m' + str(Nums[x][y]) + '\033[0m'
			if y%3 == 2:
				row += "|"
		print(row) 
		if x%3 == 2 :
			print " +---+---+---+     +---+---+---+"
	print 'Analyse Rate: ', (NbAns-NbGiv), '/', (N*N - NbGiv)
	if NbAns - NbGiv == N*N - NbGiv:
		print 'Anlysis completed!', u'\U0001F617'
	else :
		print 'Analysis failed...', u'\U0001F611'
	print ('--- --- --- --- --- --- --- ---\n')

if __name__ == '__main__' :
	main()
	show()
