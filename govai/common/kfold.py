import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import model_selection

def create_folds(data, k=5, target_col='target', task_type='classification',
                 kfold_col='kfold',
                 num_bins='auto', shuffle=True, seed=111, log=None):
 if log: print('generating kfold cols')

 data["kfold"] = -1
 if task_type=='regression':
  if num_bins=='auto':
    num_bins = np.floor(1 + np.log2(len(data)))

  if log: print(f'generating bins with n_bins={num_bins}')
  data.loc[:, "bins"] = pd.cut(data[target_col], bins=int(num_bins), labels=False)

 # initiate the kfold class from model_selection module
 kf = model_selection.StratifiedKFold(n_splits=k, shuffle=shuffle, random_state=seed)

 # fill the new kfold column
 # note that, instead of targets, we use bins for regression tasks
 if task_type=='regression':
   target_col='bins'
 for f, (t_, v_) in enumerate(kf.split(X=data, y=data[target_col].values)):
    data.loc[v_, kfold_col] = f

 if log: print('kfold done.')
 data = data.drop("bins", axis=1)
 return data