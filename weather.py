import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('F:/MachineLearning/Weather/weather_model (1).sav','rb'))

def weather_prediction(input_data):
    
    input_data_as_numpy=np.asarray(input_data)
    
    input_data_reshaped=input_data_as_numpy.reshape(1,-1)
    
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if prediction[0] == 0:
        return '☁ The weather is Cloudy'
    elif prediction[0] == 1:
        return '🌧 The weather is Rainy'
    elif prediction[0] == 2:
        return '❄ The weather is Snowy'
    elif prediction[0] == 3:
        return '🌞 The weather is Sunny'
    else:
        return '⚠ Unknown prediction'
      
def main():
    
    st.title('Weather Prediction Web App')
    
    col1,col2,col3=st.columns(3)

    with col1:
        temperature = st.text_input('🌡 Temperature')
    
    with col2:
        humidity = st.text_input('💧 Humidity')

    with col3:
        wind_speed = st.text_input('🍃 Wind Speed')
    
    with col1:
        precipitation = st.number_input('☔ Precipitation (%)')

    with col2:
        cloud_cover = st.selectbox('☁ Cloud cover',['overcast','partly cloudy','clear','cloudy'])
        cl={
          'clear':0,
          'partly cloudy':1,
          'cloudy':2,
          'overcast':3
        }
        cloud = cl[cloud_cover]

    with col3:
        atmospheric_pressure = st.text_input('🔃  Atmospheric Pressure')

    with col1:
        uv_index = st.number_input('🔆 UV Index')

    
  
    with col2:
        season = st.selectbox('🌦 Season',['Winter','Spring','Autumn','Summer'])
        ss = {
          'Winter':0,
          'Spring':1,
          'Autumn':2,
          'Summer':3
        }
        sn = ss[season]

    with col3:
        visibility = st.text_input('👁 Visibility (km)')

    with col1:
        location = st.selectbox('🏞 Location',['inland','mountain','coastal'])
        lc = {
          'inland':0,
          'mountain':1,
          'coastal':2
        }
        lcn = lc[location]

    
    diagnosis=''
    
    if st.button('Weather Report'):
        diagnosis = weather_prediction([float(temperature),float(humidity),float(wind_speed),float(precipitation),float(cloud),float(atmospheric_pressure),float(uv_index),float(sn),float(visibility),float(lcn)])

        
    st.success(diagnosis)
    
main()