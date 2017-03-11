def get_answer():
	answers={"привет": "И тебе привет!", "как дела?": "Лучше всех!", "пока": "увидимся", "что делаешь?": "сплю"}
	question=input('-')
	return answers.get(question.lower(), "я тебя не понял :-(")
x=0
while x<10:
    question1=get_answer()
    print(question1)
    x+=1