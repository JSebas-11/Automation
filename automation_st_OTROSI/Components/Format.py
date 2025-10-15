from typing import List
from Utilities.StreamlitUtilities import StreamlitUtilities as stUtl
from Services.DataService import DataService
from streamlit.delta_generator import DeltaGenerator

class Format:
    @staticmethod
    def draw(base: DeltaGenerator, data_service: DataService) -> None:
        base.html(stUtl.section_title("🛠️ Docx format and variables"))
        
        bytes_file = data_service.get_docx_bytes()
        col = base.columns([2, 1, 2])
        if not bytes_file is None:
            col[1].download_button("Descargar formato (.docx)", bytes_file, file_name="formato.docx", icon=stUtl.matl_icn("download"))
            
        expander: List[DeltaGenerator] = [base.expander("Contenido del formato (texto plano)"), base.expander("Variables")]
        expander[0].html(data_service.get_docx_as_html_txt())
        expander[1].markdown("\n".join([f"- {item}" for item in data_service.get_vars_list()]))
