import cvxpy as cp
import numpy as np
# Create two scalar optimization variables.
# 在CVXPY中变量有标量(只有数值大小)，向量，矩阵。
# 在CVXPY中有常量(见下文的Parameter)
def conv_func():
    x = Variable() # 定义变量x,定义变量y。两个都是标量
    y = Variable()
    # Create two constraints.
    # 定义两个约束式
    constraints = [x + y == 1,
                x - y >= 1]
    # 优化的目标函数
    obj = Minimize(square(x - y))
    # 把目标函数与约束传进Problem函数中
    prob = Problem(obj, constraints)
    prob.solve()  # Returns the optimal value.
    print("status:", prob.status)
    print("optimal value", prob.value) # 最优值
    print("optimal var", x.value, y.value) # x与y的解
    # 状态域被赋予'optimal'，说明这个问题被成功解决。
    # 最优值是针对所有满足约束条件的变量x,y中目标函数的最小值
    # prob.solve()返回最优值，同时更新prob.status,prob.value,和所有变量的值。



def conv_func1(User_number,BS_number,User_cos_theta,User_sin_theta,G):

    M=BS_number
    N=User_number
    W=100
 
    w = cp.Variable(M)
    z = [cp.Variable((2, 2), symmetric=True) for _ in range(N)]
    z1 = cp.Variable(N)
    J = [cp.Variable((2, 2), symmetric=True) for _ in range(N)]

    # Objective
    objective = cp.Minimize(sum(cp.exp(cp.inv_pos(-z1))))

    # Constraints
    constraints = [cp.sum(w) <= W]
    for m in range(M):
        constraints += [w[m] >= 0]
    for n in range(N):
        constraints += [cp.trace(z[n])>=0]
        constraints += [(z1[n]) == cp.trace(z[n])]
        constraints += [
            cp.bmat([[z[n], np.eye(2)], [np.eye(2), J[n]]]) >> 0,
            J[n] >= 8*np.pi*np.pi/30/30 * sum((w[m]) * G[m, n] for m in range(M))
        ]
 
    prob = cp.Problem(objective, constraints)
 
    prob.solve(solver=cp.SCS, verbose = True,max_iters=2000000,eps=1e-2) # Returns the optimal value.
    print("status:", prob.status)
    print("optimal value", prob.value) # 最优值
    print("optimal var",  w.value) # x与y的解
    # print(np.trace( np.linalg.inv(JN.value)))
    print(G[0,0,0])
def np_random(seed=42):
    if not (isinstance(seed, int) and seed >= 0):
        raise ValueError('Seed must be a non-negative integer.')
    rng = np.random.RandomState()
    rng.seed(seed)
    return rng

np_random = np_random(1)
User_number=10
BS_number=4
np.random.seed(0)
theta=np.random.rand(BS_number,User_number)*np.pi*2
selfSNR=np.random.rand(BS_number,User_number)*30
action_BW_positioning=np.ones((BS_number,1))*1e8
User_cos_theta=np.cos(theta)
User_sin_theta=np.sin(theta)
G=np.zeros((BS_number,User_number,2,2))
for i in range(User_number):
    for j in range(BS_number):
        ctheta=User_cos_theta[j,i]
        stheta=User_sin_theta[j,i]
        G[j,i,:,:]=np.array([[ctheta*ctheta, ctheta*stheta], [ctheta*stheta, stheta*stheta]])*selfSNR[j,i]       
conv_func1(User_number,BS_number,User_cos_theta,User_sin_theta,G)

# for i in range(User_number):
#     position_Jn=np.zeros((2,2))
#     for j in range(BS_number):
#         ctheta=User_cos_theta[j,i]
#         stheta=User_sin_theta[j,i]
#         G=np.array([[ctheta*ctheta, ctheta*stheta], [ctheta*stheta, stheta*stheta]])
#         position_Jn += 8*np.pi*np.pi/3e8/3e8*(action_BW_positioning[j,0]*action_BW_positioning[j,0]*selfSNR[j,i]*G)











# z1 = cp.Variable(5)
# z2 = cp.Variable(5)


# # Objective
# objective = cp.Minimize(sum(cp.exp(-cp.inv_pos(z1))))

# # Constraints
# constraints=[]
# for i in range(5):
#     constraints += [z1[i] <= 1]

# prob = cp.Problem(objective, constraints)

# prob.solve(solver=cp.SCS, verbose = True,max_iters=2000000,eps=1e-4) # Returns the optimal value.
# print("status:", prob.status)
# print("optimal value", prob.value) # 最优值
# print("optimal var",  z1.value,cp.exp(cp.inv_pos(-z1.value)),np.exp(1/(-z1.value))) # x与y的解