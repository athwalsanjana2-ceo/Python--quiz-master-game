import time
import random

print("🧠 Pai Gaon Quiz Master - CEO Edition")
print("Dekhte hai kitni GK hai!\n")

questions = [
    {"q": "Python ko kisne banaya?", "options": ["A. Guido Van Rossum", "B. Elon Musk", "C. Mark Zuckerberg"], "ans": "A"},
    {"q": "Pai Gaon kaha hai?", "options": ["A. Panipat", "B. Delhi", "C. Mumbai"], "ans": "A"},
    {"q": "1 GB me kitne MB hote hai?", "options": ["A. 1000", "B. 1024", "C. 100"], "ans": "B"},
    {"q": "HTML ka full form?", "options": ["A. Hyper Text Markup Language", "B. High Tech Modern Language", "C. Hello Text Main Language"], "ans": "A"},
    {"q": "Human skin robot me kya lagta hai?", "options": ["A. Latex Glove", "B. Plastic", "C. Iron"], "ans": "A"},
]

random.shuffle(questions)
score = 0

for i, que in enumerate(questions, 1):
    print(f"\nQ{i}. {que['q']}")
    for opt in que['options']:
        print(opt)
    
    ans = input("Jawab (A/B/C): ").upper()
    if ans == que['ans']:
        print("✅ Sahi jawab! Shabash CEO! 🎉")
        score += 1
    else:
        print(f"❌ Galat! Sahi jawab tha {que['ans']}")
    time.sleep(1)

print("\n--------------------------")
print(f"Final Score: {score}/{len(questions)}")
if score == 5:
    print("🔥 Tu toh Genius hai CEO!")
elif score >= 3:
    print("🙂 Good hai, aur practice kar!")
else:
    print("😅 Koi na, kal fir khelenge!")
