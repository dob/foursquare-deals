from hyperpublic import Hyperpublic
from settings import HYPERPUBLIC_CONFIG

def offers_near(lat,lon):
	hp = Hyperpublic(
		client_id=HYPERPUBLIC_CONFIG['client_id'],
		client_secret = HYPERPUBLIC_CONFIG['client_secret'],
	)
	deals = hp.offers.find(lat=lat,lon=lon,radius=1,type='deal',limit=5)
	events = hp.offers.find(lat=lat,lon=lon,radius=1,type='event',limit=5)
	offers = deals + events
	return offers
