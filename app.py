# Pa Market backend code starter
#  written by Tehillah Kangamba
# all database stuff is famerpersitance package
import json

from flask_restful.utils import cors

from logic.farmlogic import FarmsSingleton

from flask import Flask, request, render_template, abort

from flask_restful import Resource, Api, reqparse
from flask_caching import Cache

from logic.userslogic import UsersSingleton

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)
api = Api(app)

parser = reqparse.RequestParser()


class Users(Resource):
    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def get(self):
        result = None
        db = UsersSingleton()
        users = db.get_all_users()
        if users is None:
            abort(404, "could not find users in database")
        result = users
        return result

    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def post(self):
        data = request.get_json(force=True)
        print(data)
        try:
            email = data["email"]
            if len(data) == 1:
                db = UsersSingleton()

                user = db.get_user(email)

                if user is None:
                    abort(404, "could not find user in database")
                result = user
            else:
                db = UsersSingleton()
                query={"email":email}
                result = db.update_user(query,data)
        except json.decoder.JSONDecodeError:
            print("failed")
            abort(404, "could not find user in database")
        return result


# used to get a farm , add a farm and remove one
class Farm(Resource):
    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def get(self):
        result = None
        args = request.args
        args = args.to_dict()
        if len(args) == 1 and "id" in args.keys():
            db = FarmsSingleton("te", "hill")
            id = args["id"]
            farm = db.get_farm(id)
            if farm is None:
                abort(404, "could not find farm in database")
            result = farm
        else:
            abort(400, "invalid request made to farms")
        return result


class Crops(Resource):
    @cors.crossdomain(origin='*')
    def get(self):
        args = request.args
        args = args.to_dict()
        if len(args) == 1 and "id" in args.keys():
            db = FarmsSingleton("te", "hill")
            id = args["id"]
            crops = db.get_crops(id)
            if crops is None:
                abort(404, "This farm doesnt exist in the system")
            result = crops
        else:
            abort(400, "invalid request made to farms")

        print(result)
        return result


#  Used to get all farms
class Farms(Resource):
    @cors.crossdomain(origin='*')
    @cache.cached(timeout=60)
    def get(self):
        result = None
        db = FarmsSingleton("te", "hill")
        result = db.get_all_farms()
        # result = jsonify(result)
        return result


@app.route('/farm')
def farm_page():
    return render_template("farm.html")


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


api.add_resource(Users, "/api/users")
api.add_resource(Farms, "/api/farms")
api.add_resource(Farm, "/api/farm")

api.add_resource(Crops, "/api/crops")
if __name__ == '__main__':
    # initiliaze database

    app.run(host='0.0.0.0', port=8080, threaded=True)
