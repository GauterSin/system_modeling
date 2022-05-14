from scipy.optimize import linprog


def _algo_1():

    func = [0, -3]
    system_equation_left = [
            [-4, -3],
            [3, 2]
        ]

    system_equation_right = [2, 12]
    x1_bnds = (0, None)
    x2_bnds = (0, None)
    res = linprog(
            func,
            system_equation_left,
            system_equation_right,
            bounds=(x1_bnds, x2_bnds),
            method="revised simplex")
    print(res)
    return res

def _algo_2():

    func = [0, -2]
    system_equation_left = [
            [-4, -3],
            [3, 2]
        ]

    system_equation_right = [2, 12]
    x1_bnds = (0, None)
    x2_bnds = (0, None)
    res = linprog(
            func,
            system_equation_left,
            system_equation_right,
            bounds=(x1_bnds, x2_bnds),
            method="revised simplex")
    print(res)
    return res

_algo_1()
_algo_2()
