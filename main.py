from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Cristian": "+5255352121", 
                    "Jouse Perez": "+525512345678",
                    "Jaime Rodriguez" : "+525534152819", 
                    "James Bond" : "+525561829301"
                   })


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
