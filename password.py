# 密码重试程序
# password = 'a123456'
# 让使用者重复输入密码
# 最多输入3次
# 如果正确 就印出 "Login successfully!"
# 如果不正确 就印出 "Your password is wrong! You have__times chance remaining!"

password = 'a123456'
i = 3 # 剩余机会
while True:
	pwd = input('Please input your password: ')
	if pwd == password:
		print('Login successfully!')
		break # 逃出回圈
	else:
		i = i - 1
		print('Password is wrong! You have ', i, 'chances')
		if i == 0:
			break

