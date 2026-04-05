from xxlimited_35 import Null

from flask import Flask, request

app = Flask(__name__)

@app.route('/login/username', methods=['POST'])
def login_user_name(**kwargs):
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        if username == 'admin' and password == '123456':
            return {'status':200, 'message': 'Login Successful', 'token': "1234567890abcdefgh"}
        else:
            return {'status':200, 'message': 'Wrong username or password'}
    else:
        return {'status':401, 'message': 'request method not allowed'}

@app.route('/get/userinfo', methods=['GET'])
def get_userinfo():
    token = request.headers.get('Authorization', None)
    if token is None:
        return {'status':401, 'message': 'Token is invalid'}
    print(token)
    # if token == Null:
    #     return {'status':403, 'message': 'Not Login'}
    username = request.args.get('username')
    if username != 'admin':
        return {'status':200, 'message': 'Wrong username'}

    if request.method == 'GET':
        return {'status':200, 'message': 'Select Successful'}
    else:
        return {'status':401, 'message': 'request method not allowed'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(debug=True)