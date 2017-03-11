def get_answer(question):
	answers={"привет": "И тебе привет!", "как дела?": "Лучше всех!", "пока": "увидимся"}
	print(question)
	return answers.get(question.lower(), "Je ne comprends pas!")
question1=get_answer("привет")
print(question1) 
question2=get_answer("как дела?")
print(question2)
question3=get_answer("пока")
print(question3)