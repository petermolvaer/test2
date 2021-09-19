# imports
from flask import Flask
from flask_restful import Api
from resources.items import Items

# initialization

app = Flask(__name__)
app.config["PROPOGATE_EXCEPTIONS"] = True
api = Api(app)

# endpoints
api.add_resource(Items, "/items")

# execution
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
