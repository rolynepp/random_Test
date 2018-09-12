import random
s = input('請決定隨機數字,開始: ')
e = input('請決定隨機數字,結尾: ')
s = int(s)
e = int(e)

r = random.randint(s ,e)
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
	x = x + 1    #新更改的地方是為了顯示出key進去的次數
	# x += 1 及是x = x + 1的快寫法
