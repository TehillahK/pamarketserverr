# Pa Market backend code starter
#  written by Tehillah Kangamba
# all database stuff is famerpersitance package
from flask_restful.utils import cors

from farmlogic import FarmsSingleton

from flask import Flask, request, render_template, abort, jsonify

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# used to get a farm , add a farm and remove one
class Farm(Resource):
    @cors.crossdomain(origin='*')
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
        return result


#  Used to get all farms
class Farms(Resource):
    @cors.crossdomain(origin='*')
    def get(self):
        result = None
        db = FarmsSingleton("te", "hill")
        result = db.get_all_farms()
        print(result)
        result = jsonify(result)
        return result


@app.route('/farm')
def farm_page():
    return render_template("farm.html")


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


api.add_resource(Farms, "/api/farms")
api.add_resource(Farm, "/api/farm")

api.add_resource(Crops, "/api/crops")
if __name__ == '__main__':
    # initiliaze database

    app.run()
