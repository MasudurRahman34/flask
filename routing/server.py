from flask import Flask, jsonify, make_response, request
from data import data

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(message = 'Hello World!')
@app.route('/no_content', methods=['GET'])
def no_content():
    return ({'message': 'no content'}, 204)
@app.route('/exp')
def index_explicit():
    resp=make_response({'message': 'Hello World!'})
    resp.status_code = 200
    return resp

@app.route('/data', methods=['GET'])
def get_data():
    
    try:
        if data and len(data) > 0:
            return {'message': f'data of legth {len(data)} found'}
        else:
            return {'message': 'no data found'}, 500
    except NameError:
        return {'message': 'no data found'}, 404

@app.route('/name_search', methods=['GET'])
def name_search():
    query= request.args.get('q')
    if not query:
        return {"message": "query parameter 'q' is missing"}, 422
    for person in data:
        if query.lower() in person['first_name'].lower():
            return {'message': f'found {person} in data'}, 200
    return {'message': 'no data found'}, 404

#Task 2: Create GET /person/id endpoint
@app.route("/person/<id>", methods=['GET'])
def get_person(id):
    for person in data:
        if person['id'] == id:
            return person
    return {'message': 'no data found'}, 404
    
#Task 3: Create DELETE /person/id endpoint
@app.route("/person/<id>", methods=['DELETE'])
def delete_person(id):
    for person in data:
        if person['id'] == id:
            data.remove(person)
            return {"message": "Person with ID deleted"}, 200
    return {'message': 'no data found'}, 404
#Step 4: Parse JSON from Request body
@app.route('/person', methods=['POST'])
def create_person():
    new_person = request.get_json()
    if not new_person:
        return {'message': 'invalid input, no data provided'}, 400
    try:
        data.append(new_person)
    except NameError:
        return {'message': 'data not defined'}, 400
    
    return {'message': f"{new_person['id']}"}, 201

#Step 5: Add error handlers
@app.errorhandler(404)
def api_not_found(error):
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"message": "API not found"}, 404
@app.route('/sentiment', methods=['GET']) 
def sentiment_analyzer():
    return jsonify(message = 'sentiment data!')

if __name__ == '__main__':
    app.run(debug=True)