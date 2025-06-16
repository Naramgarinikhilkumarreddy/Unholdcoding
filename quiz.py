# Simple Quiz Game in Python

# List of quiz questions, options, and correct answers
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. London", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Who developed Python programming language?",
        "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. Bjarne Stroustrup", "D. James Gosling"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    }
]

# Score variable
score = 0

# Function to run the quiz
def run_quiz():
    global score
    print("🎉 Welcome to the Quiz Game!\n")
    
    for idx, q in enumerate(quiz):
        print(f"Q{idx + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").strip().upper()
        
        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}\n")
    
    print(f"🎯 You got {score} out of {len(quiz)} correct.")

# Run the quiz
run_quiz()