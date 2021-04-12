"""users routes"""
from flask import current_app as app, jsonify, request

from models import AttemptsFollowUp, BaseObject, db
from collections import OrderedDict
import json
import glob
from sqlalchemy.sql.expression import func


@app.route("/attempts_followup/save_followup/<participant_id>/<prolific_id>", methods=["POST", "GET"])
def save_followup(participant_id, prolific_id):
     content                        = request.json 
            
     participant                    = AttemptsFollowUp()
     participant.participant_id     = int(participant_id)
     participant.prolific_id        = str(prolific_id)
     participant.date_time          = str(content['date_time']) # start of the game 
     participant.date_time_end      = str(content['date_time_end']) # end of the game 
     participant.log_type           = str(content['log_type']) # either game or the questionnaire
     participant.log                = dict(content['log']) # all data as 1 JSON from all the sessions 
     

     app.logger.info(participant)
     BaseObject.check_and_save(participant)

     result = dict({"success": "yes"})    
     return jsonify(result)



