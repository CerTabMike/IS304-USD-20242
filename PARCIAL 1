#Michael Steven Taborda Ceron 
#18 de septiembre del 2024

class PrimeFinder:
    def __init__(self, limit):
        self._limit = limit  

    def _is_prime(self, num):
        """Método privado para verificar si un número es primo."""
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_primes(self):
        """Método público para encontrar y devolver los números primos menores que el límite."""
        primes = []
        for num in range(2, self._limit):
            if self._is_prime(num):
                primes.append(num)
        return primes

def main():
    try:
        user_input = int(input("Ingresa un número: "))
        prime_finder = PrimeFinder(user_input)
        primes = prime_finder.find_primes()
        print(f"Números primos menores que {user_input}: {primes}")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()
