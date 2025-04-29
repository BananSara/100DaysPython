from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()

# if quiz still has questions remaining:
while quiz.still_has_questions():
    quiz.next_question()


print('you have completed the quiz!')
print(f'your final score was: {quiz.score}.{len(question_bank)}')