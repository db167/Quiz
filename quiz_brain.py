class QuizBrain:
	
	def __init__(self, q_list):
		self.question_number = 0
		self.score = 0
		self.question_list = q_list 
	
	def next_question(self):
		currentQuestion = self.question_list[self.question_number]
		self.question_number += 1
		user_answer = input(f"Q. {self.question_number}: {currentQuestion.text}(True/False?):")
		self.check_answer(user_answer, currentQuestion.answer)
	
	def check_answer(self, answer, comp_answer):
		if answer.lower() == comp_answer.lower():
			self.score += 1
			print(f"You are correct, {answer} was the right answer")
		else:
			print("Wrong answer")
			print(f"The correct answer is {comp_answer}")
		print(f"Score:{self.score}/{self.question_number}")
		print("/n")

	def quiz_on(self):
		return self.question_number < len(self.question_list)


	
	
		
		
		

