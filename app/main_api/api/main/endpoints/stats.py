import logging
import re
from flask import request
from flask_restplus import Resource
from main_api.api.main.serializers import stats_layers_area_input, stats_layers_output, stats_layers_hectares_output, stats_layers_nuts_input, stats_layers_nuts_output, stats_layer_point_input, stats_layers_area_nuts_input, stats_layers_hectares_input
from main_api.api.restplus import api
from main_api.models.wwtp import Wwtp, WwtpNuts3, WwtpLau2, WwtpNuts2, WwtpNuts1, WwtpNuts0
from main_api.models.heat_density_map import HeatDensityMap, HeatDensityHa, HeatDensityNuts3, HeatDensityLau2, HeatDensityNuts0, HeatDensityNuts1, HeatDensityNuts2
from main_api.models.population_density import PopulationDensityHa, PopulationDensityNuts3, PopulationDensityLau2, PopulationDensityNuts2, PopulationDensityNuts1,PopulationDensityNuts0
from main_api.models.nuts import Nuts, NutsRG01M
from main_api.models.lau import Lau
from main_api.models.hectare import LayersHectare 
from sqlalchemy import func, BigInteger, TypeDecorator
from main_api.models import db
import datetime
import shapely.geometry as shapely_geom
from geojson import FeatureCollection, Feature
from geoalchemy2.shape import to_shape



log = logging.getLogger(__name__)

ns = api.namespace('stats', description='Operations related to statistisdscs')

layers_ref = {
	'wwtp': Wwtp,
	'wwtp_nuts3': WwtpNuts3,
	'wwtp_nuts2': WwtpNuts2,
	'wwtp_nuts1': WwtpNuts1,
	'wwtp_nuts0': WwtpNuts0,
	'wwtp_ha': Wwtp,
	'wwtp_lau2': WwtpLau2,
	'population': PopulationDensityNuts3,
	'population_density_nuts3': PopulationDensityNuts3,
	'population_density_nuts2': PopulationDensityNuts2,
	'population_density_nuts1': PopulationDensityNuts1,
	'population_density_nuts0': PopulationDensityNuts0,
	'population_density_ha': PopulationDensityHa,
	'population_density_lau2': PopulationDensityLau2,
	'heat_density_map': HeatDensityMap,
	'heat_density_ha': HeatDensityHa,
	'heat_density_nuts3': HeatDensityNuts3,
	'heat_density_nuts2': HeatDensityNuts2,
	'heat_density_nuts1': HeatDensityNuts1,
	'heat_density_nuts0': HeatDensityNuts0,
	'heat_density_lau2': HeatDensityLau2,
}

@ns.route('/layers/area/')
@api.response(404, 'No data found for that specific area.')
class StatsLayersInArea(Resource):

	@api.marshal_with(stats_layers_output)
	@api.expect(stats_layers_area_input)
	def post(self):
		"""
		Returns the statistics for specific layers, area and year
		:return:
		"""
		year = api.payload['year']
		layers = api.payload['layers']
		points = api.payload['points']
		poly = shapely_geom.Polygon([[p['lng'], p['lat']] for p in points])
		geom = "SRID=4326;{}".format(poly.wkt)

		output = []

		# for each layer,
		# try to match layer name with layer class
		# run aggregate_for_selection method
		for layer in layers:
			try:
				a = layers_ref[layer]()
			except KeyError:
				continue

			output.append({
				'name': layer,
				'values': a.aggregate_for_selection(geometry=geom, year=year)
			})

		# compute heat consumption/person if both layers are selected
		pop_nuts_name = 'population_density_nuts3'
		heat_nuts_name = 'heat_density_nuts3'
		sf = StatsFunctions()

		if pop_nuts_name in layers and heat_nuts_name in layers:
			sf.computeConsPerPerson(pop_nuts_name, heat_nuts_name, output)

		# compute heat consumption/person if both layers are selected
		pop1ha_name = 'population_density_ha'
		hdm_name = 'heat_density_ha'

		if pop1ha_name in layers and hdm_name in layers:
			sf.computeConsPerPerson(pop1ha_name, hdm_name, output)

		# compute heat consumption/person if both layers are selected
		pop_lau_name = 'population_density_lau2'
		heat_lau_name = 'heat_density_lau2'

		if pop_lau_name in layers and heat_lau_name in layers:
			sf.computeConsPerPerson(pop_lau_name, heat_lau_name, output)

		# return feature collection
		# priority lau higher level first
		# then nuts higher level first
		nuts = None
		r = re.compile("^.*_nuts[0-3]$")
		nuts_layers = list(filter(r.match, layers))
		if nuts_layers != None and hasattr(nuts_layers, '__len__') and len(nuts_layers) > 0:
			nuts_levels = []
			for l in nuts_layers:
				try:
					nuts_levels.append(int(re.search("^.*nuts([0-3])$", l).group(1)))
				except (AttributeError, ValueError):
					pass

			nuts = NutsRG01M.nuts_in_geometry(geometry=geom, year=year, nuts_level=max(nuts_levels))

		r = re.compile("^.*_lau[0-3]$")
		lau_layers = list(filter(r.match, layers))
		if lau_layers != None and hasattr(lau_layers, '__len__') and len(lau_layers) > 0:
			levels = []
			for l in lau_layers:
				try:
					levels.append(int(re.search("^.*lau([0-3])$", l).group(1)))
				except (AttributeError, ValueError):
					pass

			nuts = Lau.nuts_in_geometry(geometry=geom, year=2013, level=max(levels))

		return {
			"layers": output,
			"feature_collection": nuts
		}


