import pandas as pd
from collections import OrderedDict
from serpapi import GoogleSearch
from flask import request,Response
import spacy
import werkzeug
import os
from werkzeug.utils import secure_filename
import time
import uuid
from flask_restful import Resource, reqparse, fields, marshal_with
from onthology_app.icd import get_details_from_code,get_details_from_description,process_data_in_csv_file,allowed_file_types,update_database,get_job_status_by_id
from onthology_app.status.messages import messages
from onthology_app import Serializer
from flask import g
import sys

parser = reqparse.RequestParser()
# default location is flask.Request.values and flask.Request.json
# check help text careful it must be string
parser.add_argument("file", required=True, type=werkzeug.datastructures.FileStorage, location = 'files', help=messages["no-file-help"]["message"])
parser.add_argument("emailid", required=True, help=messages["no-email-help"]["message"])


class CodeInfo(Resource):

    def post(self,icdcode):

        try:
            icddata = get_details_from_code(icdcode)
            return icddata

        except KeyError:
            return {"error": messages["no-auth-token"]}

class DescriptionInfo(Resource):

    def get(self,description):

        try:

            icddata,df = get_details_from_description(description)
            return icddata

        except KeyError:
            return {"error": messages["no-auth-token"]}
