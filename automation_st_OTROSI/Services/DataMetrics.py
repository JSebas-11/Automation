from pandas import DataFrame
from typing import Dict

#---------------------------DATAMETRIC CLASS---------------------------
#Clase que recolectara informacion de la fuente de datos inyectada
class DataMetrics:
    #----------------------attrs-----------------------
    def __init__(self, dataSource: DataFrame):
        self.__dataSource: DataFrame = dataSource
        #Total de contratos registrados
        self.total_cts: int = 0
        #Clases, roles, dni origen y supervisores con su respectiva cantidad de resgitros
        self.cts_class_count: DataFrame = DataFrame()
        self.cts_roles_count: DataFrame = DataFrame()
        self.dni_src_count: DataFrame = DataFrame()
        self.cts_supervisor_count: DataFrame = DataFrame()
        #Para cada value (initial, added, final), tendra su columna con: Total, avg, min y max
        self.cts_values_info: Dict[str, Dict[str, str]] = {}
        
        self.__load_metrics()
    
    #----------------------methods-----------------------
    def __load_metrics(self) -> None:
        self.total_cts: int = self.__dataSource.shape[0]
        
        self.cts_class_count = self.__group_count('cto_class')
        self.cts_roles_count = self.__group_count('role')
        self.dni_src_count = self.__group_count('dni_source')
        self.cts_supervisor_count = self.__group_count('overseer_name')
        
        self.cts_values_info = {
            "Initial Value": self.__group_info('cto_initial_value'),
            "Added Value": self.__group_info('cto_added_value'),
            "Final Value": self.__group_info('cto_final_value')
        }
        
    #----------------------inner meths-----------------------
    def __group_count(self, col_name: str) -> DataFrame:
        return self.__dataSource[col_name].value_counts().reset_index(name='count')
    
    def __group_info(self, col_name: str) -> Dict[str, str]:
        col = self.__dataSource[col_name]
        return { 
            "total": f"{col.sum():,}", "avg": f"{round(col.mean(), 2):,}", "max": f"{col.max():,}", "min": f"{col.min():,}" 
        }