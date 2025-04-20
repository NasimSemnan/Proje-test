questions = {
    "What is the capital of Iran?": "Tehran",
    "What is 2 + 2?": "4",
    "What is the color of the sky during the day?": "Blue",
    "What animal barks?": "Dog"
}
score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("✅ ok")
        score += 1
    else:
        print(f"❌false : {answer}")
print(f"\nfinal score: {score} az {len(questions)}")
