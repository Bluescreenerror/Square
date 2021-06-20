import pyautogui as p
import random as r
import time as t
t.sleep(2)
x = 1920 / 2
y = 1080 / 2
a = 500
# diagonal is 426.26
initial_a = (x - a/2, y - a/2)
p.moveTo(initial_a)
t.sleep(0.2)
p.drag(a, 0)
t.sleep(0.2)
p.drag(0, a)
t.sleep(0.2)
p.drag(-a, 0)
t.sleep(0.2)
p.drag(0, -a)

M = initial_a
N = (x + a/2, y - a/2)
O = (x + a/2, y + a/2)
P = (x - a/2, y + a/2)
A = (x - a/2, y)
G = (x - a/2, y - a/4)
H = (x - a/2, y + a/4)
B = (x, y + a/2)
I = (x - a/4, y + a/2)
J = (x + a/4, y + a/2)
C = (x + a/2, y)
K = (x + a/2, y + a/4)
L = (x + a/2, y - a/4)
D = (x, y - a/2)
F = (x - a/4, y - a/2)
E = (x + a/4, y - a/2)
point_list = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P]
while True:
    point_index = r.randint(0, 15)
    point = point_list[point_index]
    p.dragTo(point)
