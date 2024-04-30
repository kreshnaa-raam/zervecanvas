import sklearn
import pandas as pd
from joblib import load

#ZER-2202
model = log_reg

df = pd.DataFrame(payload, index=[0])

prediction = model.predict(df)[0]

RESPONSE = prediction