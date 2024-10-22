from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://andrew:n510zc3XB83ckQb5@cluster0.wkhn2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.code_challenges  # Use the database you created

@app.route('/upload_challenge', methods=['POST'])
def upload_challenge():
    challenge = {
        "title": request.json['title'],
        "description": request.json['description'],
        "date_created": request.json['date_created'],
    }
    result = db.challenges.insert_one(challenge)
    return jsonify({"status": "Challenge uploaded", "id": str(result.inserted_id)})

@app.route('/submit_solution', methods=['POST'])
def submit_solution():
    submission = {
        "challenge_id": request.json['challenge_id'],
        "user_id": request.json['user_id'],
        "submission": request.json['submission'],
        "date_submitted": request.json['date_submitted']
    }
    result = db.submissions.insert_one(submission)
    return jsonify({"status": "Submission received", "id": str(result.inserted_id)})

if __name__ == '__main__':
    app.run(debug=True)
