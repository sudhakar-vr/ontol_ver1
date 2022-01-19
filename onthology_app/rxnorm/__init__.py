import pandas as pd
import requests
from collections import OrderedDict

from onthology_app import Serializer

from onthology_app.status.messages import messages

import os
import json
from datetime import datetime,timezone
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import smtplib, ssl,email
import csv
import spacy
from flask import current_app


def convert_df_to_json(df):

    code = str(df['OCode'].unique().flat[0])
    description_list = df['ODescription'].to_list()
    return  {
        "code" : code,
        "description" : description_list
    }

def get_details_from_code(rxnormcode):

    header = {'Accept': 'application/json'}
    inputrxnormcode = rxnormcode
    local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    train_data = pd.read_csv(local_path + "/static/RXNorm_Data_Test.csv", encoding='unicode_escape')

    rslt_df = train_data[train_data['OCode'] == inputrxnormcode]

    print("result dataframe")
    print(rslt_df)

    if rslt_df.empty:

        base_url='https://rxnav.nlm.nih.gov/REST/rxcui/'

        get_data_from_api =requests.get(base_url+str(inputrxnormcode)+'.json',headers=header)

        json_output = json.loads(get_data_from_api.text)
        #print("check which values are present in keys")
        ##print(json_output.keys())
        #print(json_output)
        #print(json_output['idGroup'])
        #print(type(json_output['idGroup']))
        #print(json_output['idGroup'].keys())
        #print(json_output['idGroup']['name'])
        if ("name" in json_output['idGroup'].keys()):
            return {
                "Code" : inputrxnormcode,
                "Description" : json_output['idGroup']['name']
            }
    else:
        val = convert_df_to_json(rslt_df)
        return val







