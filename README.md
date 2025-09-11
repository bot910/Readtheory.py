**Readtheory.py**
=============

An automated HTTP-based ReadTheory bot.

<br />

Readtheory is a free online reading platform offering personalized reading comprehension exercises for students of all ages. It is also used in schools to teach English reading, sometimes even given up as homework.
In readtheory you get KP (Knowledge Points) for answering questions correctly.

**Answer speed ≈ 60 questions / minute**

**KP speed (in my testing) ≈ 500 KP / minute**


<br />

**--- INSTALLATION ---**

<P>This bot only works on devices with [Python](https://www.python.org/). <br>
It has been tested on linux (ubuntu), but should also work on windows.</p>


<br />

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

<br />

**--- SETUP ---**
1. Get your user ID from the browser developer tools:
   - Open your developer tools and go to the Network tab (on the top).
   - Reload the website and search for a POST request where the name is a 8-10 numbe long string.
   - This is your user ID.
   (if you get an http error you probably inputed the wrong userID)

<br />

![Setup 1](https://i.ibb.co/QjYg24tt/Additional.png)

<br />

2. Get your AUTH bearer token from the browser developer tools:
   - Click on the POST request.
   - Go to the Headers tab.
   - Look under Request Headers for an Authorization header (the value should "Bearer ....").
   - This is your AUTH bearer token

<br />

![Setup 2](https://i.ibb.co/M5hcVf5L/additional-2.png)

<br />

The different operating modes:
```
1. normal mode - fetches quiz data and answers all questions correctly.
2. custom mode - choose what percentage of questions to answer correctly (on average).
3. grade mode - choose what grade level to get to.
```

<br />

Visit [ReadTheory](https://www.readtheory.org/) to see for yourself, and to check your KP

<br />

<p align="center">Made and developed by BOT910</p> 


<p align="center">© 2025 BOT910</p>
