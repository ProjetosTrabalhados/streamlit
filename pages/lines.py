import streamlit as st 
from streamlit_option_menu import option_menu
from Classes.Graficos import Graficos


st.markdown("# Graph lines  🎈")
st.sidebar.markdown("# Graph lines page 🎈")

# sideBar()    
csv = {
    'Continent_Consumption_TWH':'Continent_Consumption_TWH.csv',
    'Country_Consumption_TWH':'Country_Consumption_TWH.csv',
    'nonRenewablesTotalPowerGeneration':'nonRenewablesTotalPowerGeneration.csv',
    'renewablePowerGeneration97-17':'renewablePowerGeneration97-17.csv',
    'renewablesTotalPowerGeneration':'renewablesTotalPowerGeneration.csv',
    'top20CountriesPowerGeneration' : 'top20CountriesPowerGeneration.csv'
}
# while(True):
    
#     break
# st.write("---")

# st.title("Plotting graphs")
st.write("---")

graph = Graficos(csv)    
graph.plotar_graficos("lines")
