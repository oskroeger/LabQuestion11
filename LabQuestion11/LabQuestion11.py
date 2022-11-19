
# Owen Kroeger
# My Own Work

# Recursive
# 3a(n+1) - 4a(n) = 0
# 3a(n+1) = 4a(n)
# a(n+1) = 4/3a(n)

# Explicit
# a(n) = (5)*(4/3)^n

def recRelation():
    
    # n in explicit formula
    count = 0

    # recursive var
    an = 5.00

    # explicit var
    am = 0

    # temporary variables for rounding
    tempr = 0
    tempe = 0

    print("Recursive: \t Explicit: ")
    print("-----------------------------")
    for i in range(20):
        
        # run explicit formula
        am = 5*((4/3)**count)
        
        tempr = round(an, 2)
        tempe = round(am, 2)

        print(f'{tempr}\t\t {tempe}')

        # iterate both formulas 
        an = 4/3*an
        count += 1

recRelation()