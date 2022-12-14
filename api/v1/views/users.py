#!/usr/bin/python3
<<<<<<< HEAD
"""
View for User objects that handles
all default RESTFul API actions
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User
from flasgger import swag_from


@app_views.route("/users", methods=["GET"], strict_slashes=False)
@swag_from('swagger/users/all_users.yml')
def all_users():
    """Method that retrieves the list of all User objects"""
    users = storage.all(User)
    all_users = [user.to_dict() for user in users.values()]
    return jsonify(all_users)


@app_views.route("/users/<user_id>", methods=["GET"],
                 strict_slashes=False)
@swag_from('swagger/users/one_user.yml')
def user_by_id(user_id):
    """Method that retrieves a User object by id"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", methods=["DELETE"],
                 strict_slashes=False)
@swag_from('swagger/users/del_user.yml')
def delete_user_by_id(user_id):
    """Method that deletes a User object by id"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route("/users", methods=["POST"], strict_slashes=False)
@swag_from('swagger/users/new_user.yml')
def create_user():
    """Method that creates a User object"""
    json = request.get_json()
    if not json:
        return "Not a JSON", 400
    if not json.get("email"):
        return "Missing email", 400
    if not json.get("password"):
        return "Missing password", 400

    user = User(**json)
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201


@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
@swag_from('swagger/users/update_user.yml')
def update_user(user_id):
    """Method that updates a User object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    json = request.get_json()
    if not json:
        return "Not a JSON", 400

    not_allowed = ["id", "email", "created_at", "updated_at"]
    for key, value in json.items():
        if key not in not_allowed:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200
=======
"""Module with the view for Users objects"""
from api.v1.views import app_views
from models.user import User
from models import storage
from flask import request, abort, jsonify


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def users():
    """Return a list of dictionaries of all users"""
    if request.method == 'GET':
        users = []
        for user in storage.all(User).values():
            users.append(user.to_dict())
        return jsonify(users)
    data = request.get_json()
    if data is None:
        return 'Not a JSON', 400
    if 'email' not in data.keys():
        return 'Missing email', 400
    if 'password' not in data.keys():
        return 'Missing password', 400
    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def user_id(user_id):
    """Get a user instance from the storage"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(user.to_dict())
    if request.method == 'DELETE':
        user.delete()
        storage.save()
        return jsonify({}), 200
    if request.method == 'PUT':
        data = request.get_json()
        if data is None:
            return 'Not a JSON', 400
        for k, v in data.items():
            if k != 'id' or k != 'email' or k != 'created_at'\
               or k != 'updated_at':
                setattr(user, k, v)
        storage.save()
        return jsonify(user.to_dict()), 200
>>>>>>> 3ea81942a4d2a6d6f1885268a6a61619f36b27ae
