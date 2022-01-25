from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


data_path = os.path.join(BASE_DIR, 'Cleaned.csv')
def findres(arr):
    cleaned = pd.read_csv(data_path)
    x = cleaned.drop('Diagnosis', axis=1)
    y = cleaned['Diagnosis']
    regs = LogisticRegression().fit(x,y)
    case = np.array(arr)
    Result = regs.predict(case.reshape(1,-1))
    return(str(Result[0]))
