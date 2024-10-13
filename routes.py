from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
from models import mongo, WebtoonSchema
from auth import jwt_required

webtoon_bp = Blueprint('webtoon', __name__)
webtoon_schema = WebtoonSchema()

@webtoon_bp.route('/webtoons', methods=['GET'])
def get_webtoons():
    webtoons = mongo.db.webtoons.find()
    result = [webtoon_schema.dump(webtoon) for webtoon in webtoons]
    return jsonify(result), 200

@webtoon_bp.route('/webtoons', methods=['POST'])
@jwt_required
def add_webtoon():
    data = request.json
    errors = webtoon_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    webtoon_id = mongo.db.webtoons.insert_one(data).inserted_id
    return jsonify({"message": "Webtoon added", "webtoon_id": str(webtoon_id)}), 201

@webtoon_bp.route('/webtoons/<webtoon_id>', methods=['GET'])
def get_webtoon(webtoon_id):
    webtoon = mongo.db.webtoons.find_one({"_id": ObjectId(webtoon_id)})
    if not webtoon:
        return jsonify({"error": "Webtoon not found"}), 404
    
    return jsonify(webtoon_schema.dump(webtoon)), 200

@webtoon_bp.route('/webtoons/<webtoon_id>', methods=['DELETE'])
@jwt_required
def delete_webtoon(webtoon_id):
    result = mongo.db.webtoons.delete_one({"_id": ObjectId(webtoon_id)})
    if result.deleted_count == 0:
        return jsonify({"error": "Webtoon not found"}), 404
    
    return jsonify({"message": "Webtoon deleted"}), 200
