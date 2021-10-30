# example usage:
# python3 -m govai.regression.generate_kfold configs/default_kfold.yaml

import sys

from omegaconf import OmegaConf
import pandas as pd

from govai.common.kfold import create_folds

def main(args):
    df_test = pd.read_csv(filepath_or_buffer=args.test_file.path,
                           header=args.header,
                           sep=args.delimiter)

    cols = [i.lower() for i in df_test.columns]
    df_test.columns = cols
    if args.ignore_cols:
        cols = list(set(cols) - set(ignore_cols))
        df_test = df_test[cols]

    df_test.insert(0, args.id_column, [*range(len(df_test))])
    df_test.to_csv(args.test_file.output_path, index=False)

    df_train = pd.read_csv(filepath_or_buffer=args.train_file.path,
                           header=args.header,
                           sep=args.delimiter)
    
    cols = [i.lower() for i in df_train.columns]
    df_train.columns = cols
    if args.ignore_cols:
        cols = list(set(cols) - set(ignore_cols))
        df_train = df_train[cols]

    df_train.insert(0, args.id_column, [*range(len(df_train))])
    
    df_train.rename(columns={args.train_file.target_col: "target",}, inplace=True)
    df_kfold = create_folds(df_train, k=args.train_file.kfold, kfold_col=args.train_file.kfold_col, 
                            target_col='target', # renamed 
                            task_type='regression', 
                            num_bins=args.train_file.n_bins,
                            shuffle=args.train_file.shuffle, seed=args.seed)

    df_kfold.to_csv(args.train_file.output_path, index=False)


if __name__ == '__main__':
    conf = OmegaConf.load(sys.argv[1]) 
    main(conf)