# Please Install 
# Flask==0.12.2: pip install Flask==0.12.2
# Postman HTTP Client: https://www.getpostman.com/

import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:

    def __init__(self):
        self.chain = []
        self.createblock(previoushash = '0',data="-1")

    def createblock(self, previoushash,data):
        block = {'index': len(self.chain) + 1,
                 'data':data,
                 'timestamp': str(datetime.datetime.now()),
                 'previoushash': previoushash}
        self.chain.append(block)
        return block

    def getpreviousblock(self):
        return self.chain[-1]

    def hash(self, block):
        encodedblock = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encodedblock).hexdigest()
    
    def ischainvalid(self, chain):
        previousblock = chain[0]
        blockindex = 1
        while blockindex < len(chain):
            block = chain[blockindex]
            if block['previoushash'] != self.hash(previousblock):
                return False
            previousblock = block
            blockindex += 1
        return True

app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain()

# Mining a new block
@app.route('/mineblock', methods = ['GET'])
def mineblock():
    previousblock = blockchain.getpreviousblock()
    previoushash = blockchain.hash(previousblock)
    
    
    #for demo purposes after sending request from post_man, 
    #use the python console to enter a dummy transaction to see the full mining
    
    data=input("enter transaction")
    
    
    block = blockchain.createblock(previoushash,data)
    response = {'message': 'New Transaction!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'data':data,
                'previoushash': block['previoushash']}
    return jsonify(response), 200

# Getting the full Blockchain
@app.route('/getchain', methods = ['GET'])
def getchain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Checking if the Blockchain is valid
@app.route('/isvalid', methods = ['GET'])
def isvalid():
    isvalid = blockchain.ischainvalid(blockchain.chain)
    if isvalid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200

# Running the app
app.run(host = '0.0.0.0', port = 5000)
