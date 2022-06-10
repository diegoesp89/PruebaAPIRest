import rest
import json
from simplexml import dumps
from flask import Flask, make_response
from flask_restful import Api


app = Flask(__name__)

api = Api(app)
app.logger.info('Starting')

@api.representation('application/json')
def output_json(data, code, headers=None):
	resp = make_response(json.dumps({'response' : data}), code)
	resp.headers.extend(headers or {})
	return resp

@api.representation('application/xml')
def output_xml(data, code, headers=None):
	resp = make_response(dumps({'response' : data}), code)
	resp.headers.extend(headers or {})
	return resp


api.add_resource(rest.Locales, '/api/v1/locales', "/")
api.add_resource(rest.NombreComuna, '/api/v1/locales/nombre_comuna/<string:nombre>')
api.add_resource(rest.IdLocal, '/api/v1/locales/local_id/<string:id>')
api.add_resource(rest.Fecha, '/api/v1/locales/fecha/<string:fecha>')
api.add_resource(rest.LocalidadNombre, '/api/v1/locales/localidad_nombre/<string:nombre>')
api.add_resource(rest.LocalDireccion, '/api/v1/locales/local_direccion/<string:direccion>')
api.add_resource(rest.HoraApertura, '/api/v1/locales/hora_apertura/<string:hora>')
api.add_resource(rest.HoraCierre, '/api/v1/locales/hora_cierre/<string:hora>')
api.add_resource(rest.LocalTelefono, '/api/v1/locales/local_telefono/<string:fono>')
api.add_resource(rest.LocalLat, '/api/v1/locales/local_lat/<string:lat>')
api.add_resource(rest.LocalLng, '/api/v1/locales/local_lng/<string:lng>')
api.add_resource(rest.FuncionamientoDia, '/api/v1/locales/funcionamiento_dia/<string:dia>')
api.add_resource(rest.FkRegion, '/api/v1/locales/fk_region/<string:id>')
api.add_resource(rest.FkComuna, '/api/v1/locales/fk_comuna/<string:id>')

if __name__ == "__main__":
	app.run(debug=True, port=5000)