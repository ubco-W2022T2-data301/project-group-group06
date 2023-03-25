import pandas as pd

def load_clean_process(path):
    
    # Method chain 1 - load file and clean data
    data1 = (
        pd.read_csv(path)
        .drop(['Timestamp', 'FRUITS_VEGGIES', 'PLACES_VISITED', 'CORE_CIRCLE', 'SUPPORTING_OTHERS', 
                          'SOCIAL_NETWORK', 'ACHIEVEMENT', 'DONATION', 'BMI_RANGE', 'TODO_COMPLETED', 'DAILY_STEPS',
                          'LIVE_VISION', 'SLEEP_HOURS', 'LOST_VACATION', 'SUFFICIENT_INCOME', 'PERSONAL_AWARDS', 
                          'TIME_FOR_PASSION', 'WORK_LIFE_BALANCE_SCORE'], axis = "columns")
        .dropna()
        .loc[lambda x: x['DAILY_STRESS'] != '1/1/00']
    )
    
    # Method chain 2 - process data
    data2 = (
        data1.assign(DAILY_STRESS = lambda x: pd.to_numeric(x['DAILY_STRESS']), 
                     AGE = lambda x: x['AGE'].astype('category'),
                     Weighted_Score = lambda x: 7*x['FLOW'] + 7*(10-x['DAILY_SHOUTING']) + x['WEEKLY_MEDITATION']
                    )
        .rename(columns = lambda x: x.upper())
    )
    
    return data2