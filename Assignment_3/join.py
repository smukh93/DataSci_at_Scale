import MapReduce
import sys

"""
Implementation of Join Operation in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    mr.emit_intermediate(key,record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    order_list = []
    line_list  = []
    for v in list_of_values:
        if v[0]=="order":
            order_list=v
        else:
            line_list.append(v)
    for line in line_list:
    	mr.emit(order_list + line)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
