# Flask settings
#FLASK_SERVER_NAME = '0.0.0.0:80'
FLASK_SERVER_NAME = '0.0.0.0:5556'
FLASK_DEBUG = False  # Do not use debug mode in production
CELERY_BROKER_URL_DOCKER= 'amqp://admin:mypass@rabbit:5672/'
CELERY_BROKER_URL_LOCAL  = 'amqp://localhost/'
CELERY_BROKER_URL = CELERY_BROKER_URL_DOCKER
CELERY_ALWAYS_EAGER = False
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
RPC_Q = 'rpc_queue_CM_compute'
TIMEOUT_ALIVE_CM = 3
TIMEOUT_START_CM = 1
TIMEOUT_DELETE_CM= 15
RPC_CM_ALIVE= 'rpc_queue_CM_ALIVE'
PORT_LOCAL = 5000
PORT_DOCKER = 80
CM_REGISTER_Q = 'rpc_queue_CM_register'
PORT = PORT_LOCAL
CM_DB_NAME = "calculation_module.db"
# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
RESTPLUS_JSON = {
    'separators': (',', ':')
}

CORS_HEADER_API_KEY = 'av7e7d78f93e2af'
CORS_ORIGIN = 'http://hotmaps.hevs.ch'
CORS_CREDENTIALS = False
"""CORS_HEADERS = (
    CORS_HEADER_API_KEY,
    'X-Fields',
    'Content-Type',
    'Accept',
    'Accept-Charset',
    'Accept-Language',
    'Cache-Control',
    'Content-Encoding',
    'Content-Length',
    'Content-Security-Policy',
    'Content-Type',
    'Cookie',
    'ETag',
    'Host',
    'If-Modified-Since',
    'Keep-Alive',
    'Last-Modified',
    'Origin',
    'Referer',
    'User-Agent',
    'X-Forwarded-For',
    'X-Forwarded-Port',
    'X-Forwarded-Proto'
)"""

# SQLAlchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
CRS = 3035
# Duration curve constants used in heat.load.profile.py
HOURS_PER_YEAR = 8760
LIMIT_VALUES_PER_NUTS = 4000
POINTS_FIRST_GROUP_PERCENTAGE = 0.0228
POINTS_SECOND_GROUP_PERCENTAGE = 0.1141
POINTS_THIRD_GROUP_PERCENTAGE = 0.7207
POINTS_FOURTH_GROUP_PERCENTAGE = 0.1424
POINTS_FIRST_GROUP_STEP = 12
POINTS_SECOND_GROUP_STEP = 40
POINTS_THIRD_GROUP_STEP = 134
POINTS_FOURTH_GROUP_STEP = 39

# heat load and duration curve data options
NUMBER_DECIMAL_DATA = 2

# All repositories
POPULATION_TOT = 'pop_tot_curr_density_tif'
HEAT_DENSITY_TOT = 'heat_tot_curr_density_tif'
HEAT_DENSITY_NON_RES = 'heat_nonres_curr_density_tif'
HEAT_DENSITY_RES = 'heat_res_curr_density_tif'
WWTP = 'wwtp'
WWTP_CAPACITY = 'wwtp_capacity'
WWTP_POWER = 'wwtp_power'
GRASS_FLOOR_AREA_TOT = 'gfa_tot_curr_density_tif'
GRASS_FLOOR_AREA_RES = 'gfa_res_curr_density_tif'
GRASS_FLOOR_AREA_NON_RES = 'gfa_nonres_curr_density_tif'
BUILDING_VOLUMES_RES = 'vol_res_curr_density_tif'
BUILDING_VOLUMES_TOT = 'vol_tot_curr_density_tif'
BUILDING_VOLUMES_NON_RES = 'vol_nonres_curr_density_tif'
INDUSTRIAL_SITES = 'industrial_database'
INDUSTRIAL_SITES_EMISSIONS = 'industrial_database_emissions'
INDUSTRIAL_SITES_EXCESS_HEAT = 'industrial_database_excess_heat'
BIOMASS_POTENTIAL = 'potential_biomass'
MUNICIPAL_SOLID_WASTE = 'potential_municipal_solid_waste'
WIND_POTENTIAL = 'potential_wind'
SOLAR_POTENTIAL = 'solar_optimal_total'
GEOTHERMAL_POTENTIAL_HEAT_COND = 'potential_shallowgeothermal_heat_cond'
ELECRICITY_CO2_EMISSION_FACTOR = 'yearly_co2_emission'
HDD_CUR = 'hdd_curr_tif'
CDD_CUR = 'cdd_curr_tif'
ELECRICITY_MIX = 'stat.yearly_electricity_generation_mix'

