import argparse




parser = argparse.ArgumentParser(description='pgrepwc')
parser.add_argument('-c', action="store_true", help= 'counts the number of isolated occurrences of the word your searching')
parser.add_argument('-l', action="store_true", help= 'counts the number of lines where one or more occurrences of the word your searching')
parser.add_argument('-p', type=int, help= 'number of process/threads that will be created to run the search')
parser.add_argument('-t', action="store_true", help= 'option that forces the use of threads (by default using processes)')
parser.add_argument('-e', action="store_true", help= 'turns on special paralelization mode. If multiple files are indicated, this option is ignored')
parser.add_argument('palavra', type=str, help= 'The word searched in the files content')
parser.add_argument('ficheiros', type=str, nargs='+', help= 'You can add one or more files')
args= parser.parse_args()

if args.c==True:
    print('mu')
else:
    print('nao')



