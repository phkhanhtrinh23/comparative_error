from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from comparative import ComparativeError

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class ComparativeForm(Resource):
    def post(self):
        req = request.json
        obj = ComparativeError()
        res = obj.run(req['text'])

        print(res)
        return {
            'IsSuccessed': True,
            'Message': 'Success',
            'ResultObj':{
                'src': req['text'],
                'result': res
            }
        }

api.add_resource(ComparativeForm, '/api/comparative/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8014)