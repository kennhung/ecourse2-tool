from bs4 import BeautifulSoup
import requests
from getpass import getpass
from constant import baseURL
from login import login, getSession

username = ""
password = ""

session = getSession()
login(username, password, session)

url = input()

r = session.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())