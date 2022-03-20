def busqueda_while_instrumentalizado(x:int, a:[int]) -> int:
    contador_operaciones:int = 0
    p:int = 0
    contador_operaciones += 1 # '='
    while p < len(a):
        contador_operaciones += 2 # '<', 'len()'
        if a[p] == x:
            contador_operaciones += 2 # '==', '[]'
            return contador_operaciones
        else:
            p += 1
            contador_operaciones += 3 # '==', '[]', '+='
    return contador_operaciones
    
def test_busqueda_while_instrumentalizado(filename, inic:int, maxi:int, paso:int):
    file = open(filename, 'w')
    file.write('n;time\n')
    for i in range (inic, maxi, paso):
        array = list(range(i))
        x = i
        file.write(f'{i};{busqueda_while_instrumentalizado(x, array)}\n') #o file.write(str(i)+ ';' + busqueda_while_instrumentalizado(x, array) + '\n')
    file.close()

test_busqueda_while_instrumentalizado('test_busqueda_while_instrumentalizado.csv', 0, 100, 10)
