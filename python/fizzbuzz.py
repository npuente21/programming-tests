# Aquí programa una función que resuelva el problema 1 FizzBuzz

def fizzbuzz(n):
    cases = {
        3: "Fizz",
        5: "Buzz",
    }
    for number in range(1, n+1):
        string = ""
        for case in cases.keys():
            if number % case == 0:
                string += cases[case]
        if string:
            print(f'{number}: {string}')


# Ejemplo de uso
fizzbuzz(100)
