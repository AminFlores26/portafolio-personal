#MATRICULA
APORTE DE AMIN FLORES
class Matricula:
    def __init__(self):
        self.__pago_al_dia = False   
        self.__matricula_activa = False
        self.__valor_matricula = 180

    def ingresar_pago(self):
        try:
            pago = float(input("INGRESE EL PAGO DE LA MATRICULA: "))
            if pago >= self.__valor_matricula:
                self.__pago_al_dia = True
                print("PAGO COMPLETO. ESTA AL DIA.")
            else:
                self.__pago_al_dia = False
                print("PAGO INSUFICIENTE.")
        except ValueError:
            print("DEBE INGRESAR UN VALOR VALIDO.")

    def activar_matricula(self):
        if self.__pago_al_dia:
            self.__matricula_activa = True
            print("MATRICULA ACTIVADA.")
        else:
            print("NO SE PUEDE ACTIVAR MATRICULA. PAGO PENDIENTE.")

    def estado_matricula(self):
        return self.__matricula_activa

#INGRESAR EL PAGO
m = Matricula()
m.ingresar_pago()
m.activar_matricula()

print("¿Matrícula activa?", m.estado_matricula())
