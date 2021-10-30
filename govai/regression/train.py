from pathlib import Path
import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression

def main(args):
    feature_dir = Path('feature')
    kfold_fts_cont = [*feature_dir.glob("kfold_fts_cont_minmax.csv")][0]
    kfold_fts_cat = [*feature_dir.glob("kfold_fts_cat_ohe.csv")][0]

    kfold_fts_cont = pd.read_csv(kfold_fts_cont)
    kfold_fts_cat = pd.read_csv(kfold_fts_cat)
    
    kfold_targets = pd.read_csv(str(feature_dir/'kfold_targets.csv'))

    for k in range(5):
        train_ft_cont = kfold_fts_cont[kfold_fts_cont.kfold!=k]
        # scaler_cont = joblib.load()

        train_ft_cat = kfold_fts_cat[kfold_fts_cat.kfold!=k]
        train_ft = pd.concat([train_ft_cat, train_ft_cont], axis=1)


        
        target = kfold_targets[kfold_targets.kfold!=k]
        target = target['target_cont_std_mean'].values

        reg = LinearRegression().fit(train_ft, target)
        




if __name__ == '__main__':
    main(args=None)