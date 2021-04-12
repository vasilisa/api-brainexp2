"""User model"""
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR

from models.db import Model
from models.base_object import BaseObject

class ConfigDataFollowUp(BaseObject, Model):

    '''
        This is the table where we put the prolific id, participatn id and retrieved app handle and start time for the study'
    '''

    id = Column(Integer, primary_key=True)

    participant_id          = Column(Integer,nullable=False)
    prolific_id             = Column(VARCHAR(length=200))
    date_time               = Column(VARCHAR(length=200)) # date time start of the experiment 
    
    def get_id(self):
        return str(self.id)

    def get_participant_id(self):
        return str(self.participant_id)

    def get_prolific_id(self):
        return str(self.prolific_id)

    def get_date_time(self): 
        return str(self.date_time)

    def errors(self):
        errors = super(ConfigDataFollowUp, self).errors()
        return errors
 
     

