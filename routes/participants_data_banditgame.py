"""users routes"""
from flask import current_app as app, jsonify, request

from models import ParticipantsDataBanditGame, GameBlocks,BaseObject, db
from collections import OrderedDict
import numpy
from datetime import datetime
import json
import math
import glob
from sqlalchemy.sql.expression import func
from sqlalchemy import and_


@app.route("/participants_data_banditgame/create/<participant_id>/<block_id>/<prolific_id>", methods=["POST", "GET"])
def create_participant_banditgame(participant_id, block_id, prolific_id):
     content                        = request.json        
     participant                    = ParticipantsDataBanditGame()

     participant.participant_id     = int(participant_id)
     participant.prolific_id        = str(prolific_id)
     participant.block_number       = int(content['block_number'])
     participant.block_feedback     = int(content['block_feedback'])
     participant.block_learning     = int(content['block_learning'])
     participant.chosen_symbols     = str(content['chosen_symbols'])
     participant.chosen_positions   = str(content['chosen_positions'])
     participant.chosen_rewards     = str(content['chosen_rewards'])
     participant.unchosen_rewards   = str(content['unchosen_rewards'])
     participant.reward1            = str(content['reward_1'])
     participant.reward2            = str(content['reward_2'])
     participant.reaction_time      = str(content['reaction_times'])
     participant.game_id            = int(content['game_id'])
     

     # Add the performance metrics here 
     participant.block_perf = content['block_perf']
     participant.completed  = str(content['completed']) # could take up three values: "no" for the all but the last pushed block, 
     # "yes" for the last finished block 
     # " aborted" : if the user closes the browser or is idle for more than 10 min on the task, the task window closes itseld 

     participant.date_time  = str(content['date_time'])
     
     BaseObject.check_and_save(participant)

     result = dict({"success": "yes"})    

     print('Saved block data')
     return jsonify(result)

# Get the bonus information: 
@app.route("/participants_data_banditgame/score/<participant_id>/<game_id>/<prolific_id>", methods=["POST", "GET"])

def get_participant_score(participant_id,game_id,prolific_id):

    # If the prolific_id is provided than look up based on the prolific UID

    if prolific_id =='undefined': 
#         check      = ParticipantsDataBanditGame.query.filter_by(participant_id=participant_id) # START HERE WILL GET MULTIPLE GAMES INCORRETC
        query      = ParticipantsDataBanditGame.query.filter(ParticipantsDataBanditGame.participant_id==participant_id).filter(ParticipantsDataBanditGame.game_id==game_id)
    else:
        # query      = ParticipantsDataBanditGame.query.filter_by(prolific_id=prolific_id)
#         check      = ParticipantsDataBanditGame.query.filter_by(prolific_id=prolific_id) # START HERE WILL GET MULTIPLE GAMES INCORRETC
        query      = ParticipantsDataBanditGame.query.filter(ParticipantsDataBanditGame.prolific_id==prolific_id).filter(ParticipantsDataBanditGame.game_id==game_id)


    rel_perf        = query.all()    
    rel_perf_blocks = numpy.concatenate([numpy.array(rel_perf[i].get_block_perf().split(',')[-1:], dtype=numpy.float) for i in range(len(rel_perf))])

#     check_perf        = check.all()    
#     check_perf_blocks = numpy.concatenate([numpy.array(check_perf[i].get_block_perf().split(',')[-1:], dtype=numpy.float) for i in range(len(rel_perf))])
  
#     print(check_perf_blocks)
    print(rel_perf_blocks)
    
    # Get the maxperf per block from the other table 
    query     = GameBlocks.query.filter_by(game_id=game_id)
    max_perf  = query.all()    

   
    max_perf_blocks = numpy.concatenate([numpy.array(max_perf[i].get_maxreward().split(',')[-1:], dtype=numpy.float) for i in range(len(max_perf))])
    
    # idx_neg = numpy.where(numpy.array(rel_perf_blocks[2:])<0)
    idx_pos = numpy.where(numpy.array(rel_perf_blocks[2:])>0)

    print(rel_perf_blocks)
    print(max_perf_blocks)

    meanperf_pos  = numpy.mean(rel_perf_blocks[idx_pos])
    # meanperf_neg  = numpy.mean(rel_perf_blocks[idx_neg])

    meanmaxperf_pos  = numpy.mean(max_perf_blocks[idx_pos]) # exclude the first 2 training sessions 
    # meanmaxperf_neg  = numpy.mean(max_perf_blocks[idx_neg]) # exclude the first 2 training sessions 

    ratio = meanperf_pos/meanmaxperf_pos # determine the bonus based on the reward learning as before  + (1-numpy.abs(meanperf_neg/meanmaxperf_neg))

    # print([meanmaxperf_pos, meanmaxperf_neg])
    print(ratio)
    
    app.logger.info([meanperf_pos])
    app.logger.info([meanmaxperf_pos])
    app.logger.info(ratio)
    
    if math.isnan(ratio): 
        print('Ratio is nan')

    if ratio < 0.5 or math.isnan(ratio): 
        bonus = 0
    elif ratio >= 1.0: 
         bonus = 1.0
    else:
        bonus = 0.5
    
    result          = {}
    result['bonus'] = str(bonus) 

    app.logger.info(bonus)

    return jsonify(result), 200 # json.dumps(result)

# To ge the data from this table 
@app.route('/participants_data_banditgame/<participant_id>/<block_id>', methods=['GET'])

def get_participant_data_banditgame(participant_id,block_id):
    query = ParticipantsDataBanditGame.query.filter(ParticipantsDataBanditGame.participant_id==participant_id,ParticipantsDataBanditGame.participant_id==block_id)
    
    if query != None:
        print('Exists')
        
    block  = query.first_or_404()

    # format the query into a dictionnary first:
     
    result                     = {}

    arr_participant_id         = block.get_participant_id()[0].replace('  ',' ').split(' ')
    result['participant_id']   = arr_participant_id[0]

    arr_prolific_id            = block.get_prolific_id().replace('  ',' ').split(' ')
    result['prolific_id']      = arr_prolific_id

    arr_block                  = block.get_block_number()[0].replace('  ',' ').split(' ')
    result['block_number']     = arr_block[0]

    arr_feedback               = block.get_block_feedback()[0].replace('  ',' ').split(' ')
    result['block_feedback']     = arr_feedback[0]

    arr_learning               = block.get_block_learning()[0].replace('  ',' ').split(' ')
    result['block_learning']   = arr_learning[0]

    arr_datetime                = block.get_date_time()
    result['date_time']         = arr_datetime

    arr_chosen_symbols         = block.get_chosen_symbols().replace('  ',' ').split(' ') 
    result['chosen_symbols']   = arr_chosen_symbols 

    arr_chosen_positions       = block.get_chosen_positions().replace('  ',' ').split(' ') 
    result['chosen_positions'] = arr_chosen_symbols

    arr_chosen_rewards         = block.get_chosen_rewards().replace('  ',' ').split(' ') 
    result['chosen_rewards']   = arr_chosen_rewards 
    
    arr_unchosen_rewards       = block.get_unchosen_rewards().replace('  ',' ').split(' ') 
    result['unchosen_rewards'] = arr_unchosen_rewards 
     
    arr_rt                     = block.get_reaction_time().replace('  ',' ').split(' ') 
    result['reaction-times']   = arr_rt

    arr_block_perf             = block.get_block_perf().replace('  ',' ') 
    result['block_perf']       = arr_block_perf

    arr_completed             = block.get_completed().replace('  ',' ')
    result['completed']       = arr_completed

    
    app.logger.info(result)
    return jsonify(result), 200 



