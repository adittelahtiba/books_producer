from app import app, mongo, jsonify, request
from flask_jwt_extended import jwt_required

# kafka
import json
from flask_cors import CORS
from kafka import KafkaConsumer, KafkaProducer

# kafka event
TOPIC_NAME = "ADITYA-EMAILNA"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    api_version=(0, 11, 15)
)

@app.route('/',methods=['GET'])
def appawal():
    return {"aditya":"Pangestu"}

@app.route('/kafka', methods=['POST'])
def kafkaProducer():

    req = request.get_json()
    json_payload = json.dumps(req)
    json_payload = str.encode(json_payload)
    # push data into INFERENCE TOPIC
    producer.send(TOPIC_NAME, json_payload)
    producer.flush()
    print("Sent to consumer")
    return jsonify({
        "message": "You will receive an email in a short while with the plot",
        "status": "Pass"})