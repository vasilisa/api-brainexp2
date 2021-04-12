import warnings
import subprocess
from flask_cors import CORS
from flask import Flask, jsonify, request, abort, Response, make_response, render_template 

import os
from models.db import db
from models.install import install_models


warnings.filterwarnings("ignore")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pwd@localhost/brainexptwo'
db.init_app(app)
CORS(app)

with app.app_context():
    install_models()
    import routes

@app.route('/<pagename>')
def regularpage(pagename=None):
    
    """
        Important!: you need this part to make the sequential page working via showpages! 
    """
    if pagename==None:
        raise ExperimentError('page_not_found')
    return render_template(pagename)

@app.route('/app', methods=['GET', 'POST'])
def myapp():
    cpath = os.getcwd()
    print ("The current working directory is %s" % cpath)
    result = dict()
    # Add Goolge Cloud Storage service to transfer the data to the GCloud 
    return jsonify(result), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port,debug=True)

