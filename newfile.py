score = 0

questions = [
    {
        "question": "What is the capital of India?",
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for AI and Machine Learning?",
        "answer": "Python"
    },
    {
        "question": "How many days are there in a week?",
        "answer": "7"
    },
    {
        "question": "What is 5 + 7?",
        "answer": "12"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars"
    }
]

print("===== QUIZ APP =====\n")

for q in questions:
    print(q["question"])
    user = input("Your Answer: ")

    if user.strip().lower() == q["answer"].lower():
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", q["answer"], "\n")

print("======================")
print("Quiz Finished!")
print("Your Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Practicing!")