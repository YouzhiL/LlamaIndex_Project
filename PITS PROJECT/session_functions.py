from global_settings import SESSION_FILE
import yaml
import os

# takes the current state as an argument, which includes all the necessary information about the user's session and writes it to a file named SESSION_FILE.
# The state is converted into YAML format before saving
def save_session(state):
  state_to_save = {key: value for key, value in state.items()}
  with open(SESSION_FILE, 'w') as file:
    yaml.dump(state_to_save, file)


# When a session needs to be cleared, this function deletes SESSION_FILE and removes all the keys
# from the passed state object, effectively resetting the session.   
def delete_session(state):
  # The function checks the path exactly as it is defined in the SESSION_FILE variable. If SESSION_FILE is an absolute path, it checks that specific location. If it is a relative path, it checks relative to the current working directory.
  if os.path.exists(SESSION_FILE):
    os.remove(SESSION_FILE)
  for key in list(state.keys()):
    del state[key]



