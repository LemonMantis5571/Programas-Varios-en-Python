
def vida():
        vida.vidas = 5
        vida.adivinadas = ["Chaeyoung","Turca"]

def prueba():
    print("prueba 1")
    print(vida.vidas)
    print(vida.adivinadas)

        



def function_1():
    # assigning a string as a member of the function object
    function_1.var = "variable inside function_1"
    print("function_1 has been called")

def function_2():
    print("function_2 has been called")
    print(function_1.var)

function_1()
function_2()
vida()
prueba()