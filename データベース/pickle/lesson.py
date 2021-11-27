"""
Python のデータ型をそのまま保持できる.
https://qiita.com/hatt0519/items/f1f4c059c28cb1575a93
"""

import pickle

data = {"a": "a"}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    loaded = pickle.load(f)
    print(loaded)
