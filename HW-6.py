from typing import List
from contextlib import contextmanager


func_type = List[str]

@contextmanager
def file_opener(file_path: str, mode: str, process='moein'):

    open_file = open(file_path, mode)

    if mode == 'r':
        read_file = open_file.read()
        yield {read_file}
        
    elif mode == 'w' :
        open_file.writelines(process)
        yield{}
   
    open_file.close
    
    
def process_data(input_str) -> func_type:
    mylist = []
    for line in input_str:
        mylist.append(line + '\n')
    return mylist


input_file = 'data1.txt'
output_file = 'data2.txt'

result = None
with file_opener(input_file,'r') as reader :
    result = process_data(reader)
    result = ''.join(result)

with file_opener(output_file,'w', result) as write :
    print('objective completed ')
    