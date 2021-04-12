"""users routes"""
from flask import current_app as app, jsonify, request

from models import ConfigDataFollowUp,BaseObject, db
from collections import OrderedDict
import numpy
from datetime import datetime
import json
import glob
from sqlalchemy.sql.expression import func


@app.route("/config_data_followup/last_participant_id", methods=["GET"])
def get_last_participant_id_followup():

    query  = db.db.session.query(func.max(ConfigDataFollowUp.participant_id)).first_or_404()

    if query[0] is not None:
        result = dict({"new_participant_id": str(int(query[0]) + 1)})
    else:
        result = dict({"new_participant_id": str(1)})

    return jsonify(result)

@app.route("/config_data_followup/create/<participant_id>/<prolific_id>", methods=["POST", "GET"])
def create_participant_followup(participant_id, prolific_id):
     content                        = request.json        
     participant                    = ConfigDataFollowUp()
     participant.participant_id     = int(participant_id)
     participant.prolific_id        = str(prolific_id)
     participant.date_time          = str(content['date_time'])
     
     BaseObject.check_and_save(participant)

     result = dict({"success": "yes"})    

     return jsonify(result)






