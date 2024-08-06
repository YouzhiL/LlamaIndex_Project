from datetime import datetime
from global_settings import LOG_FILE
import os

# This module is for recording events, user actions, and other significant occurrances
# during the execution of the application into a log file.
# Mainly to provide the context for the PITS agent during its interactions with the user 
def log_action(action, action_type):
  timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  log_entry = f"{timestamp}: {action_type} : {action}\n"
  with open( LOG_FILE,'w') as file:
    file.write(log_entry) #This function reduces the file size to zero bytes. This effectively clears all the content of the file without deleting the file itself.
    
  