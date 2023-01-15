from flask import Flask, jsonify, request
import numpy as np
import json

app = Flask(__name__)
with open('task.json', 'r') as f:
    task = json.load(f)


@app.route('/api/v1/fruits', methods=['GET'])
def read_json():
    return jsonify(task)


@app.route('/api/v1/fruits/<int:id>', methods=['GET'])
def get_id(id):
    for x in task:
        if x["id"] == id:
            return jsonify(x)
    else:
        return "the id doesn't exist"


# it works!,tried it in postman 
# \
@app.route('/api/v1/fruits/<int:id>', methods=['DELETE'])
def delete_id(id):

    for i in task:
        if i["id"] == id:
            task.remove(i)
            with open('data.json', 'w') as json_file:
                json.dump(task, json_file)
            return 'deleted successfully', 200
            

    else:
        return jsonify({"error": "the Fruit u try to delete is  not found"}), 404
            



if __name__ == "__main__":

    app.run(debug=True)
