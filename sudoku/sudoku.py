mat=[]


def citirefisier():
    global mat
    for linie in range(9):
        x=list(map(int, f.readline().strip().split()))
        mat.append(x)

def citiretast():
    global mat
    for x in range(9):
        x=list(map(int, input(f"elementele de pe linia {x+1}: ").strip().split()))
        mat.append(x)

def afisare():
    global mat
    for linie in mat:
        print(linie)
        
        

def rezolvare():
    global mat
    coord=[0,0]
    if not gasesteliber(coord):
        return True
    else:
        i,j=coord
        for nr in range (1,10):
            if posibil(i,j,nr):
                mat[i][j]=nr
                if rezolvare():
                    return True
                mat[i][j]=0


def gasesteliber(t):
    global mat
    for i in range (9):
        for j in range (9):
            if mat[i][j]==0:
                t[0], t[1]= i, j
                return True
    return False
        
        
def posibil(lin,col,nr):
    return linie(lin,nr) and coloana(col,nr) and caseta(lin,col,nr)    
                
def linie(lin,nr):
    global mat
    for j in range (9):
        if mat[lin][j]==nr:
            return False
    return True

def coloana(col,nr):
    global mat
    for i in range (9):
        if mat[i][col]==nr:
            return False
    return True

def caseta(lin,col,nr):
    global mat
    i0=lin-lin%3
    j0=col-col%3
    for i in range(3):
        for j in range (3):
            if mat[i0+i][j0+j]==nr:
                return False
    return True

while 1:
    f=open ("sudoku.txt" ,  "r")
    print("C - citeste date de la tastatura")
    print("F - citeste date din fisier")
    print("A - afiseaza matricea dealului")
    print("R - rezolva problema")
    print("I - info autor")
    print("T - termina")
    opt=input("Optiunea dumneavoastra: ")
    match opt:
        case 'C':
            citiretast()
        case 'F':
            citirefisier()
        case 'A':
            afisare()
            x=input("apasati tasta D daca doriti stergerea matricei: ")
            if x=='D':
                del(mat)
            mat=[]
        case 'R':
            rezolvare()
        case 'I':
            print("nume: Bucsa Mathias")
            print("Grupa: 3112 A")
        case 'T':
            exit(0)