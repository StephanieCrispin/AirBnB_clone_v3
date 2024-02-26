from flask import jsonify
from api.v1.views import app_views

app_views.route("/status", strict_slashes = False)
def return_status():
  jsonify({"status":"OK"})

  @app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stat_count():
    """ endpoint that retrieves the # of each objects by type """
    count_stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(count_stats)


if __name__ == "__main__":
    pass