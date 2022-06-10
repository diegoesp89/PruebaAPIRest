from flask import request
from flask import current_app as app
from flask_restful import Resource
import requests
import json


def get_initial_data():
    try:
        uri = "https://farmanet.minsal.cl/maps/index.php/ws/getLocalesRegion?id_region=7"
        uResponse = requests.get(uri)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    return json.loads(Jresponse)

data = get_initial_data()

class Locales(Resource):
	def get(self):
		return data

class NombreComuna(Resource):
    def get(self, nombre):
        return [d for d in data if (d['comuna_nombre'] == nombre.upper())]

class IdLocal(Resource):
    def get(self, id):
        return [d for d in data if (d['local_id'] == id)]

class Fecha(Resource):
    def get(self, fecha):
        return [d for d in data if (d['fecha'] == fecha)]

class LocalidadNombre(Resource):
    def get(self, nombre):
        return [d for d in data if (d['localidad_nombre'] == nombre.upper())]

class LocalDireccion(Resource):
    def get(self, direccion):
        return [d for d in data if (d['local_direccion'] == direccion.upper())]

class HoraApertura(Resource):
    def get(self, hora):
        return [d for d in data if (d['funcionamiento_hora_apertura'] == hora)]

class HoraCierre(Resource):
    def get(self, hora):
        return [d for d in data if (d['funcionamiento_hora_cierre'] == hora)]

class LocalTelefono(Resource):
    def get(self, fono):
        return [d for d in data if (d['local_telefono'] == fono)]

class LocalLat(Resource):
    def get(self, lat):
        return [d for d in data if (d['local_lat'] == lat)]

class LocalLng(Resource):
    def get(self, lng):
        return [d for d in data if (d['local_lng'] == lng)]

class FuncionamientoDia(Resource):
    def get(self, dia):
        return [d for d in data if (d['funcionamiento_dia'] == dia.lower())]

class FkRegion(Resource):
    def get(self, id):
        return [d for d in data if (d['fk_region'] == id)]

class FkComuna(Resource):
    def get(self, id):
        return [d for d in data if (d['fk_comuna'] == id)]
