from typing import List
import pandas as pd
from pandas import DataFrame
from Models.Employee import Employee, EmployeeBuilder
from Models.Contract import Contract, ContractBuilder
from Models.FinalContract import FinalContract, FinalContractBuilder

#---------------------------DATASOURCE CLASS---------------------------
#Clase que recolectara los datos de la fuente y convertira a los tipos correspondiente
class DataSource:
    #----------------------attrs-----------------------
    def __init__(self):
        self.data: DataFrame = DataFrame()
        self.raw_data: DataFrame = DataFrame()
        
    #----------------------methods-----------------------
    def load(self) -> bool:
        try:
            self.data = pd.read_csv("DataSources\\finalData.csv")
            self.raw_data = pd.read_excel("DataSources\\rawData.xlsx")
            return True
        except Exception as e:
            print(f"There has been an error loading data in DataSource-load: {e}")
            return False
        
    def get_final_cts(self) -> List[FinalContract]:
        employees: List[Employee] = self.get_employees()
        contracts: List[Contract] = self.get_contracts()
        final_contracts: List[FinalContract] = []
        
        for emp, cont in zip(employees, contracts):
            final_cont: FinalContract = (
                FinalContractBuilder()
                .with_contract(cont)
                .with_employee(emp)
                .build()
            )
            final_contracts.append(final_cont)
        
        return final_contracts    
    
    def get_employees(self) -> List[Employee]:
        employees: List[Employee] = []
        for row in self.data.itertuples(index=False):
            employee: Employee = (
                EmployeeBuilder()
                .with_name(row.employee_name)
                .with_role(row.role)
                .with_dni_info(row.employee_dni, row.dni_source)
                .with_supervisor_info(row.overseer_name, row.overseer_genre)
                .build()
            )
            employees.append(employee)
        
        return employees
    
    def get_contracts(self) -> List[Contract]:
        contracts: List[Contract] = []
        for row in self.data.itertuples(index=False):
            contract: Contract = (
                ContractBuilder()
                .with_number(row.cto_number)
                .with_legal_info(row.cto_class, row.cto_object)
                .with_initial_value(row.cto_initial_value)
                .with_added_value(row.cto_added_value)
                .with_final_value(row.cto_final_value)
                .build()
            )
            contracts.append(contract)
        
        return contracts