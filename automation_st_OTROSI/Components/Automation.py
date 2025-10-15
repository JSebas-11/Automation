import streamlit as st
from typing import List
from streamlit.delta_generator import DeltaGenerator
from Services.DataService import DataService
from Models.FinalContract import FinalContract
from Utilities.StreamlitUtilities import StreamlitUtilities as stUtl
from Utilities.PathVerifier import PathVerifier

class Automation:
    @staticmethod
    def draw(base: DeltaGenerator, data_service: DataService) -> None:
        #----------------------VARS-----------------------
        if 'data_ctos' not in st.session_state:
            st.session_state.data_ctos = []
        
        if 'ready_ctos_num' not in st.session_state:
            st.session_state.ready_ctos_num = 0
        
        if 'ctos_loaded' not in st.session_state:
            st.session_state.ctos_loaded = False
        
        if 'ctos_results' not in st.session_state:
            st.session_state.ctos_results = []
        
        target_path: str = ""
        incorrect_path: bool = True
        generate_btn_disabled: bool = True
        
        #----------------------HEADER (INFO-CARGAR)-----------------------
        base.html(stUtl.section_title("🛠️ Docx format and variables"))
        base.write(f"{st.session_state.ready_ctos_num} ctos listos para ser generados")
        
        placeholder_btn = base.empty()
        placeholder_df = base.empty()
        
        if placeholder_btn.button("Cargar contratos", type="primary", icon=stUtl.matl_icn("upload"), disabled=st.session_state.ctos_loaded):
            contracts: List[FinalContract] | None = data_service.load_contracts()
            
            if contracts is None:
                st.warning("Ha habido un error cargando los archivos con los datos. Revisa el error en la consola", icon="⚠️")
            else:
                st.session_state.ready_ctos_num = len(contracts)
                st.session_state.data_ctos = contracts
                st.session_state.ctos_loaded = True
                placeholder_df.dataframe([contract.to_dict() for contract in contracts])
                st.rerun()
        
        if st.session_state.ctos_loaded and st.session_state.data_ctos:
            placeholder_df.dataframe([c.to_dict() for c in st.session_state.data_ctos])
        
        #----------------------MAIN (PATH-BTN)-----------------------
        target_path = base.text_input(f"Ruta destino (Carpeta): {target_path}", placeholder=fr"C:\User\OTROSI", icon=stUtl.matl_icn("folder"))
        
        if (PathVerifier.valid_path(target_path)):
            incorrect_path = False
            st.toast("Ruta Correcta!", icon="✅")
        else:
            st.toast("Ruta Incorrecta o Nula", icon="❌")
        
        generate_btn_disabled = (not st.session_state.ctos_loaded) or (incorrect_path)
        
        if base.button("Generar OTROSI", type="primary", icon="🚀", disabled=generate_btn_disabled):
            ctos: List[FinalContract] = st.session_state.data_ctos
            size: int = len(ctos)
            
            base.write("Resultados:")
            progress_bar = base.progress(0)
            progress_txt = base.empty()
            
            for i, contract in enumerate(ctos, 1):
                progress_txt.text(f"Creando contrato {i}/{size} - ({contract.number} - {contract.emp_name})")
                st.session_state.ctos_results.append(data_service.create_docx_file(contract, target_path))
                progress_bar.progress(int(i/size*100))

            base.info("Creacion de contratos finalizada")
        
        #----------------------FOOTER (RESULTS)-----------------------
        placeholder_result = base.empty()
        if len(st.session_state.ctos_results) > 0:
            expander = placeholder_result.expander("Results", True, icon="👁‍🗨")
            for result in st.session_state.ctos_results:
                expander.html(stUtl.result_card(result))
        
        