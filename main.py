from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q_dict in question_data:
    question_bank.append(Question(q_dict["question"], q_dict["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
