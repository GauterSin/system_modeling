import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize



"""
Каменьщиков АА-19-05
Вариант 17 (пример 8)
"""

x1 = 0
x2 = 0

def func(
        x1: float,
        x2: float):
    return 45 * x1**2 - 88 * x1 * x2 + 45 * x2**2 + 102 * x1 + 268 * x2 - 21


def gradient_function(x1, x2):
    return np.array(
            [90 * x1 - 88 * x2 + 102],
            [-88 * x1 + 90 * x2 + 268]
            ) 


def task_2():
    
    return optimize.minimize(
            func,
            x1,
            x2,
            method='SLSQP')

print(task_2())



"""
Task 3 (вариант 2)
"""


# # ньютон  
# def newton(x0, eps):
#     step = 0
#     xk = x0
#     gk = gradient_function(xk)
#     hessen = hesse(xk)
#     sigma = np.linalg.norm(gk)
#     sk = -1 * np.dot(np.linalg.inv(hessen), gk)
#          w = np.zeros ((2, 10 ** 3)) # Сохраняем итерацию и устанавливаем переменную xk
#
#     while sigma > eps and step < 100:
#                  # метод Ньютона в альфа = 1
#         w[:, step] = np.transpose(xk)
#
#         step += 1
#         xk = xk + sk
#         gk = gradient_function(xk)
#         hessen = hesse(xk)
#         sigma = np.linalg.norm(gk)
#         sk = -1 * np.dot(np.linalg.inv(hessen), gk)
#         print('--The {}-th iter, the result is {},object value is {:.4f}'.format(step, np.array(xk), object_function(xk)))
#     return w
#
#
#
#
#  # Метод сопряженного градиента
# def conjugate_gradient(x0, eps):
#     xk = x0
#     gk = gradient_function(xk)
#     sigma = np.linalg.norm(gk)
#     sk = -gk
#     step = 0
#          w = np.zeros ((2, 10 ** 3)) # Сохраняем итерацию и устанавливаем переменную xk
#  
#     while sigma > eps and step < 1000:
#         w[:, step] = np.transpose(xk)
#  
#         step += 1
#         alpha = wolfe_powell(xk, sk)
#         xk = xk + alpha * sk
#         g0 = gk
#         gk = gradient_function(xk)
#         miu = (np.linalg.norm(gk) / np.linalg.norm(g0))**2
#         sk = -1 * gk + miu * sk
#         sigma = np.linalg.norm(gk)
#         print('--The {}-th iter, the result is {},object value is {:.4f}'.format(step, np.array(xk),object_function(xk)))
#     return w
#
#
# def hill_climb(domain, costf):
#
#     # Выбрать случаиное решение
#     sol = [random.randint(0, domain[i]) for i in xrange(len(domain))]
#     best = costf(sol)
#
#     # Главныи цикл
#     is_stop = False
#     while not is_stop:
#         # Создать список соседних решении
#         neighbors = []
#         for j in xrange(len(domain)):
#
#         # Отходим на один шаг в каждом направлении
#         if 0 < sol[j] < 9:
#             neighbors.append(sol[0:j] + [sol[j]+1] + sol[j+1:])
#             neighbors.append(sol[0:j] + [sol[j]-1] + sol[j+1:])
#
#         if 0 == sol[j]:
#             neighbors.append(sol[0:j] + [sol[j]+1] + sol[j+1:])
#
#         if sol[j] == domain[j]:
#             neighbors.append(sol[0:j] + [sol[j]-1] + sol[j+1:])
#
#         # Ищем наилучшее из соседних решении
#
#         is_stop = True
#         for j in xrange(len(neighbors)):
#             cost = costf(neighbors[j])
#         if cost < best:
#             is_stop = False
#             best = cost
#             sol = neighbors[j]
#
#     return sol, best
