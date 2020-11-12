from flask import Blueprint, jsonify, abort, request, json
from api.views import appblueprint


@appblueprint.route('/flutterwave/', methods=['POST'])
def add_user():
    """Receives a post request from http://127.0.0.1:5000/v2/api/flutterwave/ """

    user_input = request.json
    return jsonify({"message": user_input })