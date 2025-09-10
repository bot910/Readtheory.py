import json
import sys
import time
import requests

def getletter(num):
    if 0 <= num <= 25:
        return chr(ord('A') + num)

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
    """Submit the answer to a question."""
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

    if isinstance(data, dict):
        print("Top-level keys:", list(data.keys())[:20])
    else:
        print(f"Response is non-JSON text, {len(data)} characters. Preview:")

    if 'command' in data and 'questions' in data['command']:
        questions = data['command']['questions']
        for i, question in enumerate(questions, start=1):
            qid = question.get('questionId') or question.get('id')
            correct_id = question.get('correct_answer_id')
            answer_ids = [answer.get('id') for answer in question.get('answers', [])]
            correct_ans_index = answer_ids.index(correct_id)

            print(f"Question {i}:")
            print(f"  Question ID: {qid}")
            print(f"  Correct Answer ID: {correct_id}")
            print(f"  All Answer IDs: {answer_ids}")
            print(f"  Correct answer index: {correct_ans_index}")
            print(f"  Correct answer letter: {getletter(correct_ans_index)}")
            print("\nSubmitting answer...")

            try:
                resp = post_answer(token, int(user_id), qid, correct_id, elapsed_seconds=0)
                print("\nSubmitted answer accepted")
            except requests.HTTPError as e:
                print(f"\nHTTP error on submission: {e}")
            except Exception as e:
                print(f"\nError on submission: {e}")

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

print("Get your auth token from the browser devtools")
print("Get your user ID from the browser devtools\n")
print("IMPORTANT: dont answer too many quizzes, you might get banned (or reported by your teacher). \n")

token = input("Auth token (paste 'Bearer ...'): ").strip()
user_id = input("User ID (e.g. 25384163): ").strip()
amount = input("Amount of times to run (e.g. 50):").strip()

time.sleep(1)

print("\nStarting bot...")
print("\n")
for i in range(2):
    main()
    print("\n")
    print(f"--- Completed iteration {i+1}/50 ---")
    time.sleep(1.5)
