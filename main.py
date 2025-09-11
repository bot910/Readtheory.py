import os
import sys
import json
import time
import random
import requests

# dont like my code? fork and fix it yourself

def getletter(num):
    if 0 <= num <= 25:
        return chr(ord('A') + num)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def fetch_quiz_data(token: str, user_id: str) -> dict | str:
    url = f"https://prod.readtheory.org/quiz/student_quiz_data/{user_id}"
    headers = {
        "Authorization": str(token),
        "Accept": "*/*",
        "User-Agent": "python-requests/2.x",
        "Origin": "https://readtheoryapp.com",
        "Referer": "https://readtheoryapp.com/",
        "DNT": "1",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
    }

    resp = requests.get(url, headers=headers, timeout=20)
    resp.raise_for_status()

    try:
        data = resp.json()
    except ValueError:
        data = resp.text



    return data

def post_answer(token: str, student_id: int, question_id: int, answer_id: int, elapsed_seconds: int = 0) -> dict:
    url = "https://prod.readtheory.org/quiz/answer_question"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Origin": "https://readtheoryapp.com",
        "Referer": "https://readtheoryapp.com/",
        "DNT": "1",
        "Cache-Control": "no-cache"
    }

    body = {
        "studentId": student_id,
        "questionId": question_id,
        "answerId": answer_id,
        "elapsedSeconds": elapsed_seconds
    }

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()

def main():

    try:
        data = fetch_quiz_data(token, user_id)
    except requests.HTTPError as e:
        print("HTTP error:", e, file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(3)

    command = data['command']
    grade_map = { "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Eleven": 11, "Twelve": 12}
    quizgrade = grade_map.get(command.get("level"), None)

    if mode == 3 and quizgrade == target_grade:
        clear()
        print(f"Current grade: {quizgrade} / target: {target_grade}")
        print("\nCurrent quiz at grade:", quizgrade)
        print(f"\nReached target grade {target_grade}, stopping.")
        sys.exit(0)

    quizlist = []
    if 'command' in data and 'questions' in data['command']:
        questions = data['command']['questions']
        for i, question in enumerate(questions, start=1):
            qid = question.get('questionId') or question.get('id')
            correct_id = question.get('correct_answer_id')
            answer_ids = [answer.get('id') for answer in question.get('answers', [])]
            correct_ans_index = answer_ids.index(correct_id)

            clear()

            if mode == 1:
                print(f"--- Quiz number {a+1}/{amount} ---\n")
            elif mode == 2:
                print(f"--- Quiz number {a+1}/{amount} ---\n")
            elif mode == 3:
                print(f"--- Quiz number {a+1} ---\n")

            if mode == 3:
                if mode == 3 and quizgrade == target_grade:
                    print(f"\nReached target grade {target_grade}")
                else:
                    print(f"Current grade: {quizgrade} / target: {target_grade}")
            else:
                print("\nCurrent quiz at grade:", quizgrade)
            print("\nFetching quiz data...\n")

            print(f"Question {i}/{len(questions)}:")
            print(f"  Amount of answers: {len(answer_ids)}")
            print(f"  Correct answer letter: {getletter(correct_ans_index)}")
            
            if mode == 1:
                ansid = correct_id
                quizlist.append((True))
            elif mode == 2:
                if random.randint(0, 101) <= correct_percentage:
                    ansid = correct_id
                    quizlist.append((True))
                else:
                    if answer_ids[0] == correct_id:
                        ansid = answer_ids[1]
                    else:
                        ansid = answer_ids[0]
                    quizlist.append((False))
            elif mode == 3:
                if quizgrade < target_grade:
                    ansid = correct_id
                    quizlist.append((True))
                elif quizgrade > target_grade:
                    if answer_ids[0] == correct_id:
                        ansid = answer_ids[1]
                    else:
                        ansid = answer_ids[0]
                    quizlist.append((False))
            
            print("\nSubmitting answer: ", getletter(answer_ids.index(ansid)))
            try:
                post_answer(token, int(user_id), qid, ansid, elapsed_seconds=0)
                print("\nSubmitted answer accepted")
            except requests.HTTPError as e:
                print(f"\nHTTP error on submission: {e}")
            except Exception as e:
                print(f"\nError on submission: {e}")

            time.sleep(0.01)

        scpc = quizlist.count(True) / len(quizlist) * 100
        print(f"\nQuiz completed with score: {int(scpc)}%")
        time.sleep(0.25)

    else:
        print("\n'questions' key not found inside 'command'")



print("""
 ██▀███  ▓█████ ▄▄▄      ▓█████▄ ▄▄▄█████▓ ██░ ██ ▓█████  ▒█████   ██▀███ ▓██   ██▓      ██▓███ ▓██   ██▓
▓██ ▒ ██▒▓█   ▀▒████▄    ▒██▀ ██▌▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒     ▓██░  ██▒▒██  ██▒
▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ░██   █▌▒ ▓██░ ▒░▒██▀▀██░▒███   ▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░     ▓██░ ██▓▒ ▒██ ██░
▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░     ▒██▄█▓▒ ▒ ░ ▐██▓░
░██▓ ▒██▒░▒████▒▓█   ▓██▒░▒████▓   ▒██▒ ░ ░▓█▒░██▓░▒████▒░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░ ██▓ ▒██▒ ░  ░ ░ ██▒▓░
░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒   ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒  ▒▓▒ ▒▓▒░ ░  ░  ██▒▒▒ 
  ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒     ░     ▒ ░▒░ ░ ░ ░  ░  ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░  ░▒  ░▒ ░     ▓██ ░▒░ 
  ░░   ░    ░    ░   ▒    ░ ░  ░   ░       ░  ░░ ░   ░   ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░   ░   ░░       ▒ ▒ ░░  
   ░        ░  ░     ░  ░   ░              ░  ░  ░   ░  ░    ░ ░     ░     ░ ░       ░           ░ ░     
""")
print("An automated http based readtheory bot. \n")
print("Made and developed by BOT910")
print("© 2025 Bot910")

print("\n--- SETUP ---")

print("IMPORTANT: dont answer too many quizzes, you might get banned (or reported by your teacher). \n")
print("Get your auth token from the browser devtools")
print("Get your user ID from the browser devtools\n")

token = input("Auth token (paste 'Bearer ...'): ").strip()
user_id = input("User ID (e.g. 25384163): ").strip()

print("Choose an operating mode:\n")
print("  1. normal mode - fetches quiz data and answers all questions correctly")
print("  2. custom mode - choose what percentage of questions to answer correctly")
print("  3. grade mode - choose what grade level to get to.)\n")

mode = int(input("Enter mode (1, 2 or 3): ").strip())

if mode not in {1, 2, 3}:
    print("Invalid mode selected, exiting.")
    sys.exit(1)

if mode == 1:
    amount = int(input("Amount of times to run (e.g. 50):").strip())
elif mode == 2:
    amount = int(input("Amount of times to run (e.g. 50):").strip())
    correct_percentage = int(input("Correct answer percentage (0-100): ").strip())
    if not (-1 <= correct_percentage <= 101):
        print("Invalid percentage, exiting.")
        sys.exit(1)
elif mode == 3:
    target_grade = int(input("Target grade level (1-12): ").strip())
    amount=9999

time.sleep(1)

clear()

print("\nStarting bot...")
print("\n")
for a in range(amount):
    main()
