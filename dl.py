drove = input('Have you ever driven a car?')
if drove != 'yes' and drove != 'no':
	print('please enter yes or no')
	raise systemExit

age = input('How old are you?')

if drove == 'yes': 
	if int(age) > 18:
		print('Good for you')
	else:
		print('等你拿到駕照才可以開')
elif drove == 'no':
	if int(age) >= 18:
		print('Go get the drive license')
	else:
		print('等到18歲，就可以考駕照囉')
else:
	print('please eneter yes or no')

# raise systemExit 觸發程式中止
# cls 可以讓cmd裡的畫面清掉