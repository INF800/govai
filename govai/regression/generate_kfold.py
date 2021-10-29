import sys
import omegaconf as OmegaConf

from govai.common.kfold import kfold

def main(args):
    df_test = pd.read_csv(filepath_or_buffer=args.test_file.path,
                           header=args.ignore_header,
                           sep=args.delimiter)

    cols = [i.lower() for i in df_test.columns]
    df_test.columns = cols
    if args.test_file.ignore_cols:
        cols = list(set(cols) - set(ignore_cols))
        df_test = df_test[cols]

    df_test.insert(0, args.id_column, [*range(len(df_test))])

    df_train = pd.read_csv(filepath_or_buffer=args.train_file.path,
                           header=args.ignore_header,
                           sep=args.delimiter)
    
    cols = [i.lower() for i in df_train.columns]
    df_train.columns = cols
    if args.train_file.ignore_cols:
        cols = list(set(cols) - set(ignore_cols))
        df_train = df_train[cols]

    df_train.insert(0, args.id_column, [*range(len(df_train))])
    
    df_train.rename(columns={args.train_file.target_col: "target",}, inplace=True)
    df_kfold = kfold(...)


if __name__ == '__main__':
    conf = OmegaConf.load(sys.argv[0]) 
    main(conf.original_data)