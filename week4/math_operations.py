def basic_operations(x, y):
    _sum = x+y
    difference = x-y
    product = x*y

    try:
        x/y
    except ZeroDivisionError:
        print("Raised ZeroDivisionError Error: Re-enter a value for the divider")
        y = int(input())
    finally:
        quotient = x/y


    return {"sum":_sum, "difference":difference, "product":product, "quotient":quotient}


def power_operation(base, exp, **kwargs):
    print(kwargs)
    result = base**exp;

    try:
        base % kwargs["modulo"]
    except KeyError:
        return {"power_result":result}
    else:
        mod = base % kwargs["modulo"]

        return {"power_result":result, "modulo":mod}


def apply_operations(tups):
    # [(func, [i,j, k])]
    answers = []


    for func, pars in tups :
        ans = list( map( func, [pars[0]], [pars[1]] ) )
        answers.append(ans)

    return answers
# print(apply_operations([(basic_operations, [1,2] ), (basic_operations, [1,4] )]))
