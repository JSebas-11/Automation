from os.path import isdir

#---------------------------PathVerifier CLASS---------------------------
#Clase para comprobar que la ruta destino exista
class PathVerifier:
    @staticmethod
    def valid_path(path: str) -> bool:
        return isdir(path)