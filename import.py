import pandas as pd
import numpy as np

# importing json files as dataframes
inferences = pd.read_json(r'My spotify Data/Inferences.json')
# df to csv
inferences.to_csv('user_inferences.csv', index=False)

# streaming history files
streaming_history = pd.read_json(r'My spotify Data/StreamingHistory0.json')
streaming_history = streaming_history.append(pd.read_json(r'My spotify Data/StreamingHistory1.json'))
streaming_history = streaming_history.append(pd.read_json(r'My spotify Data/StreamingHistory2.json'))
# df to csv
streaming_history.to_csv('streaming_history.csv', index=False)
