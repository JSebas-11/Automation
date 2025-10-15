from typing import Self
from pandas import isna
from Utilities.JoinDniInfo import JoinDniInfo

#---------------------------EMPLOYEE CLASS---------------------------
#Clase base de los empleados
class Employee:
    #----------------------attrs-----------------------
    def __init__(self):
        self.name: str | None = None
        self.role: str | None = None
        self.dni_number: str | None = None
        self.dni_source: str | None = None
        self.dni_full: str | None = None
        self.supervisor: str | None= None
        self.supervisor_genre: str | None = None
        
#---------------------------EMPLOYEE CLASS BUILDER---------------------------
#Builder para clase Employee, que hara cierta limpieza y comprobacion a los datos
class EmployeeBuilder:
    #----------------------attrs-----------------------
    def __init__(self):
        self._employee = Employee()
        
    #----------------------methods-----------------------
    def build(self) -> Employee:
        return self._employee
    
    def with_name(self, name: str) -> Self:
        if name == "":
            raise ValueError("Name can't be empty")
        
        self._employee.name = name
        return self
    
    def with_role(self, role: str) -> Self:
        if isna(role):
            self._employee.role = " " 
        else:            
            self._employee.role = role
        return self
    
    def with_dni_info(self, number: str, source: str) -> Self:
        if number == "":
            raise ValueError("Number can't be empty")
        
        self._employee.dni_number = number
        self._employee.dni_source = source
        self._employee.dni_full = JoinDniInfo.join_dni_info(number, source)
        return self
    
    def with_supervisor_info(self, name: str, genre: str) -> Self:
        if name == "" or genre == "":
            raise ValueError("Neither Name nor Genre can't be empty")
        
        self._employee.supervisor = name
        self._employee.supervisor_genre = genre
        return self