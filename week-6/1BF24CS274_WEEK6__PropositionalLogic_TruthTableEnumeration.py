
from itertools import product

print("P\tQ\tR\tQ->R\tP->~Q\tQ OR R\tKB")

for P, Q, R in product([True, False], repeat=3):
    
    a = (not Q or R)       
    b = (not P or not Q)   
    c = (Q or R)           
    KB = a and b and c

    # Print truth table
    values = [P, Q, R, a, b, c, KB]
    result = ["T" if x else "F" for x in values]

    print("\t".join(result))
