import streamlit as st
import pandas as pd

class Graficos:
    # ./csv_arquivos/Energy-/
    # __dir_arq = str()

    def __init__(self, csv, dir_arq="./csv_arquivos/Energy-/"):
        self.__dir_arq = dir_arq
        self.__csv = csv
    
    # _csv = {
    #     'Continent_Consumption_TWH':'Continent_Consumption_TWH.csv',
    #     'Country_Consumption_TWH':'Country_Consumption_TWH.csv',
    #     'nonRenewablesTotalPowerGeneration':'nonRenewablesTotalPowerGeneration.csv',
    #     'renewablePowerGeneration97-17':'renewablePowerGeneration97-17.csv',
    #     'renewablesTotalPowerGeneration':'renewablesTotalPowerGeneration.csv',
    #     'top20CountriesPowerGeneration' : 'top20CountriesPowerGeneration.csv'
    # }


    def plotar_graficos(self, tipo=""):
        data = dict()
        for name in self.__csv:
            # st.write(csv[name])
            data[name] = (pd.read_csv(self.__dir_arq+self.__csv[name]))


        for name_arq in data:
            try:
                
                match tipo.lower():
                    case "barras":
                        st.bar_chart(data[name_arq])
                    case _:
                        st.warning("Não foi possivel reconhecer o tipo de gráfico pedido")
            
            except Exception as e:
                st.error(e)
                st.warning("Segue tabela para visualização do arquivo "+self.__csv[name_arq])
                st.write(data[name_arq])