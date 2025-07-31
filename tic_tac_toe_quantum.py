def quantum_calculation():
    """
    Quantum simulator that returns binary array
    """
    from qiskit import QuantumCircuit, transpile
    from qiskit_aer import AerSimulator
    simulator = AerSimulator()
    k = []
    for x in range(4):
        circut = QuantumCircuit(1,1)
        circut.h(0)
        circut.measure([0],[0])
        compile = transpile(circut,simulator)
        job = simulator.run(compile,shots=1)
        res = job.result()
        count = res.get_counts(compile)
        k.append(count)
    k1 = ""
    for x in range(len(k)):
        k1 += str(k[x])
    j = 2
    new = []
    for x in range(len(k)): 
        new.append(int(k1[j]))
        j += 8
    return new    

def szybkie_wyliczanie(new):
    """
    Converting from binary to decimal
    """
    op = 0
    for x in range(len(new)):
        if(new[x] == 1):
            op+=2**x
    return op

def quick_repair(result):
    if(result > 8):
        result = int(result/2)
    return result

def SI():
    result1 = quantum_calculation()
    result2=szybkie_wyliczanie(result1) 
    result2 = quick_repair(result2)
    return result2

def draw(table):
    """
    Draw checking
    """
    if((table[0] != '0') and (table[1] != '1') and (table[2] != '2') and (table[3] != '3') and (table[4] != '4') and (table[5] != '5') and (table[6] != '6') and (table[7] != '7') and (table[8] != '8')):
            print("Draw")
            return True
    else:
        return False


def main_tic():
    """
    main function 
    """
    a1 = 48
    player1,player2,mode0 = 0,0,0
    table = []
    for i in range(0,9):
        table.append(chr(a1))
        a1 += 1
    print("Choose game mode")
    mode0 = int(input("1 player(1)\n: "))

    if(mode0 == 1):
        end = False
        print("-------")
        print(f"|{table[0]}|{table[1]}|{table[2]}|")
        print(f"|{table[3]}|{table[4]}|{table[5]}|")
        print(f"|{table[6]}|{table[7]}|{table[8]}|")
        print("-------")
        while(end == False):
            #player1
            try0 = False
            while((try0 == False) and (end == False)):
                player1 = int(input("Your move\n: "))
                for x in range(0,9):
                    if(player1 == x):
                        if(table[x] == 'X' or table[x] == 'O'):
                            print("Place is taken")
                            if(draw(table) == True):
                                exit()
                        else:
                            table[x] = 'X'
                            try0 = True
                        break
            if((table[0] == 'X') and (table[3] == 'X') and (table[6] == 'X')):
                print("WIN")
                end = True
            elif((table[0] == 'X') and (table[1] == 'X') and (table[2] == 'X')):
                print("WIN")
                end = True
            elif((table[3] == 'X') and (table[4] == 'X') and (table[5] == 'X')):
                print("WIN")
                end = True
            elif((table[6] == 'X') and (table[7] == 'X') and (table[8] == 'X')):
                print("WIN")
                end = True
            elif((table[1] == 'X') and (table[4] == 'X') and (table[7] == 'X')):
                print("WIN")
                end = True
            elif((table[2] == 'X') and (table[5] == 'X') and (table[8] == 'X')):
                print("WIN")
                end = True
            elif((table[6] == 'X') and (table[4] == 'X') and (table[2] == 'X')):
                print("WIN")
                end = True
            elif((table[0] == 'X') and (table[4] == 'X') and (table[8] == 'X')):
                print("WIN")
                end = True
            #player2
            try1 = False
            while((try1 == False) and (end == False)):
                player2 = SI()
                for x in range(0,9):
                    if(player2 == x):
                        if(table[x] == 'X' or table[x] == 'O'):
                            if(draw(table) == True):
                                exit()
                        else:
                            table[x] = 'O'
                            try1 = True
                        break
            if((table[0] == 'O') and (table[3] == 'O') and (table[6] == 'O')):
                print("LOSE")
                end = True
            elif((table[0] == 'O') and (table[1] == 'O') and (table[2] == 'O')):
                print("LOSE")
                end = True
            elif((table[3] == 'O') and (table[4] == 'O') and (table[5] == 'O')):
                print("LOSE")
                end = True
            elif((table[6] == 'O') and (table[7] == 'O') and (table[8] == 'O')):
                print("LOSE")
                end = True
            elif((table[1] == 'O') and (table[4] == 'O') and (table[7] == 'O')):
                print("LOSE")
                end = True
            elif((table[2] == 'O') and (table[5] == 'O') and (table[8] == 'O')):
                print("LOSE")
                end = True
            elif((table[6] == 'O') and (table[4] == 'O') and (table[2] == 'O')):
                print("LOSE")
                end = True
            elif((table[0] == 'O') and (table[4] == 'O') and (table[8] == 'O')):
                print("LOSE")
                end = True
            print("-------")
            print(f"|{table[0]}|{table[1]}|{table[2]}|")
            print(f"|{table[3]}|{table[4]}|{table[5]}|")
            print(f"|{table[6]}|{table[7]}|{table[8]}|")
            print("-------")
    else:
        print("Wrong value")


if(__name__=="__main__"):
    main_tic()



