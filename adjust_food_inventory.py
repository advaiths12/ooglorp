import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
import string
import math


#function to retrain the model based on the new data
#returns model object
def retrain(csv_path):
    df = pd.read_csv(csv_path)

    df.head()

    m = Prophet()
    m.fit(df)
    return m

def predict_date(date, model):

    #make dataframe
    future = model.make_future_dataframe(periods=365)
    #add to tail
    future.tail()

    #make prediction
    forecast = model.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    #change to standard times
    forecast['ds'] = pd.to_datetime(forecast['ds'])




def main():


    print(list(forecast['yhat_lower'])[list(forecast['ds']).index(pd.Timestamp('2010-08-10'))]) #how to look up a certain date




    fig1 = m.plot(forecast)