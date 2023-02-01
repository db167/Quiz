from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import replit

question_bank = []
quiz = QuizBrain(question_bank)

for question in question_data:
	question_text = question["text"]
	question_answer = question["answer"]
	new_question = Question(question_text, question_answer)
	question_bank.append(new_question)

while quiz.quiz_on():
	quiz.next_question()
replit.clear()

print("Quiz Finished")
print(f"Score: {quiz.score}/{quiz.question_number}")


