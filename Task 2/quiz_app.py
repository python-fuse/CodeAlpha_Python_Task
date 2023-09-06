quizzes = []
answers = []
global points
points = 0

def add_quiz():
	new_quiz = input('Enter a new quiz question: ')
	quizzes.append(new_quiz)
	new_quiz_answer = input("Enter the quiz's answer: ")
	answers.append(new_quiz_answer)
	choice()

def choice():
	choice = input("Enter 'A' to add another or 'Q' to return to menu: ")
	if choice.lower() == 'a':
		add_quiz()

	elif choice.lower() == 'q':
		main()

   

def quiz_app():
	global points
	current_ans = 0

	for i in quizzes:
		print(f"Question: {i}?")
		attempt = input('Enter answer: ')
		if attempt.lower() == answers[current_ans]:
			print('Correct')
			points +=1
			current_ans+=1
		else:
			print('Wrong Answer')
			print(f'the correct answer is {answers[current_ans]}')
			current_ans+=1
	player_choice()
			

def player_choice():
	choice = input('Would you like to play again? Y/N:')
	if choice.lower() == "y":
		playQuiz()
	if choice.lower() == 'n':
		main()

def playQuiz():
    print('Welcome to the quiz task!')
    print("Enter 'S' to start or 'Q' to exit to menu")
    command = input('Enter the command: ')
    if command.lower() == 's':
      quiz_app()
    elif command.lower() == 'q':
      main()

def main():
	global points
	print('Enter "Q" at any point to quit')
	ask = input('Admin or Player: ')
	if ask.lower() == 'admin':
		add_quiz()
	elif ask.lower() == 'player':
		playQuiz()
	elif ask.lower() == 'q':
		print(f'Thanks for playing you scored {points} points')
	else:
		main()


if __name__ == '__main__':
	main()