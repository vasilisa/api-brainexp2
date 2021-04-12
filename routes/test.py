from flask import current_app as app, jsonify, request, render_template

from models import Test, BaseObject, db
# from collections import OrderedDict
import json
# import glob
import datetime
from sqlalchemy.sql.expression import func


# Status codes
ALLOCATED = 1
STARTED   = 2
COMPLETED = 3
DEBRIEFED = 4
QUITEARLY = 6


@app.route('/exp', methods=['GET']) # ROUTE TO START EXPERIMENT 

def start_exp():

    """
        Serves up the experiment applet.
    """
    print('prolific_id' in request.args)
    print('handle' in request.args)


    print('Start Expe')

    if not ('prolific_id' in request.args) and ('handle' in request.args) and ('participant_id' in request.args): 
        raise ExperimentError('prolific_study_participant_id_handle_not_set_in_exp_url')
    
    prolific_id    = request.args['prolific_id']
    participant_id = request.args['participant_id']
    handle         = request.args['handle']
    
    print(("Prolific ID: {0}, Participant ID: {1}, handle: {2}").format(prolific_id, participant_id, handle))
    
    # Filter for prolific id and longit id in the DB: check first to see if they exist.  
    # this might not work TO BE CHANGED 
    matches = Test.query.\
                        filter(Test.prolific_id == prolific_id).\
                        filter(Test.handle == handle).\
                        all()
    # print(matches) 
    numrecs = len(matches)
    if numrecs == 0: # is not in the DB -> create a record in the DB 
        part   = Test(prolific_id, participant_id, handle)
        
        print("No match. Status is", part.status)
 
        part.status         = STARTED
        part.beginexp       = datetime.datetime.now()
        part.prolific_id    = prolific_id
        part.handle         = handle
        part.participant_id = int(participant_id) 
        
        BaseObject.check_and_save(part)

        result = dict({"success": "yes"}) 
        
    else : 
        part = matches[0]
        print("Participant id {0} matched in the DB! Status is {1}".format(participant_id, part.status))
    
    # Start the task  TO BE CHANGED

    # return render_template('ps_dev_exp.html', study_id = 'kiki', participant_id = participant_id, prolific_id = prolific_id, longit_id = 'coucou')
    return render_template('index.html', prolific_id = prolific_id, participant_id = participant_id, handle = handle)


@app.route('/quitter', methods=['POST'])

def quitter():
    
    """
        Subjects post data as they quit, to help us better understand the quitters.
    """
    print("accessing the /quitter route")
    # print(request.form.keys())

    prolific_id  = request.form['prolific_id']
    study_id     = request.form['study_id']
    datastring   = request.form['datastring']
    when         = request.form['when']

    datafile     = open('quitters/prolific_id'+prolific_id+'_'+study_id+'_'+when+'.csv', 'w')
    datafile.write(datastring)
    datafile.close()
    
    if ('prolific_id' in request.form) and ('datastring' in request.form) and ('longit_id' in request.form): 
        prolific_id = request.form['prolific_id']
        datastring  = request.form['datastring']
        longit_id   = request.form['longit_id']
        
        print("getting the save data {0} for quitter prolific id {1} longit id {2}", datastring,prolific_id,longit_id)
        user = Test.query.\
            filter(Test.prolific_id == prolific_id).\
            filter(Test.longit_id == longit_id).\
            one()
        
        user.datastring = datastring
        user.status     = STARTED

        BaseObject.check_and_save(user)

        result = dict({"success": "yes"}) 
        # db_session.add(user) #inserting entry into database
        # db_session.commit()
        print("Quitter route, status is", user.status)
    return render_template('error.html', errornum= 1011)


@app.route('/done', methods=['POST', 'GET'])
def savedata():
    """
        User has finished the experiment and is posting their data in the form of a
        (long) string. They will receive a debriefing back.
    """
    print("accessing the /done route")

    print('prolific_id' in request.form)
    print('handle' in request.args)


    prolific_id    = request.args['prolific_id']
    handle         = request.args['handle'] # if it is in the url 
    participant_id = request.args['participant_id']
    
    prolific_id    = request.form['prolific_id'] # if it is in the data 
    
    json           = request.form['json']
    
    print("saving the data of PROLIFIC ID {0} and handle {1}".format(prolific_id,handle))
    
    # datafile = open('space_novel_subinfo/'+study_id+'_'+prolific_id+'_'+longit_id+'_'+when+'.csv', 'w')
    # datafile.write(datastring)
    # datafile.close()

    # # bonuses 
    # datafile2 = open('Payments/'+study_id+'_'+prolific_id+'_'+longit_id+'_'+when+'.csv', 'w')
    # datafile2.write(payment)
    # datafile2.close()
    
    if ('prolific_id' in request.form) and ('json' in request.form): 
        prolific_id    = request.form['prolific_id']
        datastring     = request.form['json']
        handle         = request.form['handle']
        participant_id = request.form['participant_id']
        bonus          = request.form['bonus']

        print("getting the save data {0} for prolific ID {1} and handle {2}".format(datastring,prolific_id,handle))

        # This is the TableName 
        user = Test.query.\
            filter(Test.prolific_id == prolific_id).\
            filter(Test.handle      == handle).\
            one()
        
        
        user.datasubinfo = datastring
        user.status      = COMPLETED
        user.bonus       = bonus
        user.endexp      = datetime.datetime.now()

        BaseObject.check_and_save(user)

        result = dict({"success": "yes"}) 

        print("Exp subinfo done route, status is", user.status)
    
    return jsonify(result), 200
    



