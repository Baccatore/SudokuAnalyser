# -*- codeing: utf-8 -*-

# [Sudoku Analyser]
# Author : Yuichiro SUGA
# Last update : 2016-12-04
# This program analyses a sudoku problem with the input into icells 2nd
# order list. Even when you get instisfiying result, you may have a proper one
# after changing the order of algorithm in "decide" module.
# This program is designed to be run on the macintosh terminal.


import os
N = 9
num = set([1,2,3,4,5,6,7,8,9])
nums = [[num.copy() for i in range(N)] for i in range(N)]
icells = [
		[0,8,0,5,7,0,2,0,0],
		[0,0,9,6,0,0,0,0,0],
		[4,0,1,0,9,0,0,0,0],
		[9,0,4,0,0,3,0,0,0],
		[0,0,0,0,0,0,3,0,0],
		[0,5,0,0,0,0,0,7,8],
		[0,9,0,0,0,7,5,0,0],
		[2,0,0,0,0,0,0,6,4],
		[0,0,0,0,0,6,0,2,9]
		]
nbAns = 0
nbAnsDet = 0

def main():
	global icells, nums
	print('Sudoku Analyser')
	init()
	for n in range(25):
		for x in range(N):
			for y in range(N):
				searchHV(x,y)
				searchS(x,y)
				check(x,y)
		decide()

def init():
	global icells
	for y in range(N):
		for x in range(N):
			if icells[x][y] != 0 :
				answer(x,y,icells[x][y])

#Search vertically and Horizontally
#Search the same number in the same line and row
#If find the same numver, remove it from nums
def searchHV(x,y):
	global icells
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
	global nums
	if type(nums[x][y]) == set and len(nums[x][y]) == 1:
		answer(x,y,nums[x][y].pop())

def decide():
	global nums, nbAnsDet
	#Compare vertically
	for xn in range(N):
		nbi = [0 for i in range(N)]#nomber of apparation i 
		for yn in range(N):
			for i in range(N):
				if type(nums[xn][yn]) == int :
					continue
				if i+1 in nums[xn][yn]:
					nbi[i] += 1
		for i in range(N):
			if nbi[i] != 1:
				nbi[i] = 0
		for yn in range(N):
			for i in range(N):
				if type(nums[xn][yn]) == int :
					continue
				if nbi[i]==1 and i+1 in nums[xn][yn]:
					answer(xn,yn,i+1)
					nbAnsDet +=1
	#Compare holizontally
	for yn in range(N):
		nbi = [0 for i in range(N)]#nomber of apparation i 
		for xn in range(N):
			for i in range(N):
				if type(nums[xn][yn]) == int :
					continue
				if i+1 in nums[xn][yn]:
					nbi[i] += 1
		for i in range(N):
			if nbi[i] != 1:
				nbi[i] = 0
		for xn in range(N):
			for i in range(N):
				if type(nums[xn][yn]) == int :
					continue
				if nbi[i]==1 and i+1 in nums[xn][yn]:
					answer(xn,yn,i+1)
					nbAnsDet +=1
	#Compare within square
	for sx in range(3):
		for sy in range(3):
			nbi = [0 for i in range(N)]
			for yn in range(sx*3,sx*3+3):
				for xn in range(sy*3,sy*3+3):
					for i in range(N):
						if type(nums[xn][yn]) == int :
							continue
						if i+1 in nums[xn][yn]:
							nbi[i] += 1
			for i in range(N):
				if nbi[i] != 1:
					nbi[i] = 0
			for xn in range(sx*3,sx*3+3):
				for yn in range(sx*3,sx*3+3):
					for i in range(N):
						if type(nums[xn][yn]) == int :
							continue
						if nbi[i]==1 and i+1 in nums[xn][yn]:
							answer(xn,yn,i+1)
							nbAnsDet +=1



#remove function
# x,  y: coordinate of reference number
#xn, yn: coordinate of cell to delete
def remove(x,y,xn,yn):
	global icells, nums
	if type(nums[xn][yn]) == int or icells[x][y] == 0:
		return
	nums[xn][yn].discard(icells[x][y])

def answer(x,y,i):
	global nums, nbAns
	nums[x][y] = i
	nbAns += 1
	for xn in range(N):
		for yn in range(N):
			if type(nums[xn][y]) == set:
				nums[xn][y].discard(i)
			if type(nums[x][yn]) == set:
				nums[x][yn].discard(i)
	sx = x-x%3
	sy = y-y%3
	for xn in range(sx,sx+3):
		for yn in range(sy,sy+3):
			if type(nums[xn][yn]) == set:
				nums[xn][yn].discard(i)

def show():
	global icells,nums
	print '[Given problem]   [Analysis result]'
	print " +---+---+---+     +---+---+---+"
	for x in range(N):
		row = str() + " |"
		for y in range(N):
			if icells[x][y] != 0 :
				row += '\033[31m' + str(icells[x][y]) + '\033[0m'
			else :
				row += str(icells[x][y])
			if y%3 == 2:
				row += "|"
		row += "     |"
		for y in range(N):
			if type(nums[x][y]) == set:
				row += '*'
			elif icells[x][y] != nums[x][y]:
				row += '\033[32m' + str(nums[x][y]) + '\033[0m'
			else :
				row += '\033[31m' + str(nums[x][y]) + '\033[0m'
			if y%3 == 2:
				row += "|"
		print(row) 
		if x%3 == 2 :
			print " +---+---+---+     +---+---+---+"

#	for x in range(N):
#		for y in range(N):
#			print x, y, nums[x][y]
#		print "---"

	print (nbAns-25), '/', (81-25)

if __name__ == '__main__' :
	main()
	show()
