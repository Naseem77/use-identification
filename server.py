from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/check/', methods=['GET', 'POST', 'DELETE'])
def request_page():
    if(request.method == 'POST'):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.get_json()
            userId = data.get('employee_id')

            with open('employees.json') as f:
                database = json.load(f)
            for i in database['employees']:
                #print("here: ", i['employee_id'])
                if i['employee_id'] == userId:
                    x = True
                    break
                else:
                    x = False
            return jsonify({"eligble": x})
        else:
            return 'Content-Type not supported!'

    if(request.method == 'GET'):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.get_json()
            userId = data.get('employee_id')
            with open('employees.json') as f:
                database = json.load(f)
            for i in database['employees']:
                if i['employee_id'] == userId:
                    return jsonify({"first name: ": i['first_name'], "last name: ": i['last_name'], "Day of birth: ": i['date_of_birth']})
            return 'user does not exists!'
        else:
            return 'Content-Type not supported!'


if __name__ == '__main__':
    app.run(port=8080)
