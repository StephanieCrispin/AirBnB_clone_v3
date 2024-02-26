#!/usr/bin/python3
'''
    RESTful API actions for State objects
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State

@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_all_states():
  """
  Gets a list of all the states
  """
  state_obj = []
  for state in storage.all("State").values():
    state_obj.append(state.to_dict())
    return jsonify(state_obj)

@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_one_state(state_id):
  """
  Gets a list of a single state
  """
  try:
    state = storage.get("state", state_id)
    return jsonify(state.to_dict())
  except:
    abort(404)

@app_views.route("/states/<state_id", methods=["DELETE"], strict_slashes=False)
def deletes_one_state(state_id):
  """
  Deletes a list of a single state
  """

  try:
    state = storage.delete("states", state_id)
    return jsonify({}),200
  except:
    abort(404)

@app_views.route("/states", methods=["POST"], strict_slashes=False)
def creates_one_state():
  """
  Creates a new state
  """

  if not request.json:
    abort(400)
    return jsonify({"error":"Not a JSON"})
  if name not in request.json:
    abort(400)
    return jsonify({"error":"Missing name"})
  
  n_state = State(**request.get_json())
  n_state.save()
  return jsonify(state.to_dict()),201

@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
  state = storage.get(state, state_id)
  if state is None:
    abort(400)
  if not request.json:
    return jsonify({"error":"Not a JSON"}),400
  for key,value in request.get_json().items:
    if key not in ["id", "createe_at", "updated_at"]:
      setattr(state, key, value)
    state.save()
  return jsonify(state.to_dict())