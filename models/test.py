"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DATETIME, Float, VARCHAR, Text, Boolean, String, DateTime,JSON
from models.db import Model
from models.base_object import BaseObject
import datetime 

class Test(BaseObject, Model):

    '''
        This is the table where we put the collected QUESTIONNAIRE data from the participants in the RLVARTASK: this only contains the responses but not the question content which is stored in the JS object on the server. 
        
    '''
    id              = Column(Integer, primary_key=True) 
    participant_id  = Column(BigInteger,nullable=True)
    prolific_id     = Column(String(128)) 
    handle          = Column(String(128)) # handle from the BE  
    beginexp        = Column(DateTime, nullable=True) # begin 
    endexp          = Column(DateTime, nullable=True)
    
    datatask        = Column(JSON, nullable=True) # Data for the task
    datasubinfo     = Column(JSON, nullable=True) # Data for the task
    
    debriefed       = Column(Boolean)
    status          = Column(Integer, nullable = True)
    bonus           = Column(Text, nullable=True) # Data for the task 

    def __init__(self,prolific_id, participant_id, handle): 
        

        print('TASK INIT')

        self.debriefed      = False
        self.participant_id = participant_id  
        self.prolific_id    = prolific_id     
        self.handle         = handle     
        self.status         = 1
        self.beginexp       = datetime.datetime.now() 

    def get_id(self):
        return str(self.id)

    def get_participant_id(self):
        return str(self.participant_id)

    def get_prolific_id(self):
        return str(self.prolific_id)

    def get_handle(self):
        return str(self.handle)

    def get_datatask(self):
        return str(self.datatask)

    def get_datasubinfo(self):
        return str(self.datasubinfo)
    

        
    def errors(self):
        errors = super(Test, self).errors()
        return errors
 
     

