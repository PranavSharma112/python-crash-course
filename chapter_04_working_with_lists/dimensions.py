dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200, 50)
# dimensions[0] = 250

# to define an tuple with one element with one tuple define it with a trailing comma my_t = (3,)

# Writing Over a tuple 
dimensions = (200, 50)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Reassigning is allowed and that's the right way!

"""

Method	                            Description	Example
tuple.count(x)	                    Returns the number of times x appears in the tuple.	(1, 2, 2, 3).count(2) → 2
tuple.index(x[, start[, stop]])	    Returns the index of the first occurrence of x. Optional start and stop limit the search range.
 Raises ValueError if not found.	(10, 20, 30, 20).index(20, 2) → 3
"""