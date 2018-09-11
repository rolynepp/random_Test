import random
r = random.randint(1 ,100)
while True:
	a = input('請輸入數字: ')
	a = int(a)
	if a == r:
		print('終於猜對了')
	elif a > r :
		print('比答案大')
	else:
		print('比答案小')

