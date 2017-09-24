import MapReduce
import sys

"""
Friend Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    """
    Here to understand an asymmetric Friend Count
    key value pair is generated for all friends.
    Hence, as the friendships are counted twice, the ones with only one friend
    are asymmetric ones.
    
    """
    for i in range(len(record)):
    	mr.emit_intermediate(record[i],record[1-i])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    for v in list_of_values:
      if list_of_values.count(v)==1:
          mr.emit((key, v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
