from flask_restx import Namespace, Resource


ns = Namespace("api")



@ns.route("/hello")
class Test(Resource):
    def get(self):
        return {"hello": "flask restx"}