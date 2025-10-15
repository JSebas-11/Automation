from typing import List
from Utilities.StreamlitUtilities import StreamlitUtilities as stUtl
from streamlit.delta_generator import DeltaGenerator
from Services.DataMetrics import DataMetrics

class Metrics:
    @staticmethod
    def draw(base: DeltaGenerator, data_metrics: DataMetrics) -> None:
        base.html(stUtl.section_title("📊 General Metrics"))
        
        #Basic Info
        simple_metrics = base.columns([2, 1, 2])
        simple_metrics[1].html(stUtl.simple_metric_card("📄", "Contratos totales", data_metrics.total_cts))
        
        #Values Info
        cols = base.columns([1, 3, 3, 3, 1], gap="large")
        prices_metrics = [cols[1], cols[2], cols[3]]
        
        for i, (metric, stats) in enumerate(data_metrics.cts_values_info.items()):
            prices_metrics[i].html(
                stUtl.value_metric_card("💰", metric, stats['total'], stats['avg'], stats['min'], stats['max'])
            )
            
        #By Categories Info
        expanders: List[DeltaGenerator] = [
            base.expander("Total por Clase de Contrato", icon="🏷️"), base.expander("Total por Rol", icon="👥"),
            base.expander("Total por Origen de Empleado", icon="🌐"), base.expander("Total por Supervisor", icon="👔")
        ]
        
        stUtl.df_metrics(expanders[0], data_metrics.cts_class_count)
        stUtl.df_metrics(expanders[1], data_metrics.cts_roles_count)
        stUtl.df_metrics(expanders[2], data_metrics.dni_src_count)
        stUtl.df_metrics(expanders[3], data_metrics.cts_supervisor_count)