ReadTheory Bot
===============

An automated HTTP-based ReadTheory bot.

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
   - Reload the page and search for a POST request where the filename is a 8-10 numbe long string.
   - This is your user ID.
  
![Setup 1](https://i.ibb.co/twh7V1QH/Additional.png)
   
2. Get your AUTH bearer token from the browser developer tools:
   - Click on the POST request.
   - Go to the Headers tab.
   - Look under Request Headers for an Authorization header (the value should "Bearer ....").
   - This is your AUTH bearer token

![Setup 2](https://i.ibb.co/M5hcVf5L/additional-2.png)


Visit [ReadTheory](https://www.readtheory.org/) for more info.


Made and developed by BOT910
© 2025 BOT910
