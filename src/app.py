from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    done = request_body.get("done")
    label = request_body.get("label")
    if None in [done, label]:
        return jsonify({"Fields missing"}), 400    
    todos.append({
        "done": done,
        "label": label
    })
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos), 200

##################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)