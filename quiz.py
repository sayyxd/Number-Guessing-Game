questions = [
    ("What is the capital of India?", "delhi"),
    ("Which language is this quiz written in?", "python"),
    ("What is 12 * 12?", "144"),
    ("Which planet is known as the Red Planet?", "mars"),
]

score = 0
for q, answer in questions:
    if input(q + " ").strip().lower() == answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. Answer: {answer}\n")

print(f"Final score: {score}/{len(questions)}")
percent = score / len(questions) * 100
print("Great job!" if percent >= 75 else "Keep practicing!")
