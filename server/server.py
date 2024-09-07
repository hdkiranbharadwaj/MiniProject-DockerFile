from flask import Flask
from flask_cors import CORS
import pickle
from flask import jsonify
from flask import request

app = Flask(__name__)
CORS(app) 

@app.route("/")
def members():
    return {'members':['Hello','World']}



@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["data"]
        print("Received data:", data)
        pickled_model = pickle.load(open('model.pkl', 'rb'))
        prediction = pickled_model.predict([data])
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)})




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# python3 server.py 3.11.9
# python3 -m pip install something
# npm start (for react)