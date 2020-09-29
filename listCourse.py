from bs4 import BeautifulSoup
import requests
from getpass import getpass
from constant import baseURL
from login import login, getSession, getSesskey


def listCouese(session):
    r = session.get(baseURL + "/my")
    r.encoding = 'utf-8'

    soup = BeautifulSoup(r.text, 'html.parser')
    sessKey = getSesskey(soup)

    r = session.post(baseURL + "/lib/ajax/service.php" +
                     "?sesskey={sessKey}&info=core_course_get_enrolled_courses_by_timeline_classification".format(
                         sessKey=sessKey),
                     data='[{"index":0,"methodname":"core_course_get_enrolled_courses_by_timeline_classification","args":{"offset":0,"limit":0,"classification":"inprogress","sort":"fullname"}}]')
    r.encoding = 'utf-8'

    for v in r.json()[0]['data']['courses']:
        # print(v)
        print("{id} {fullnamedisplay}".format(
            id=v['id'], fullnamedisplay=v['fullnamedisplay']))


if __name__ == '__main__':
    username = input("Username: ")
    password = getpass()

    session = getSession()
    login(username, password, session)

    print("Login successful")

    listCouese(session)
