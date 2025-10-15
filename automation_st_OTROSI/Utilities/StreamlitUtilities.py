from typing import Any
from pandas import DataFrame
from streamlit.delta_generator import DeltaGenerator
from Utilities.CreationResult import CreationResult

#---------------------------StreamlitUtilities CLASS---------------------------
#Clase con variables y metodos auxiliares para la UI
class StreamlitUtilities:
    #----------------------attrs-----------------------
    clr_primary = "#FF4B4B"
    clr_txt = "#FAFAFA"
    clr_bg_main = "#0E1117"
    clr_bg_sec = "#262730"
    
    #----------------------methods-----------------------
    @staticmethod
    def matl_icn(name: str) -> str:
        return f":material/{name}:"
    
    #----------------------templates meths-----------------------
    @staticmethod
    def section_title(title: str) -> str:
        return f"""
            <h1 style="font-size: 32px; color: {StreamlitUtilities.clr_primary};
                padding-left: 10px; border-left: 4px solid {StreamlitUtilities.clr_primary}; margin: 0 10px; 
                display: inline-block;">
            {title}
            </h1>
        """
    
    @staticmethod
    def simple_metric_card(icon: str, metric_name: str, value: Any) -> str:
        return f"""
            <div style="width: 240px; background: {StreamlitUtilities.clr_bg_sec}; border: 1px solid {StreamlitUtilities.clr_primary}; 
                border-radius: 8px; padding: 16px; 
                display: flex; align-items: center; gap: 12px;">

                <div style="width: 40px; height: 40px;
                  display: flex; align-items: center; justify-content: center;
                  border-radius: 6px; background: {StreamlitUtilities.clr_primary}; font-size: 22px;">
                {icon}
                </div>

                <div style="display: flex; flex-direction: column;">
                  <span style="font-size: 15px; color: {StreamlitUtilities.clr_primary};">{metric_name}</span>
                  <span style="font-size: 20px; font-weight: bold; color: {StreamlitUtilities.clr_primary};">{str(value)}</span>
                </div>

            </div>
        """
    
    @staticmethod
    def value_metric_card(icon: str, metric_name: str, total: Any, avg: Any, min: Any, max: Any) -> str:
        return f"""
            <div style="width: 260px; background: {StreamlitUtilities.clr_bg_sec}; 
                border: 1px solid {StreamlitUtilities.clr_primary}; border-radius: 10px; padding: 14px 18px; 
                display: flex; align-items: flex-start; gap: 14px;">
                
                <div style=" width: 44px; height: 44px; 
                    display: flex; align-items: center; justify-content: center; 
                    border-radius: 8px; background: {StreamlitUtilities.clr_primary}; font-size: 22px;">
                    {icon}
                </div>

                <div style="display: flex; flex-direction: column; gap: 4px;">
                    <span style="font-size: 15px; font-weight: 600; color: {StreamlitUtilities.clr_primary};">
                        {metric_name}
                    </span>

                    <div style="font-size: 14px; color: {StreamlitUtilities.clr_txt}; line-height: 1.4;">
                        <div>🔢 <b>Total:</b> ${total}</div>
                        <div>⚖️ <b>Promedio:</b> ${avg}</div>
                        <div>📉 <b>Min:</b> ${min}</div>
                        <div>📈 <b>Max:</b> ${max}</div>
                    </div>
                </div>
            </div>
        """
    
    @staticmethod
    def df_metrics(base: DeltaGenerator, df: DataFrame) -> None:
        for row in df.itertuples(index=False):
            base.markdown(f"""
                <div style=" display: flex; align-items: center; justify-content: space-between;
                    background: {StreamlitUtilities.clr_bg_sec}; border: 1px solid {StreamlitUtilities.clr_primary}; 
                    border-radius: 8px; padding: 10px 16px;">
                    <span style="font-size: 15px; color: {StreamlitUtilities.clr_txt};">{row[0]}</span>
                    <span style="font-size: 18px; font-weight: bold; color: {StreamlitUtilities.clr_primary};">{row.count}</span>
                </div>
            """, unsafe_allow_html=True)
    
    @staticmethod
    def result_card(result: CreationResult) -> str:
        if result.success:
            icon = "✅"
            border_color = "#66A140"
        else:
            icon = "❌"
            border_color = "#aa1122"

        exception_html = f"<div>⚠️ <b>Error:</b> {result.exception_msg}</div>" if result.exception_msg else ""
        
        return f"""
            <div style="background: {StreamlitUtilities.clr_bg_sec}; 
                border: 1px solid {border_color}; border-radius: 10px; padding: 14px 18px; 
                display: flex; align-items: flex-start; gap: 14px;">

                <div style="width: 44px; height: 44px; 
                    display: flex; align-items: center; justify-content: center; 
                    border-radius: 8px; background: {border_color}; font-size: 22px;">
                    {icon}
                </div>

                <div style="display: flex; flex-direction: column; gap: 4px;">
                    <span style="font-size: 15px; font-weight: 600; color: {border_color};">
                        Resultado
                    </span>

                    <div style="font-size: 14px; color: {StreamlitUtilities.clr_txt}; line-height: 1.4;">
                        <div>ℹ️ <b>Descripción:</b> {result.msg}</div>
                        {exception_html}
                    </div>
                </div>
            </div>
        """