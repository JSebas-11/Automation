from num2words import num2words

#---------------------------NumToWord CLASS---------------------------
#Clase para convertir numero a letras
class NumToWords:
    @staticmethod
    def num2word(number: int) -> str:
        num_as_word: str = num2words(number, lang="es")
        #Ajustes al resultado
        if num_as_word.endswith("mil"):
            num_as_word += " pesos ml"
        elif num_as_word.endswith("millones") or num_as_word.endswith("millón"):
            num_as_word += " de pesos ml"
        
        num_as_word += f" (${number:,})"
        
        return num_as_word.upper()