_TOT = 'pop_tot_curr_density'

# All layers references for queries
LAYERS_REF_ALL = [
    POPULATION_TOT,
    HEAT_DENSITY_TOT,
    HEAT_DENSITY_NON_RES,
    HEAT_DENSITY_RES,
    WWTP,
    GRASS_FLOOR_AREA_TOT,
    GRASS_FLOOR_AREA_RES,
    GRASS_FLOOR_AREA_NON_RES,
    BUILDING_VOLUMES_RES,
    BUILDING_VOLUMES_TOT,
    BUILDING_VOLUMES_NON_RES,
    INDUSTRIAL_SITES,
    INDUSTRIAL_SITES_EMISSIONS,
    INDUSTRIAL_SITES_EXCESS_HEAT,
    BIOMASS_POTENTIAL,
    MUNICIPAL_SOLID_WASTE,
    WIND_POTENTIAL,
    SOLAR_POTENTIAL,
    GEOTHERMAL_POTENTIAL_HEAT_COND,
    WWTP_CAPACITY,
    WWTP_POWER,
    ELECRICITY_CO2_EMISSION_FACTOR,
    HDD_CUR,
    CDD_CUR,
]

LAYERS_REF_HECTARES = [
    POPULATION_TOT,
    HEAT_DENSITY_TOT,
    HEAT_DENSITY_NON_RES,
    HEAT_DENSITY_RES,
    GRASS_FLOOR_AREA_TOT,
    GRASS_FLOOR_AREA_RES,
    GRASS_FLOOR_AREA_NON_RES,
    WWTP,
    INDUSTRIAL_SITES_EMISSIONS,
    INDUSTRIAL_SITES_EXCESS_HEAT,
    BUILDING_VOLUMES_RES,
    BUILDING_VOLUMES_TOT,
    BUILDING_VOLUMES_NON_RES,
    WWTP_CAPACITY,
    WWTP_POWER,
    SOLAR_POTENTIAL,
    GEOTHERMAL_POTENTIAL_HEAT_COND,
    HDD_CUR,
    CDD_CUR,
]

LAYERS_REF_HECTARES_TABLE = [
    POPULATION_TOT,
    HEAT_DENSITY_TOT,
    HEAT_DENSITY_NON_RES,
    HEAT_DENSITY_RES,
    WWTP,
    GRASS_FLOOR_AREA_TOT,
    GRASS_FLOOR_AREA_RES,
    GRASS_FLOOR_AREA_NON_RES,
    BUILDING_VOLUMES_RES,
    BUILDING_VOLUMES_TOT,
    BUILDING_VOLUMES_NON_RES,
    SOLAR_POTENTIAL,
    INDUSTRIAL_SITES_EMISSIONS,
    INDUSTRIAL_SITES_EXCESS_HEAT,
    BUILDING_VOLUMES_NON_RES,
    WWTP_CAPACITY,
    WWTP_POWER,
    GEOTHERMAL_POTENTIAL_HEAT_COND,
    HDD_CUR,
    CDD_CUR,
]

