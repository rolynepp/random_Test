import random
r = random.randint(1 ,100)
x = 1
while True:
	a = input('請輸入數字: ')
	a = int(a)
	if a == r:
		print('終於猜對了')
		break
	elif a > r :
		print('比答案大')
	else:
		print('比答案小')
	print('你總共輸入了',x ,'次')
	x = x + 1
