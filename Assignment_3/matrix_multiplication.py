import MapReduce
import sys

"""
Matrix Multiplication in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    for i in range(5):
        if key == "a":
            mr.emit_intermediate((record[1],i),(record[2],record[3]))
        if key == "b":
            mr.emit_intermediate((i,record[2]),(record[1],record[3]))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    a_value_dict = {}
    b_value_dict = {}
    for v in list_of_values:
        if v[0] in a_value_dict:
            b_value_dict[v[0]]=v[1]	
        else:
            a_value_dict[v[0]]=v[1]
    for k in b_value_dict.keys():
        total = total + b_value_dict[k]*a_value_dict[k];
    mr.emit((key[0],key[1],total));

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
