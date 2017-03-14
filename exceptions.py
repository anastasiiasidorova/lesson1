def ask_user():
	try:
		while True:
			user_input = input('Как дела?')
	except (KeyboardInterrupt):
		print('Вы такой интересный собеседник, как жаль, что вы уходите')

ask_user()