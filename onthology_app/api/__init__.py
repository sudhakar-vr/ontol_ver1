from flask_restful import Api
from onthology_app.api.icd import CodeInfo,DescriptionInfo
from onthology_app.api.rxnorm import RxNormCodeInfo
from flask import g, request


def init_api(app):
    api = Api(app)


    api.add_resource(CodeInfo, '/api/icdcode/<string:icdcode>')

    api.add_resource(DescriptionInfo, '/api/icddesc/<string:description>')

    api.add_resource(RxNormCodeInfo, '/api/rxnormcode/<int:rxnormcode>')

