from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]




@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if task_id not in [i['id'] for i in tasks]:
            abort(404)
    else:
        task = list(filter(lambda t: t['id'] == task_id, tasks))[0]
        return jsonify({'task': task})


# обработка ошибок
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# новый метод для получения всех задач
@app.route('/todo/api/v1/all_tasks', methods=['GET'])
def all_tasks():
    return jsonify(tasks)


@app.route('/todo/api/v1/tasks', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    
    tasks.append(request.json)
    return jsonify(request.json), 201




@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
