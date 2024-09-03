'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
# Michael Steven Taborda Ceron 
# Solucion tarea
class CuentaBancaria:
    def __init__(self, numeroCta, nombreCliente, fechaApertura, saldoInicial=0):
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__fechaApertura = fechaApertura
        if saldoInicial < 100000:
            raise ValueError("Saldo incial > 100000")
        self.__saldo = saldoInicial
        
    def get_numeroCta(self):
        return self.__numeroCta
    
    def get_nombreCliente(self):
        return self.__nombreCliente
    
    def get_fechaApertura(self):
        return self.__fechaApertura
    
    def get_saldo(self):
        return self.__saldo

    def consignar(self, monto):
        if monto <= 0:
            raise ValueError("Consignar: El monto debe ser positivo")
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("Retirar: El monto debe ser positivo")
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes")
        self.__saldo -= monto

def menu():
    while True:
        print("\nMenú de operaciones bancarias")
        print("1. Crear una nueva cuenta")
        print("2. Consultar saldo")
        print("3. Realizar consignación")
        print("4. Realizar retiro")
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            numeroCta = input("Número de cuenta: ")
            nombreCliente = input("Nombre del cliente: ")
            fechaApertura = input("Fecha de apertura: ")
            try:
                saldoInicial = float(input("Ingrese el saldo inicial: "))
                cuenta = CuentaBancaria(numeroCta, nombreCliente, fechaApertura, saldoInicial)
                print("Cuenta creada exitosamente.")
            except ValueError as e:
                print(e)
        elif opcion == 2:
            if 'cuenta' in locals():
                print(f"El saldo actual es: {cuenta.get_saldo()}")
            else:
                print("No hay ninguna cuenta creada.")
        elif opcion == 3:
            if 'cuenta' in locals():
                try:
                    monto = float(input("Monto a consignar: "))
                    cuenta.consignar(monto)
                    print("Consignación realizada exitosamente.")
                except ValueError as e:
                    print(e)
            else:
                print("No hay ninguna cuenta creada.")
        elif opcion == 4:
            if 'cuenta' in locals():
                try:
                    monto = float(input("Monto a retirar: "))
                    cuenta.retirar(monto)
                    print("Retiro realizado exitosamente.")
                except ValueError as e:
                    print(e)
            else:
                print("No hay ninguna cuenta creada.")
        elif opcion == 5:
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
  
