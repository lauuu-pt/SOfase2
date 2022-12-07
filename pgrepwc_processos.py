### Grupo: SO-TI-09
### Aluno 1: Henrique Venâncio (fc58618)
### Aluno 2: Laura Tomás (fc58641)
### Aluno 3: Tomás Alves (fc58633)

import sys
import os
from multiprocessing import Process
import argparse

parser = argparse.ArgumentParser(description='pgrepwc')
parser.add_argument('-c', action="store_true", help= 'counts the number of isolated occurrences of the word your searching')
parser.add_argument('-l', action="store_true", help= 'counts the number of lines where one or more occurrences of the word your searching')
parser.add_argument('-p', type=int, help= 'number of process/threads that will be created to run the search')
parser.add_argument('-e', action="store_true", help= 'turns on special paralelization mode. If multiple files are indicated, this option is ignored')
parser.add_argument('palavra', type=str, help= 'The word searched in the files content')
parser.add_argument('ficheiros', type=str, nargs='+', help= 'You can add one or more files')
args= parser.parse_args()


        
            
def procuraPalavra(ficheiros, palavra):
    count=0
    for ficheiro in ficheiros:
        with open(ficheiro, 'r') as f:
            for linha in f:
                if palavra in linha:
                    count+=1
    return count


def main(args):
    print('Programa: pgrepwc_processos.py')
    print('Argumentos: ',args)

if __name__ == "__main__":
    main(sys.argv[1:])
    
#def ordena(lista):
#    L=[]

if args.c==True:
    print(procuraPalavra(args.ficheiros, args.palavra))
    if args.l==True:
        print('yas')
