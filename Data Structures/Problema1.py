#Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a
#sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
#Write a function to help bob locate the card
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

def localizar_carta(cartas,query):
    position = 0

    while position < len(cartas):
        if cartas[position] == query:
            return position
        
        position +=1
    return -1




cartas = [13,11,10,7,4,3,1,0]
query = 7
output = 3

result = localizar_carta(cartas,query)
print(result)



prueba = {
        'input': {
            'cartas' : [13,11,10,7,4,3,1,0],
            'query': 7
        },
        'output': 3
}
localizar_carta(**prueba['input']) == prueba['output']

pruebas = []
pruebas.append(prueba)

pruebas.append({
    'input':  {
        'cartas' : [13,11,10,7,4,3,1,0],
        'query': 7
    },
    'output' : 3


})
#el numero aparece en el medio
pruebas.append(prueba)
pruebas.append({
    'input': {
        'cartas' : [13,11,10,7,4,3,1,0],
        'query' : 1
    },
    'output' : 6
})
#no contiene el numero seleccionado
pruebas.append({
    'input': {
        'cartas' : [9,7,5,2,-9],
        'query' : 4
    },
    'output' : -1
})
#el nombre mismo se repite en las cartas
pruebas.append({
    'input': {
        'cartas' : [8,8,6,6,6,6,3,2,2,2,0,0,0],
        'query' : 6
    },
    'output' : 2
})

#es el primer elemento
pruebas.append({
        'input' : {
            'cartas' : [3,-1,-9,-127],
            'query' : -127
        },
        'output' : 3

})
#la carta contienen solo 1 elemento
pruebas.append({
        'input' : {
            'cartas' : [6],
            'query' : 6
        },
        'output' : 0

})
#
pruebas.append({
        'input' : {
            'cartas' : [3,-1,-9,-127],
            'query' : -127
        },
        'output' : 3

})
#las cartas no contienen el requerido
pruebas.append({
        'input' : {
            'cartas' : [9,7,5,2,-9],
            'query' : -4
        },
        'output' : -1

})
#las cartas estan vacias
pruebas.append({
        'input' : {
            'cartas' : [],
            'query' : 7
        },
        'output' : -1

})

prueba
result = localizar_carta(prueba['input']['cartas'],prueba['input']['query'])
result
result == output

evaluate_test_case(localizar_carta,prueba)
for prueba in pruebas:
    print(localizar_carta(**prueba['input']) == prueba ['output'])
evaluate_test_cases(localizar_carta,pruebas)