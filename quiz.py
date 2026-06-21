print("Welcome to the quiz!")
quiz = [
    {
        "question": "What is the capital of India?",
        "answer": "Delhi"
    },
    {
        "question": "What is 2 + 2?",
        "answer": "4"
    },
    {
        "question": "Which language are you learning?",
        "answer": "Python"
    },
    {
        "question": "How many days are there in a week?",
        "answer": "7"
    },
    {
        "question": "What color is the sky?",
        "answer": "Blue"
    }
]
score = 0
for question in quiz:
    print("Question : " + question["question"])
    user_answer = input("Answer: ")
    if user_answer.strip().upper() == question["answer"].upper():
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print("Correct answer: " + question["answer"])
print("Quiz Finished!")
print("Total score: " + str(score) + "/" + str(len(quiz)))
