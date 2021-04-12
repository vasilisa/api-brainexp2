"""User model"""
from sqlalchemy import Column, Integer, ForeignKey, DATETIME, Float, VARCHAR,Text

from models.db import Model
from models.base_object import BaseObject

class ParticipantsDataBanditGame(BaseObject, Model):

    '''
        This is the table where we put the collected data from the participants in the RLVARTASK: this excludes the task specifications which 
        are stored separately in the Participants and Participants_blocks tables 
    
    '''
    id = Column(Integer, primary_key=True)

    participant_id    = Column(Integer, nullable=False)
    prolific_id       = Column(VARCHAR(length=200))

    game_id           = Column(Integer, nullable=False) 
    
    date_time         = Column(VARCHAR(length=200)) # date time start of the experiment 
    
    block_number       = Column(Integer, nullable=False)
    block_learning     = Column(Integer, nullable=False)
    block_feedback     = Column(Integer, nullable=False)
    
    chosen_symbols     = Column(Text(length=10000), nullable=False)     
    chosen_positions   = Column(Text(length=10000), nullable=False)    
    chosen_rewards     = Column(Text(length=10000), nullable=False) 
    unchosen_rewards   = Column(Text(length=10000), nullable=False)
    reward1            = Column(Text(length=10000), nullable=False) 
    reward2            = Column(Text(length=10000), nullable=False)    
    reaction_time      = Column(Text(length=10000), nullable=False)
      
    
    # Related to the performances: 
    # Add the performance metrics here 
    block_perf  = Column(Float, nullable=False)
    completed   = Column(VARCHAR(length=100), nullable=False) # could take up three values: "completed" for the all but the last pushed block,
     # uncompleted if this is not the last block or "aborted" if the user closes the browser or hits the return button?   
     
    def get_id(self):
        return str(self.id)

    def get_participant_id(self):
        return str(self.participant_id)

    def get_prolific_id(self):
        return str(self.prolific_id)

    def get_game_id(self):
        return str(self.game_id)

    def get_block_number(self):
        return str(self.block_number)

    def get_chosen_symbols(self): 
        return str(self.chosen_symbols)

    def get_chosen_positions(self): 
        return str(self.chosen_positions)

    def get_chosen_rewards(self): 
        return str(self.chosen_rewards)

    def get_unchosen_rewards(self): 
        return str(self.chosen_rewards)

    def get_reaction_time(self): 
        return str(self.reaction_time)

    def get_date_time(self): 
        return str(self.date_time)

    def get_block_perf(self): 
        return str(self.block_perf)

    def get_completed(self): 
        return str(self.completed)
    
    def errors(self):
        errors = super(ParticipantsDataBanditGame, self).errors()
        return errors
 
     

