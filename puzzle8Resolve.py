from Puzzle8 import Sudoku
from Fila import Fila
from datetime import datetime



#Set inicial do Sudoku
su = Sudoku([2,8,7,
             5,4,1,
             6,3,0]);


def puzzle8Resolve(su):
    data_atual = datetime.now()
    hora = data_atual.strftime('%H:%M:%S')
    print(hora)

    hashs = set();



    fi = Fila();


    fi.add(su);

    cont = 0
    while True:

        try:
            suAnalizado = fi.remove();
        except:
            break;

        if suAnalizado.inOrder() == True:
            break;
        else:

            for sudokus in suAnalizado.moves():

                if (sudokus.__hash__() in hashs) == False:
                    fi.add(sudokus)

                hashs.add(sudokus.__hash__())

            cont += 1

    print('%s estados analisados, resultado:' %(cont))
    if 181441 <= cont:
        print("Formatação sem solução")
    else:
        suAnalizado.historia()
    data_atualf = datetime.now()
    horaf = data_atualf.strftime('%H:%M:%S')
    print(horaf)



puzzle8Resolve(su)


