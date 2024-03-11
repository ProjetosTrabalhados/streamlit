import streamlit as st
# import pandas as pd
from streamlit_option_menu import option_menu
#tester



# __error = {}
# st.markdown("# Main page 🎈")
# st.sidebar.markdown("# Main page 🎈")
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
    st.title("Main")
    sideBar()
    # selected=""
  

if __name__ == "__main__":
    main()


