from datetime import date

import boundaries

def valid_ward(feature):
    if feature.get('WARD') != 'OUT':
        return True
    return False

def ocd_id_func(feature):
    return 'ocd-division/country:us/state:il/place:chicago/ward:{0}'.format(feature.get('WARD'))

def ward_namer(feature):
    return 'chicago-ward-{0}'.format(feature.get('WARD'))

boundaries.register('chicago-wards-2003',  
    file='',
    last_updated=date(2015, 4, 2),
    name='Chicago Wards 2003',
    singular='Chicago Ward 2003',
    domain='Chicago',
    authority='City of Chicago',
    source_url='https://data.cityofchicago.org/api/geospatial/xt4z-bnwh?method=export&format=Original',
    licence_url='',
    start_date=date(2003,5,1),
    end_date=date(2015,4,30),
    notes='',
    name_func=ward_namer,
    id_func=ocd_id_func,
    is_valid_func=valid_ward,
    label_point_func=lambda feature: None,
)

