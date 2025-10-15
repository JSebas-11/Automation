from typing import List
from Utilities.StreamlitUtilities import StreamlitUtilities as stUtl
from streamlit.delta_generator import DeltaGenerator
from Services.DataSource import DataSource

class Data:
    @staticmethod
    def draw(base: DeltaGenerator, data_src: DataSource) -> None:
        base.html(stUtl.section_title("🗂️ Data Sources"))
        
        expanders: List[DeltaGenerator] = [
            base.expander("Datos limpios (csv)", icon="🔹"), base.expander("Datos crudos (xlsx)", icon="🗃️")
        ]
        
        expanders[0].dataframe(data_src.data)
        expanders[1].dataframe(data_src.raw_data)