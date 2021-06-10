from logging import debug
from flask import Flask

app = Flask(__name__)

import dynamodb_handler as dynamodb


@app.route('/')
def root_route():
    return 'Hello World'

# TODO: GET all books

@app.route('/book', methods=['POST'])
def addABook():

    id, title, author = 1001, 'Angels and Demons', 'Dan Brown'

    response = dynamodb.addItemToBook(id, title, author)
    return {
        'response': response
    }

# TODO: DELETE all books

@app.route('/book/<id>', methods=['GET'])
def getBook(id):
    response = dynamodb.GetItemFromBook(id)

    return {
        'response': response
    }

@app.route('/book/<id>', methods=['DELETE'])
def DeleteABook(id):

    response = dynamodb.DeleteAnItemFromBook(id)
    return {
        'response': response
    }   

@app.route('/book/<id>', methods=['PUT'])
def UpdateABook(id):

    data = {
        'title': 'Angels And Demons',
        'author': 'Daniel Brown'
    }

    response = dynamodb.UpdateItemInBook(id, data)

    return {
        'response': response
    }   


# like a book - api
@app.route('/like/book/<id>', methods=['POST'])
def LikeBook(id):

    response = dynamodb.LikeABook(id)

    return {
        'response': response
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)