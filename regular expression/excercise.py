#1. Check if strings contain only octal digits

def is_octal(s):
    return all(ch in '01234567' for ch in s)
strings = ['789','123','004']
result = {s: is_octal(s) for s in strings}
print(result)

#2. Extract user ID, domain name and suffix from email addresses
emails = """zuck@facebook.com sunder33@google.com jeff42@amazon.com"""
email_list = emails.split()

for email in email_list:
    user, domain = email.split('@')
    domain_name, suffix = domain.split('.')
    print(f"User ID: {user}, Domain: {domain_name}, Suffix: {suffix}")

#3. Split irregular sentence into proper words
import re

sentence = "A, very very; irregular_sentence"
cleaned = re.sub(r'[^\w\s]', '', sentence).replace('_', ' ')
print(cleaned)

#4. Clean up tweet to remove extras
import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxod cc: @garybernhardt #rstats'''

def clean_tweet(text):
    text = re.sub(r'RT|cc', '', text)
    text = re.sub(r'http\S+|@\S+|#\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return ' '.join(text.split())

print(clean_tweet(tweet))
# 5. Extract text between HTML tags
import requests
from bs4 import BeautifulSoup

url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
text_list = [tag.get_text() for tag in soup.find_all()]
print(text_list)

#6. Words that begin and end with the same character
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
matching_words = [w for w in words if w[0] == w[-1]]
print(matching_words)