@app.route('/taskdone', methods=['POST', 'GET'])
def savetaskdata():
    """
        User has finished the experiment and is posting their data in the form of a
        (long) string. They will receive a debriefing back.
    """
    print("accessing the /taskdone route")

    print('prolific_id' in request.form)
    print('handle' in request.args)


    prolific_id    = request.args['prolific_id']
    handle         = request.args['handle'] # if it is in the url 
    participant_id = request.args['participant_id']
    
    json           = request.form['json']
    
    print("saving the task data of PROLIFIC ID {0} and handle {1}".format(prolific_id,handle))
    
    if ('prolific_id' in request.form) and ('json' in request.form): 
        prolific_id    = request.form['prolific_id']
        datastring     = request.form['json']
        handle         = request.form['handle']
        participant_id = request.form['participant_id']

        print("getting the save data {0} for prolific ID {1} and handle {2}".format(datastring,prolific_id,handle))

        # This is the TableName 
        user = Test.query.\
            filter(Test.prolific_id == prolific_id).\
            filter(Test.handle      == handle).\
            one()
        
        
        user.datatask = datastring

        BaseObject.check_and_save(user)

        result = dict({"success": "yes"}) 

        print("Exp task done route, status is", user.status)
    
    return jsonify(result), 200
    



# ADD FEEDBACK HERE 
@app.route('/feedbackDone', methods=['POST']) # not sure where it is called 

def startfeedback():

    """
        User has finished the feedback and is posting their data in the form of a
        (long) string. They will receive a prolific validation page back.

    """
    print("accessing the /feedbackDone route")

    prolific_id    = request.form['prolific_id']
    study_id       = request.form['study_id']
    participant_id = request.form['participant_id']
    longit_id      = request.form['longit_id']
    
    when           = request.form['when']
    
    print("saving the feedback data of subject {1} for study {0} in time point {2}".format(prolific_id,study_id,longit_id))
    
    if ('prolific_id' in request.form) and ('feedbackDatastring' in request.form): 
        prolific_id         = request.form['prolific_id']
        feedbackDatastring  = request.form['feedbackDatastring']
    
        print("getting the feedback save data {0} for prolific ID {1} and longit ID {2}".format(feedbackDatastring,prolific_id,longit_id))
        user = Test.query.\
            filter(Test.prolific_id == prolific_id).\
            filter(Test.longit_id == longit_id).\
            one()
        
        user.feedback   = feedbackDatastring
        user.status     = DEBRIEFED
        user.endexp     = datetime.datetime.now()
        
        BaseObject.check_and_save(user)

        result = dict({"success": "yes"}) 

        print("Feedback done route, status is", user.status)


    return render_template('payment.html') # proceed to the validation prolific page 

    

@app.route('/inexp', methods=['POST']) # not sure where it is called 
def enterexp():
    """
    AJAX listener that listens for a signal from the user's script when they
    leave the instructions and enter the real experiment. After the server
    receives this signal, it will no longer allow them to re-access the
    experiment applet (meaning they can't do part of the experiment and
    referesh to start over).
    """
    print("/inexp")
    if ('prolific_id' in request.form) and ('longit_id' in request.form): 
        prolific_id   = request.form['prolific_id']
        longit_id     = request.form['longit_id']

    else: 
        raise ValueError('improper_inputs')\

    user = Test.query.\
            filter(Test.prolific_id == prolific_id).\
            filter(Test.longit_id   == longit_id).\
            one()
    user.status   = STARTED
    user.beginexp = datetime.datetime.now()

    BaseObject.check_and_save(user)
    result = dict({"success": "yes"}) 
    return "Success"

@app.route('/inexpsave', methods=['POST'])
def inexpsave():
    """
    The experiments script updates the server periodically on subjects'
    progress. This lets us better understand attrition.
    """
    print("accessing the /inexpsave route")
    
    if ('prolific_id' in request.form) and ('longit_id' in request.form) and ('datastring' in request.form): 
        prolific_id   = request.form['prolific_id']
        longit_id     = request.form['longit_id']
        datastring    = request.form['datastring']
        print("getting the save data for prolific id {0}, longit id {1}: {2}".format(prolific_id, longit_id, datastring))
        
        user = Test.query.\
                filter(Test.prolific_id == workerId).\
                filter(Test.longit_id == longit_id).\
                one()
        user.datastring = datastring
        user.status     = STARTED

        BaseObject.check_and_save(user)
        result = dict({"success": "yes"}) 

    return render_template('error.html', errornum=1012)

