{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "763543fc-32b2-46e3-964c-8293dd560f20",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0249de78-5dbe-4847-9971-16819ac8abdb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(url_or_path_to_csv_file):\n",
    "\n",
    "    # Method Chain 1 (Load data and deal with missing data)\n",
    "\n",
    "    df1 = (\n",
    "          pd.read_csv(url_or_path_to_csv_file)\n",
    "          .dropna()\n",
    "          .drop([10005]) # data in index 10005 column DAILY_STRESS is irrelevent, so the row is dropped.\n",
    "      )\n",
    "\n",
    "    # Method Chain 2 (Clean data by drop unrelated columns, drop others, and do processing)\n",
    "\n",
    "    df2 = (\n",
    "          df1\n",
    "          .drop(columns=[\"PLACES_VISITED\", \"CORE_CIRCLE\", \"SUPPORTING_OTHERS\", \n",
    "                         \"SOCIAL_NETWORK\", \"ACHIEVEMENT\", \"DONATION\", \"LOST_VACATION\", \n",
    "                         \"DAILY_SHOUTING\", \"SUFFICIENT_INCOME\", \"PERSONAL_AWARDS\", \"TIME_FOR_PASSION\", \n",
    "                         \"WEEKLY_MEDITATION\", \"AGE\", \"WORK_LIFE_BALANCE_SCORE\", \"FLOW\", \"LIVE_VISION\", \n",
    "                         \"Timestamp\"])\n",
    "          .assign(BMI_RANGE = lambda x: x['BMI_RANGE'].astype(object), \n",
    "                  TODO_COMPLETED = lambda x: x['TODO_COMPLETED'].astype(object))\n",
    "          .reset_index(drop=True)\n",
    "      )\n",
    "\n",
    "    # Make sure to return the latest dataframe\n",
    "\n",
    "    return df2 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0cbeaa7-3dbf-44dc-9002-0c441c48be45",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