@ns.route('/layers/nuts/')
@api.response(404, 'No data found for that specific list of NUTS.')
class StatsLayersNutsInArea(Resource):
	@api.marshal_with(stats_layers_nuts_output)
	@api.expect(stats_layers_nuts_input)
	def post(self):
		"""
		Returns the statistics for specific layers, area and year
		:return:
		"""
		year = api.payload['year']
		layers = api.payload['layers']
		nuts = api.payload['nuts']


		# compute nuts level
		nuts_level = 0
		for n in nuts:
			if len(n)-2 > nuts_level:
				nuts_level = len(n)-2

		output = []

		# for each layer,
		# try to match layer name with layer class
		# run aggregate_for_selection method
		for layer in layers:
			try:
				a = layers_ref[layer]()
			except KeyError:
				continue

			output.append({
				'name': layer,
				'values': a.aggregate_for_nuts_selection(nuts=nuts, year=year)
			})

		# compute heat consumption/person if both layers are selected
		pop_nuts_name = 'population_density_nuts3'
		heat_nuts_name = 'heat_density_nuts3'
		sf = StatsFunctions()

		if pop_nuts_name in layers and heat_nuts_name in layers:
			sf.computeConsPerPerson(pop_nuts_name, heat_nuts_name, output)

		# compute heat consumption/person if both layers are selected
		pop_lau_name = 'population_density_lau2'
		heat_lau_name = 'heat_density_lau2'

		if pop_lau_name in layers and heat_lau_name in layers:
			sf.computeConsPerPerson(pop_lau_name, heat_lau_name, output)

		# output
		return {
			"layers": output,
		}

@ns.route('/layers/hectares/multi')
@api.response(404, 'No data found for that specific area.')
class StatsLayersHectareMulti(Resource):
	@api.marshal_with(stats_layers_hectares_output)
	@api.expect(stats_layers_hectares_input)
	def post(self):
		"""
		Returns the statistics for specific layers, hectares and year
		:return:
		"""
		# Entrees
		year = api.payload['year']
		layers = api.payload['layers']        
		areas = api.payload['areas']

		polyArray = []
		output = []

		# convert to polygon format for each polygon and store them in polyArray
		for polygon in areas: 
			po = shapely_geom.Polygon([[p['lng'], p['lat']] for p in polygon['points']])
			polyArray.append(po)
		


		# convert array of polygon into multipolygon
		multipolygon = shapely_geom.MultiPolygon(polyArray)

		#geom = "SRID=4326;{}".format(multipolygon.wkt)
		geom = multipolygon.wkt

		res = LayersHectare.aggregate_for_selection(geometry=geom, year=year, layers=layers)
		output = res

		# compute heat consumption/person if both layers are selected
		pop1ha_name = 'population_density_ha'
		hdm_name = 'heat_density_ha'
		sf = StatsFunctions()

		if pop1ha_name in layers and hdm_name in layers:
			sf.computeConsPerPerson(pop1ha_name, hdm_name, output)

		#output
		return {
			"layers": output,
		}

class StatsFunctions():
	def computeConsPerPerson(self, l1, l2, output):
		"""
		Compute the heat consumption/person if population_density and heat_density layers are selected
		"""
		hdm = None
		heat_cons = None
		population = None

		for l in output:
			if l.get('name') == l2:
				hdm = l
				for v in l.get('values', []):
					if v.get('name') == 'heat_consumption':
						heat_cons = v
			if l.get('name') == l1:
				for v in l.get('values', []):
					if v.get('name') == 'population':
						population = v

		if heat_cons != None and population != None:
			pop_val = float(population.get('value', 1))
			pop_val = pop_val if pop_val > 0 else 1
			hea_val = float(heat_cons.get('value', 0))

			v = {
				'name': 'consumption_per_citizen',
				'value': hea_val / pop_val,
				'unit': heat_cons.get('unit') + '/' + population.get('unit')
			}

			hdm.get('values').append(v)

		return hdm