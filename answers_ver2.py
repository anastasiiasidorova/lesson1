def get_answer():
	answers={"привет": "И тебе привет!", "как дела?": "Лучше всех!", "пока": "увидимся"}
	question=input('-')
	return answers.get(question.lower(), "я тебя не понял :-(")
question1=get_answer()
print(question1) 
question2=get_answer()
print(question2)
question3=get_answer()
print(question3)