# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 01:32:58 2020

@author: Vishwas Basotra
"""
# importing flask

from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

stores = [
            {
                'name':'Mart',
                'items':[{'name':'Item1','price':120}]
            }
    ]

# POST - used to recieve data
# GET - used to send data back only

@app.route('/')
def home():
    return render_template('index.html')

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
            'name':request_data['name'],
            'items':[]
        }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string: name>
    # 'hppt://127.0.0.1:5000/store/some_name
@app.route('/store/<string:name>')   
def get_store(name):
    # iterate over stores
    for store in stores:
        # if the store name matches, return it
        if store['name'] == name:
            return jsonify(store)
    # if none match, return an error message
    return jsonify({'ERROR': 'Store Not Found!'})
    
# GET /store
@app.route('/store')   
def get_stores():
    return jsonify({'stores':stores})

# POST /store/<string: name>/item {name:, price:}
@app.route('/store/<string:name>/item',methods=['POST'])   
def create_items_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                    'name': request_data['name'],
                    'price': request_data['price']
                }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'ERROR': 'Item could not be added!'})

# GET /store/<string: name>/item
@app.route('/store/<string:name>/item')   
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'ERROR': 'Item Not Found in Store!'})

app.run(port=5000)
