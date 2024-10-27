from config.Mongo import mongo_connect

locals_property = mongo_connect['locales_venta']
locals_property_study = mongo_connect['locales_estudiados']


def get_property():
    local = locals_property.find()
    return list(local)

def get_study_property():
    local = locals_property_study.find()
    return list(local)