#!/usr/bin/python3
'''
    RESTful API actions for City objects
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State,City

@app_views.route("/states/<state_id>/cities", methods=["GET"], strict_slashes=False)
def get_all_cities(state_id):
  """
  Gets all the city object and state id that matches
  """
  try:
    city_list = []
    state_list = storage.all("City")
    for key, value in state_list.items():
      value = value.to_dict()
      if value.get("state_id") == state_id:
        city_list.append(value)
    return jsonify(city_list)
  except BaseException:
    abort(404)

@app_views.route("/cities/<city_id>", methods=["GET"],strict_slashes=False)
def gets_a_city(city_id):
  """
  Gets a particular city
  """
  try:
    city = storage.get("City", city_id)
    return jsonify(city.to_dict())
  except Exception:
    abort(404)

@app_views.route("/cities/<city_id>", methods=['DELETE'], strict_slashes=False)
def deletes_a_city(city_id):
  """
  Deletes a particular city
  """
  try:
    city = storage.get("City", city_id)
    storage.delete(city)
    return jsonify({}),200
  except Exception:
    abort(404)

@app_views.route("/states/<state_id>/cities", methods=['POST'], strict_slashes=False)
def creates_a_city(state_id):
  """
  Creates a new city
  """
  state = storage.get("State", state_id)
  if not state:
    abort(404)
  if not request.json:
    abort(400)
    return jsonify({"error":"Not a JSON"})
  if name not in request.json:
    abort(400)
    return jsonify({"error":"Missing name"})

  n_city = City(**request.get_json())
  n_city.save()
  return jsonify(n_city.to_dict()),201

  @app_views.route("/cities/<city_id>", methods=["PUT"], strict_slashes=False)
  def put_city(city_id):
    """
    Updates a city
    """
    city = storage.get("City", city_id)
    if city is None:
      abort(404)
    if not request.json:
      return jsonify({'error':"Not a JSON"}),400
    for key, value in request.get_json().items():
      if key not in ['id', "created_at", "updated_at"]:
        setattr(city, key, value)
        
    city.save()
    return jsonify(city.to_dict()),200