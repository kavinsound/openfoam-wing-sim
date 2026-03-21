import numpy as np
from scipy.spatial.transform import Rotation as R
import math

start_time = 0.0
end_time = 0.2
n = 100
delta_t = 0.2/n



freq = 20
pi = np.pi

max_r = 60 * pi / 180
max_f = 20 * pi / 180

fn_r = lambda x: (-1 * np.cos(freq * 2 * pi * x) + 0.6) * 1/2
fn_f = lambda x: np.sign(np.sin(freq * 2 * pi * x)) * (np.abs(np.sin(freq * 2 * pi * x))**(0.8))

# print(fn_f(0))

def getNextOrientation(t):
    euler_theta = [fn_f(t), 0, fn_r(t)]
    # print(f"t: {t}: {euler_theta}")
    rot = R.from_euler('zx', [euler_theta[2], euler_theta[0]], degrees=False)

    eulers = rot.as_euler('xyz', degrees=False)
    return eulers

with open("meshMotion.dat", "w") as f:
    f.write(f"{n+1}\n(\n")

    for i in range(n+1):
        current_t = start_time + delta_t * i
        current_t = round(current_t, 3)
        # print(current_t)
        q = getNextOrientation(current_t)
        f.write(f"({current_t} ((0 0 0) ({q[0]} {q[1]} {q[2]})))\n")
    f.write(")")


    
