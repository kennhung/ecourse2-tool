from bs4 import BeautifulSoup
import requests

from constant import baseURL


def getSession():
    r_sess = requests.Session()
    r = r_sess.get(baseURL)  # get first moodle session
    return r_sess


def getLoginToken(soup):
    logintokenTags = soup.findAll('input', {"name": "logintoken"})
    if len(logintokenTags) > 0:
        return logintokenTags[0]["value"]
    else:
        raise Exception("cannot get input with name=logintoken")


def postLogin(username, password, loginToken, request_session):
    return request_session.post(baseURL+"/login/index.php", headers={'Content-Type': "application/x-www-form-urlencoded"}, data="logintoken={loginToken}&username={username}&password={password}".format(
        loginToken=loginToken, username=username, password=password))


def login(username, password, session):
    r = session.get(baseURL + "/login/index.php")
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    loginToken = getLoginToken(soup)
    r = postLogin(username, password, loginToken, session)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    loginErroTags = soup.find("a", {"id": "loginerrormessage"})
    if loginErroTags != None and len(loginErroTags) > 0:
        raise Exception('Login fail: {message}'.format(message = loginErroTags.contents[0]))

def getSesskey(soup):
    return soup.find('input', {"name": "sesskey"})['value']