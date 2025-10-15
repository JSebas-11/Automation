from typing import Self
from Utilities.NumToWords import NumToWords

#---------------------------CONTRACT CLASS---------------------------
#Clase base de los contratos
class Contract:
    #----------------------attrs-----------------------
    def __init__(self):
        self.number: int = 0
        self.cont_class: str | None = None
        self.cont_object: str | None= None
        self.initial_value: str | None = None
        self.added_value: str | None = None
        self.final_value: str | None = None
        
#---------------------------CONTRACT CLASS BUILDER---------------------------
#Builder para clase Contract, que hara cierta limpieza y comprobacion a los datos
class ContractBuilder:
    #----------------------attrs-----------------------
    def __init__(self):
        self._contract = Contract()
        
    #----------------------methods-----------------------
    def build(self) -> Contract:
        return self._contract
        
    def with_number(self, number: int) -> Self:
        if number <= 0:
            raise ValueError("Contract number can't be negative")
        
        self._contract.number = number
        return self
    
    def with_legal_info(self, contract_class: str, contract_object: str) -> Self:
        if contract_class == "" or contract_object == "":
            raise ValueError("Both class and object can't be empty")
        
        self._contract.cont_class = contract_class
        self._contract.cont_object = contract_object
        return self
    
    def with_initial_value(self, initial_value: str) -> Self:
        is_correct, int_value = self.__number_value(initial_value)
        if not is_correct:
            raise ValueError("""There has been an error with Initial Value, possible issues:
                            \n-Parameter empty\n-Must be a number as a str\n-Value must be greater or equal than 0""")
        
        self._contract.initial_value = NumToWords.num2word(int_value)
        return self
    
    def with_added_value(self, added_value: str) -> Self:
        is_correct, int_value = self.__number_value(added_value)
        if not is_correct:
            raise ValueError("""There has been an error with Added Value, possible issues:
                            \n-Parameter empty\n-Must be a number as a str\n-Value must be greater or equal than 0""")
        
        self._contract.added_value = NumToWords.num2word(int_value)
        return self
    
    def with_final_value(self, final_value: str) -> Self:
        is_correct, int_value = self.__number_value(final_value)
        if not is_correct:
            raise ValueError("""There has been an error with Final Value, possible issues:
                            \n-Parameter empty\n-Must be a number as a str\n-Value must be greater or equal than 0""")
        
        self._contract.final_value = NumToWords.num2word(int_value)
        return self
        
    #----------------------inner methods-----------------------
    def __number_value(self, value: str) -> tuple[bool, int | None]:
        if value == "":
            return (False, None)
        
        try:
            value_num: int = int(value)
        except:
            return (False, None)
        
        if value_num < 0:
            return (False, None)
        
        return (True, value_num)
    