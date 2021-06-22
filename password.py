# 密码重试程序
# password = 'a123456'
# 让使用者重复输入密码
# 最多输入3次
# 如果正确 就印出 "Login successfully!"
# 如果不正确 就印出 "Your password is wrong! You have__times chance remaining!"

password = 'a123456'
i = 3 # 剩余机会
while i > 0:
	i = i - 1
	pwd = input('Please input your password: ')
	if pwd == password:
		print('Login successfully!')
		break # 逃出回圈
	else:
		print('Password is wrong!')
		if i > 0:
			print('You have ', i, 'chances')
		else:
			print('No more chance! Your account is locked!')



