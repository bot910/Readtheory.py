ReadTheory.py
=============

An automated HTTP-based ReadTheory bot.

Readtheory is a free online reading platform offering personalized reading comprehension exercises for students of all ages. It is also used in schools to teach English reading, sometimes even given up as homework.
In readtheory you get KP (Knowledge Points) for answering questions correctly. (Teachers can give up homework like: get 200 KP this week)

Answer speed ≈ 60 questions / minute
KP speed (in my testing) ≈ 500 KP / minute 

--- INSTALLATION ---

This bot only works on devices with [Python](https://www.python.org/).

Install dependancies
```bash
pip3 install requests
```
Clone the repo
```bash
git clone https://github.com/bot910/readtheory.py
```
Run the code
```bash
cd readtheory.py
Python3 main.py
```

--- SETUP ---
1. Get your user ID from the browser developer tools:
   - Open your developer tools and go to the Network tab (on the top).
   - Reload the website and search for a POST request where the name is a 8-10 numbe long string.
   - This is your user ID.
   (if you get an http error you probably inputed the wrong userID)
  
![Setup 1](https://i.ibb.co/QjYg24tt/Additional.png)
   
2. Get your AUTH bearer token from the browser developer tools:
   - Click on the POST request.
   - Go to the Headers tab.
   - Look under Request Headers for an Authorization header (the value should "Bearer ....").
   - This is your AUTH bearer token

![Setup 2](https://i.ibb.co/M5hcVf5L/additional-2.png)


The different operating modes:
```
1. normal mode - fetches quiz data and answers all questions correctly.
2. custom mode - choose what percentage of questions to answer correctly (on average).
3. grade mode - choose what grade level to get to.
```



Visit [ReadTheory](https://www.readtheory.org/) to see for yourself, and to check your KP

Made and developed by BOT910

© 2025 BOT910
