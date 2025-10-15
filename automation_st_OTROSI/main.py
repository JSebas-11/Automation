import streamlit as st
from Services.DataService import DataService
from Utilities.StreamlitUtilities import StreamlitUtilities
from Services.DataSource import DataSource
from Services.DataMetrics import DataMetrics
from Components.Metrics import Metrics
from Components.Format import Format
from Components.Data import Data
from Components.Automation import Automation

@st.cache_data
def load_services() -> bool:
    #Cargar datos desde la fuente al DataSource
    data_src: DataSource = DataSource()
    data_loaded: bool = data_src.load()
    
    if data_loaded:
        #En caso de poder cargar los datos asignamos las variables correspondientes
        st.session_state.datasource = data_src
        st.session_state.metrics = DataMetrics(data_src.data)
        st.session_state.dataservice = DataService(data_src)
        
    return data_loaded

def main() -> None:
    #--------------------------GLOBAL VARIABLES--------------------------
    st.set_page_config("Automatizacion OTROSI", page_icon="📄", layout="wide")
    loaded_services: bool = load_services()
    
    #--------------------------HEADER--------------------------
    st.write(f"<h1 style='color:{StreamlitUtilities.clr_primary}; text-decoration:underline'><center>Automatizacion de OTROSI<center></h1>",
        unsafe_allow_html=True)
    st.write("<p><center>Mini-app diseñada para automatizar el proceso de creacion de OTROSI usando una plantilla (.docx)<center></p>",
        unsafe_allow_html=True)
    
    st.divider()
    
    if loaded_services: 
        st.success("Datos y servicios cargados correctamente", icon=StreamlitUtilities.matl_icn("check_circle"))
    else: 
        st.error("Ha habido un error cargando datos y servicips. Refresca la app o revisa en la consola si el error persiste", 
            icon=StreamlitUtilities.matl_icn("priority_high"))
    
    st.divider()
    
    tab_workspace, tab_metrics, tab_format, tab_data = st.tabs(
        ["⚙️ WORKSPACE", "🧮 METRICS", "🧾 FORMAT", "📊 DATA"]
    )
    
    #--------------------------SECTIONS--------------------------
    if loaded_services:
        Automation.draw(tab_workspace, st.session_state.dataservice)
        Metrics.draw(tab_metrics, st.session_state.metrics)
        Format.draw(tab_format, st.session_state.dataservice)
        Data.draw(tab_data, st.session_state.datasource)
    
    
if __name__ == '__main__':
    main()