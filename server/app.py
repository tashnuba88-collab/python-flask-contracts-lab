#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response
# sample data the routes search through
contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)


# Returns the contract text with a 200 if the ID exists, otherwise a 404
@app.route('/contract/<int:id>')
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return make_response(contract["contract_information"], 200)
    return make_response("", 404)


# Returns a 204 with no data if the customer exists (data is sensitive), otherwise a 404
@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name in customers:
        return make_response("", 204)
    return make_response("", 404)


if __name__ == '__main__': 
    app.run(port=5555, debug=True)
