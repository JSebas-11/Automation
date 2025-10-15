from typing import Self, Any, Dict
from Models.Contract import Contract
from Models.Employee import Employee

#---------------------------FINAL CONTRACT CLASS---------------------------
#Clase para usar en la UI con toda la informacion recolectada de Employee y Contract
class FinalContract:
    #----------------------attrs-----------------------
    def __init__(self):
        self.number: int
        self.cont_class: str | None
        self.cont_object: str | None
        self.initial_value: str | None
        self.added_value: str | None
        self.final_value: str | None
        self.emp_name: str | None
        self.emp_role: str | None
        self.emp_dni: str | None
        self.supervisor: str | None
        self.supervisor_genre: str | None
        
    #----------------------methods-----------------------
    def to_dict(self) -> Dict[str, Any]:
        return {
            'number': self.number, 'cont_class': self.cont_class, 'cont_object': self.cont_object,
            'initial_value': self.initial_value, 'added_value': self.added_value, 'final_value': self.final_value,
            'emp_name': self.emp_name, 'emp_role': self.emp_role, 'emp_dni': self.emp_dni,
            'supervisor': self.supervisor, 'supervisor_genre':self. supervisor_genre
        }
    
    def get_attr_by_var_name(self, var_name: str) -> Any:
        mapping: Dict[str, Any] = {
            "ctoNumber": self.number,
            "ctoClass": self.cont_class,
            "ctoObject": self.cont_object,
            "ctoInitialValue": self.initial_value,
            "ctoAddedValue": self.added_value,
            "ctoFinalValue": self.final_value,
            "employeeName": self.emp_name,
            "employeeRole": self.emp_role,
            "employeeDni": self.emp_dni,
            "employeeOverseerGenre": self.supervisor_genre,
            "employeeOverseerName": self.supervisor
        }
        
        return mapping.get(var_name, "")
        
#---------------------------FinalCONTRACT CLASS BUILDER---------------------------
#Builder para clase FinalContract, que hara el mappeo con los objetos Employee y Contract
class FinalContractBuilder:
    #----------------------attrs-----------------------
    def __init__(self):
        self._final_contract = FinalContract()
        
    #----------------------methods-----------------------
    def build(self) -> FinalContract:
        return self._final_contract
        
    def with_contract(self, contract: Contract) -> Self:
        #Asignar propiedades de objeto Contract (esto asegura que ya cumplio las validaciones)
        self._final_contract.number = contract.number
        self._final_contract.cont_class = contract.cont_class
        self._final_contract.cont_object = contract.cont_object
        self._final_contract.initial_value = contract.initial_value
        self._final_contract.added_value = contract.added_value
        self._final_contract.final_value = contract.final_value
        
        return self
    
    def with_employee(self, employee: Employee) -> Self:
        #Asignar propiedades de objeto Employee (esto asegura que ya cumplio las validaciones)
        self._final_contract.emp_name = employee.name
        self._final_contract.emp_role = employee.role
        self._final_contract.emp_dni = employee.dni_full
        self._final_contract.supervisor = employee.supervisor
        self._final_contract.supervisor_genre = employee.supervisor_genre
        
        return self
    