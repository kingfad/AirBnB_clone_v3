#!/usr/bin/python3
<<<<<<< HEAD
"""
View for Review object
that handles all default
RESTFul API actions
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review
from models.user import User
from flasgger import swag_from


@app_views.route("/places/<place_id>/reviews",
                 methods=["GET"],
                 strict_slashes=False)
@swag_from('swagger/reviews/all_reviews.yml')
def all_reviews(place_id):
    """
    Method that get all reviews of Place
    that match with passed place_id
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    all_reviews = storage.all(Review)
    reviews = [review.to_dict() for review in all_reviews.values()
               if review.place_id == place.id]

    return jsonify(reviews)


@app_views.route("/reviews/<review_id>",
                 methods=["GET"],
                 strict_slashes=False)
@swag_from('swagger/reviews/one_review.yml')
def get_review(review_id):
    """Method that get Review with specific id"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route("/reviews/<review_id>",
                 methods=["DELETE"],
                 strict_slashes=False)
@swag_from('swagger/reviews/del_review.yml')
def delete_review(review_id):
    """Method that deletes Review with specific id"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route("/places/<place_id>/reviews",
                 methods=["POST"],
                 strict_slashes=False)
@swag_from('swagger/reviews/new_review.yml')
def create_review(place_id):
    """Method that creates new Review for place with specific id"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    json = request.get_json()
    if not json:
        return "Not a JSON", 400
    if not json.get("user_id"):
        return "Missing user_id", 400
    if not json.get("text"):
        return "Missing text", 400

    user = storage.get(User, json.get("user_id"))
    if not user:
        abort(404)

    json["place_id"] = place.id

    review = Review(**json)
    storage.new(review)
    storage.save()

    return jsonify(storage.get(Review, review.id).to_dict()), 201


@app_views.route("/reviews/<review_id>",
                 methods=["PUT"],
                 strict_slashes=False)
@swag_from('swagger/reviews/update_review.yml')
def update_review(review_id):
    """Method that updates Review with specific id"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)

    json = request.get_json()
    if not json:
        return "Not a JSON", 400

    exceptions = ["id", "user_id", "place_id", "created_at", "updated_at"]

    for key, value in json.items():
        if key not in exceptions:
            setattr(review, key, value)

    storage.save()
    return jsonify(storage.get(Review, review.id).to_dict()), 200
=======
"""Module with the view for Review objects"""
from api.v1.views import app_views
from models.review import Review
from models.place import Place
from models.city import City
from models.user import User
from models import storage
from flask import request, abort, jsonify


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'],
                 strict_slashes=False)
def reviews(place_id):
    """Return a list of dictionaries of all reviews for a place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if request.method == 'GET':
        reviews = []
        for review in place.reviews:
            reviews.append(review.to_dict())
        return jsonify(reviews)
    data = request.get_json()
    if data is None:
        return 'Not a JSON', 400
    if 'user_id' not in data.keys():
        return 'Missing user_id', 400
    user = storage.get(User, data.get('user_id'))
    if user is None:
        abort(404)
    if 'text' not in data.keys():
        return 'Missing text', 400
    data['place_id'] = place_id
    new_review = Review(**data)
    new_review.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_review(review_id):
    """Get a review instance from the storage"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(review.to_dict())
    if request.method == 'DELETE':
        review.delete()
        storage.save()
        return jsonify({}), 200
    if request.method == 'PUT':
        data = request.get_json()
        if data is None:
            return 'Not a JSON', 400
        for k, v in data.items():
            if k != 'id' or k != 'user_id' or k != 'place_id'\
               or k != 'created_at' or k != 'updated_at':
                setattr(review, k, v)
        storage.save()
        return jsonify(review.to_dict()), 200
>>>>>>> 3ea81942a4d2a6d6f1885268a6a61619f36b27ae