LAYERS_REF_NUTS = [
    POPULATION_TOT,
    HEAT_DENSITY_TOT,
    HEAT_DENSITY_RES,
    INDUSTRIAL_SITES_EMISSIONS,
    INDUSTRIAL_SITES_EXCESS_HEAT,
    GRASS_FLOOR_AREA_TOT,
    GRASS_FLOOR_AREA_RES,
    GRASS_FLOOR_AREA_NON_RES,
    BUILDING_VOLUMES_RES,
    BUILDING_VOLUMES_TOT,
    BUILDING_VOLUMES_NON_RES,
    WWTP_CAPACITY,
    WWTP_POWER,
    WWTP,
    SOLAR_POTENTIAL,
    GEOTHERMAL_POTENTIAL_HEAT_COND,
    ELECRICITY_CO2_EMISSION_FACTOR,
    HDD_CUR,
    CDD_CUR,
]

LAYERS_REF_LAU = [
    POPULATION_TOT,
    HEAT_DENSITY_TOT,
    HEAT_DENSITY_NON_RES,
    HEAT_DENSITY_RES,
    WWTP,
    BUILDING_VOLUMES_RES,
    BUILDING_VOLUMES_TOT,
    BUILDING_VOLUMES_NON_RES,
    GRASS_FLOOR_AREA_TOT,
    GRASS_FLOOR_AREA_RES,
    GRASS_FLOOR_AREA_NON_RES,
    SOLAR_POTENTIAL,
    BUILDING_VOLUMES_NON_RES,
    INDUSTRIAL_SITES_EMISSIONS,
    INDUSTRIAL_SITES_EXCESS_HEAT,
    WWTP_CAPACITY,
    WWTP_POWER,
    GEOTHERMAL_POTENTIAL_HEAT_COND,
    HDD_CUR,
    CDD_CUR,
]

LAYERS_REF_NUTS_TABLE = [
    POPULATION_TOT,
    HEAT_DENSITY_TOT,
    HEAT_DENSITY_RES,
    WWTP,
    GRASS_FLOOR_AREA_TOT,
    GRASS_FLOOR_AREA_RES,
    GRASS_FLOOR_AREA_NON_RES,
    BUILDING_VOLUMES_RES,
    BUILDING_VOLUMES_TOT,
    BUILDING_VOLUMES_NON_RES,
    MUNICIPAL_SOLID_WASTE,
    INDUSTRIAL_SITES,
    SOLAR_POTENTIAL,
    INDUSTRIAL_SITES_EMISSIONS,
    INDUSTRIAL_SITES_EXCESS_HEAT,
    INDUSTRIAL_SITES,
    WWTP_CAPACITY,
    WWTP_POWER,
    GEOTHERMAL_POTENTIAL_HEAT_COND,
    ELECRICITY_CO2_EMISSION_FACTOR,
    HDD_CUR,
    CDD_CUR,
]

LAYERS_REF_LAU_TABLE = [
    POPULATION_TOT,
    HEAT_DENSITY_TOT,
    HEAT_DENSITY_NON_RES,
    HEAT_DENSITY_RES,
    WWTP,
    GRASS_FLOOR_AREA_TOT,
    GRASS_FLOOR_AREA_RES,
    GRASS_FLOOR_AREA_NON_RES,
    BUILDING_VOLUMES_RES,
    BUILDING_VOLUMES_TOT,
    BUILDING_VOLUMES_NON_RES,
    MUNICIPAL_SOLID_WASTE,
    INDUSTRIAL_SITES_EMISSIONS,
    INDUSTRIAL_SITES_EXCESS_HEAT,
    WWTP_CAPACITY,
    WWTP_POWER,
    INDUSTRIAL_SITES,
    SOLAR_POTENTIAL,
    GEOTHERMAL_POTENTIAL_HEAT_COND,
    ELECRICITY_CO2_EMISSION_FACTOR,
    HDD_CUR,
    CDD_CUR,
]