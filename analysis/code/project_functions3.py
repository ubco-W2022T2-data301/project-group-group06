import pandas as pd

def load_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .dropna()
          .drop([10005]) # data in index 10005 column DAILY_STRESS is irrelevent, so the row is dropped.
      )

    # Method Chain 2 (Clean data by drop unrelated columns, drop others, and do processing)

    df2 = (
          df1
          .drop(columns=["PLACES_VISITED", "CORE_CIRCLE", "SUPPORTING_OTHERS", 
                         "SOCIAL_NETWORK", "ACHIEVEMENT", "DONATION", "LOST_VACATION", 
                         "DAILY_SHOUTING", "SUFFICIENT_INCOME", "PERSONAL_AWARDS", "TIME_FOR_PASSION", 
                         "WEEKLY_MEDITATION", "AGE", "WORK_LIFE_BALANCE_SCORE", "FLOW", "LIVE_VISION", 
                         "Timestamp"])
          .assign(BMI_RANGE = lambda x: x['BMI_RANGE'].astype(object), 
                  TODO_COMPLETED = lambda x: x['TODO_COMPLETED'].astype(object))
          .reset_index(drop=True)
      )

    # Make sure to return the latest dataframe

    return df2 