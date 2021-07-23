#Primero introduzco una N que son la cantidad de operaciones a realizar
#Despues pongo la lista de operaciones


if __name__ == '__main__':
    N = int(input())
    lista = []
    for _ in range(N):
        comando = input()
        lcomando = comando.split(" ")
        print(lcomando)
        if lcomando[0]=="insert": lista.insert(int(lcomando[1]),int(lcomando[2]))
        elif lcomando[0]=="print": print(lista)
        elif lcomando[0]=="remove": lista.remove(int(lcomando[1]))
        elif lcomando[0]=="append": lista.append(int(lcomando[1]))
        elif lcomando[0]=="sort": lista.sort()
        elif lcomando[0]=="pop": lista.pop()
        elif lcomando[0]=="reverse": lista.reverse()
