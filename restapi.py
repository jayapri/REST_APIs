from flask import Flask, jsonify

app = Flask(__name__)


restaurants = [{'name': "Hyderabadi Biriyani House",
                'restaurant_id': "0",
                'Description': "Very Tasty Home made Biriyani available"
                               " for affordable price",
                'Location': "Missisauga",
                'Menu': "Visit hydbiriyani.com to know more"},
               {'name': "Madras Cafe",
                'restaurant_id': "1",
                'Description': "Very Tasty Home made Biriyani available"
                               " for affordable price",
                'Location': "Toronto",
                'Menu': "Visit madrascafe.com to know more"},
               {'name': "Kachigooda",
                'restaurant_id': "2",
                'Description': "Very Tasty Home made Biriyani available"
                               " for affordable price",
                'Location': "Oshawa",
                'Menu': "Visit kachigooda.com to know more"},
               {'name': "RR Biriyani",
                'restaurant_id': "3",
                'Description': "Very Tasty Home made Biriyani available"
                               " for affordable price",
                'Location': "Pickering",
                'Menu': "Visit rrbiriyani.com to know more"},
               {'name': "JK Biriyani",
                'restaurant_id': "4",
                'Description': "Very Tasty Home made Biriyani available"
                               " for affordable price",
                'Location': "Whitby",
                'Menu': "Visit jkbiriyani.com to know more"},
               {'name': "Salem Biriyani",
                'restaurant_id': "5",
                'Description': "Very Tasty Home made Biriyani available"
                               " for affordable price",
                'Location': "Ajax",
                'Menu': "Visit salembiriyani.com to know more"},
               {'name': "Madura Biriyani",
                'restaurant_id': "6",
                'Description': "Very Tasty Home made Biriyani available"
                               " for affordable price",
                'Location': "Scarborough",
                'Menu': "Visit madhurabiriyani.com to know more"},
               {'name': "Nilgiris Biriyani",
                'restaurant_id': "7",
                'Description': "Very Tasty Home made Biriyani available"
                               " for affordable price",
                'Location': "Brampton",
                'Menu': "Visit nilgirisbiriyani.com to know more"}]


@app.route('/')
def index():
    return "Welcome to restaurants"


@app.route("/restaurants", methods=['GET'])
def get():
    return jsonify({'restaurants': restaurants})


@app.route("/restaurants/<int:restaurant_id>", methods=['GET'])
def get_restaurant(restaurant_id):
    return jsonify({'restaurant': restaurants[restaurant_id]})


@app.route("/restaurants", methods=['POST'])
def create():
   restaurant = {'name': "Mad Biriyani",
                  'restaurant_id': "8",
                   'Description': "Very Tasty Home made Biriyani available"
                                   " for affordable price",
                   'Location': "Markham",
                   'Menu': "Visit madbiriyani.com to know more"}
   restaurants.append(restaurant)
   return jsonify({'created': restaurant})


@app.route("/restaurants/<int:restaurant_id>", methods=['PUT'])
def restaurant_update(restaurant_id):
    restaurants[restaurant_id]['Description'] = "ABC"
    return jsonify({'restaurant': restaurants[restaurant_id]})


@app.route("/restaurants/<int:restaurant_id>", methods=['DELETE'])
def delete(restaurant_id):
    restaurants.remove(restaurants[restaurant_id])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)

