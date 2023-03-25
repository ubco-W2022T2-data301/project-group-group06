def load_clean_process(file):
    # Method Chain 1 - load and clean data 
    df1 = (
        pd.read_csv(file)
        .dropna(axis = 0)
        .drop(columns = 'Timestamp')
        .loc[lambda x: x['DAILY_STRESS'] != '1/1/00']
        .rename(columns = lambda x: x.capitalize())    
    )
    
    # Method chaining to process the data 
    df2 = (
        df1
        .assign(Daily_stress = lambda x: pd.to_numeric(x['Daily_stress']), 
            Age = lambda x: x['Age']
            .cat.rename_categories(['21-35', '36-50', '> 50', '< 20']),
            Work_life_balance_score = lambda x: x['Work_life_balance_score'].astype(float).pipe(drop_outlier)) 
    )
    
    # Process data
    df3 = df2.reset_index()
    
    return df3