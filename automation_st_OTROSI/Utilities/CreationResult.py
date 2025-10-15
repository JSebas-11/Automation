from typing import Optional
from dataclasses import dataclass

#---------------------------CreationResult CLASS---------------------------
#Clase para mostrar resultado de la creacion de los archivos
@dataclass
class CreationResult:
    success: bool
    msg: str
    exception_msg: Optional[str] = None

    @staticmethod
    def ok(msg: str) -> "CreationResult":
        return CreationResult(True, msg)
    
    @staticmethod
    def fail(msg: str, exception_msg: Optional[str] = None) -> "CreationResult":
        return CreationResult(False, msg, exception_msg)
        