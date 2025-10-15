from pandas import isna

#---------------------------JoinDniInfo CLASS---------------------------
#Clase para converger el dni number con el source con el correspondiente formato
class JoinDniInfo:
    @staticmethod
    def join_dni_info(number: str, src: str | None) -> str:
        sep_number: str = f"{int(number):,}".replace(",", ".")
        
        if isna(src) or src == "":
            return sep_number
        
        return f"{sep_number} DE {src}"