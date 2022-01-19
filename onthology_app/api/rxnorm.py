import pandas as pd
from collections import OrderedDict
from flask import request,Response
import requests
#import simplejson as json
import spacy
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.metrics.pairwise import cosine_similarity
import werkzeug
import os
from werkzeug.utils import secure_filename
import time
import uuid

from flask_restful import Resource, reqparse, fields, marshal_with
from onthology_app.rxnorm import get_details_from_code

from onthology_app.status.messages import messages
from onthology_app import Serializer
from flask import g
import sys


parser = reqparse.RequestParser()
parser.add_argument("file", required=True, type=werkzeug.datastructures.FileStorage, location = 'files', help=messages["no-file-help"]["message"])
parser.add_argument("emailid", required=True, help=messages["no-email-help"]["message"])

class RxNormCodeInfo(Resource):

    def post(self, rxnormcode):

        try:

            rxnormdata = get_details_from_code(rxnormcode)
            return rxnormdata

        except KeyError:

            return {"error": messages["no-auth-token"]}



