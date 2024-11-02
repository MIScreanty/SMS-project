import requests
import re
import json

def show_money():
    url = "https://my3.webcom.mobi/json/balance.php"
    head = {"Content-type": "text/json; charset=utf-8;"}
    info = {"login": "Vladislav", "password": "QWE456"}
    try:
        answer = requests.post(url, data=json.dumps(info), headers=head)
        print(f"Баланс: {answer.json()["money"]}")
        return answer.json()["money"]
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def valid_phone(n_phone):
    pattern = r'^79\d{9}$'
    return bool(re.match(pattern, n_phone))

def send_sms():
    user = "Vladislav"
    password = "QWE456"
    sender = "Anonim"
    phone = "79280078494"
    if not valid_phone(phone):
        print("Неверный номер телефона")
        return
    text = "Привет, сегодня хороший день!"
    money = show_money()
    balance = int(money) if money.isdigit() else money
    if isinstance(balance, int):
        if balance >= 7:
            url_api = f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={phone}&text={text}"

            answer = requests.get(url_api)

            if answer.status_code == 200:
                print("Сообщение отправлено")
            else:
                print(f"Ошибка: {answer.status_code}")
        else:
            print(f"Недостаточно денег. Ваш баланс: {balance}")
    else:
        print("Незвестен баланс")

send_sms()
