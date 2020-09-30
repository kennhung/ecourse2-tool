from bs4 import BeautifulSoup
import requests
from getpass import getpass
from constant import baseURL
from login import login, getSession

def submitAttend(session, sessid, studentPassword):
    r = session.get(
        baseURL + "/mod/attendance/attendance.php?sessid={sessid}".format(sessid=sessid))
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    sessKey = soup.find('input', {"name": "sesskey"})["value"]
    mform_isexpanded_id_session = soup.find(
        'input', {"name": "mform_isexpanded_id_session"})["value"]
    _qf__mod_attendance_student_attendance_form = soup.find(
        'input', {"name": "_qf__mod_attendance_student_attendance_form"})["value"]
    return session.post(baseURL + "/mod/attendance/attendance.php", headers={'Content-Type': "application/x-www-form-urlencoded"},
                        data="sessid={sessid}&sesskey={sesskey}&mform_isexpanded_id_session={mform_isexpanded_id_session}".format(sessid=sessid, sesskey=sessKey, mform_isexpanded_id_session=mform_isexpanded_id_session) +
                        "&_qf__mod_attendance_student_attendance_form={qf}".format(qf=_qf__mod_attendance_student_attendance_form) +
                        "&studentpassword={stuPassword}&status=28725".format(stuPassword=studentPassword))


if __name__ == "__main__":
    username = input("username: ")
    password = getpass()
    session = getSession()
    login(username, password, session)

    sessid = input("sessid: ")
    studentPassword = input("studentPassword: ")
    r = submitAttend(session, sessid, studentPassword)
    soup = BeautifulSoup(r.text, 'html.parser')
    user_notificationsTags = soup.findAll('span', {"id": "user-notifications"})
    print(user_notificationsTags)