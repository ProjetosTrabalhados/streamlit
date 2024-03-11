import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
#tester
#tester2



# __error = {}

def sideBar():
      with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Graphs'], 
            icons=['house', 'graphs'], menu_icon="cast", default_index=0)
        
        match selected:
            case 'Graphs':
                # st.write(selected)
                # st.page("pages/graph.py")
                st.switch_page("pages/graph.py")
            case _:
                # st.switch_page("main.py")
                pass

def main():
    # st.title("Main")
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

    

    df_1 = pd.read_csv('./arquivos/Energy-/renewablePowerGeneration97-17.csv')
    df_2 = pd.read_csv('./arquivos/Energy-/top20CountriesPowerGeneration.csv')

    
    st.title("Geração de enegia reutilizavel por anos")
    st.write(df_1)
    st.write("---")
    st.title("Paises com maior numero de geração de energia")
    st.write(df_2)




    df_1 = df_1.drop(columns=["Year"], axis=1)
    df_2 = df_2.drop(columns=["Country", "Total (TWh)"], axis=1)

    max_1 = df_1.index[-1]
    max_2 = df_2.index[-1]
    diff = max_1-max_2
    if diff < 0:
        diff *=-1

    # st.write(diff)

    for index in range(max_1,(max_1-diff), -1):
        # st.write(index)
        df_1 = df_1.drop(df_1.index[index])
    # df_2_new = dict()

    


    st.write("***")
    st.title("Comparação entre tabelas")
    #Trazendo dados defirentes/iguais(true/false)  nos dois index com base no df_1


    st.write(df_1[(df_1 > df_2).all(axis=1) == False])
    
    # sideBar()
    # selected=""
  

if __name__ == "__main__":
    main()


