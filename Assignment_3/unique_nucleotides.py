import MapReduce
import sys

"""
Finding Unique Nucleotides in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    seq_id = record[0]
    nucleotide_trunc = record[1][:-10] 
    mr.emit_intermediate(0,nucleotide_trunc)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    unique_nucleotides = []
    for v in list_of_values:
      if v not in unique_nucleotides:
          unique_nucleotides.append(v)
    for u in unique_nucleotides:
	    mr.emit((u))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
