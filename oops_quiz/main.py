from question_modal import Questions
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Questions(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'you have completed the quiz ,final score is {quiz.score}/{len(question_bank)}')

