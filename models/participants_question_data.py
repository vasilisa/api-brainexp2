"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DATETIME, Float, VARCHAR

from models.db import Model
from models.base_object import BaseObject

class ParticipantsQuestionData(BaseObject, Model):

    '''
        This is the table where we put the collected QUESTIONNAIRE data from the participants in the RLVARTASK: this only contains the responses but not the question content which is stored in the JS object on the server. 
        
    '''
    id = Column(Integer, primary_key=True)

    participant_id  = Column(BigInteger, nullable=False)
    prolific_id     = Column(VARCHAR(length=200))
    handle          = Column(VARCHAR(length=100))

    date_time_survey_start           = Column(VARCHAR(length=100)) # the date at which the questionnaire has been answered   
    date_time_survey_end             = Column(VARCHAR(length=100)) # the date at which the questionnaire has been answered   
    date_time                        = Column(VARCHAR(length=100)) # the date at which the questionnaire has been answered   

    block_number     = Column(Integer) # the questionnaire has parts and each part is stored as a separate row in the table
    block_name       = Column(VARCHAR(length=1000)) # the questionnaire has parts and each part is stored as a separate row in the table
    question_ids     = Column(VARCHAR(length=1000))  # the survey block name /tag for the section 
    answers          = Column(VARCHAR(length=10000)) # an array with the string answers to each of the question items in the questionnaire block    
    survey_completed = Column(VARCHAR(length=100)) # whether the survey has been completed, uncompleted or "aborted"
    

    def get_id(self):
        return str(self.id)

    def get_participant_id(self):
        return str(self.participant_id)

    def get_prolific_id(self):
        return str(self.prolific_id)

    def get_block_number(self):
        return str(self.block_number)

    def get_block_name(self):
        return str(self.block_name)

    def get_question_ids(self): 
        return str(self.question_ids)

    def get_answers(self): 
        return str(self.answers)

    def get_survey_completed(self): 
        return str(self.survey_completed)
    
    def get_date(self): 
        return str(self.date_time)

    def get_datetime(self): 
        return str(self.date_time_survey_start)

    def get_datetime(self): 
        return str(self.date_time_survey_end)

    
    def errors(self):
        errors = super(ParticipantsQuestionData, self).errors()
        return errors
 
     

