import cvxpy as cp
import numpy as np






class ADMM():
    def __init__(self, BS_number=4, User_number = 10, bandwidth_total = 10e6, mu_1 = 0.5, mu_2 = 0.5,s=0.2,SNR,association_UE,video_bitrate_frame):
        self.BS_number=BS_number
        self.User_number=User_number
        self.bandwidth_total=bandwidth_total
        self.mu_1=mu_1
        self.mu_2=mu_2
        self.s=s
        self.SNR=np.onse((BS_number,User_number))*1e3 #modefy
        self.video_bitrate_frame=np.ones((1,User_number))*1e6 #modefy
        self.association_UE=np.onse((BS_number,User_number)) #modefy
        self.rate_perHz=np.log2(1+SNR)
        self.rate_perHz=np.sum(association_UE*rate,0).reshape((1,self.User_number)) 
        self.position_error_requirment=np.onse((1,User_number))
        
        self.theta_v=np.zeros((1,User_number))
        self.theta_p=np.zeros((BS_number,1))
        self.w_c=np.zeros((1,User_number))
        self.w_p=np.zeros((BS_number,1))
        self.z_c=np.zeros((1,User_number))   
        self.z_p=np.zeros((BS_number,1))
        
        
          
        

    def cal_Pvideo(z_c,w_c,w_gate,u,theta_v):
        
        if (z_c>=w_gate):
            c = - self.mu_1*u
        else:
            c = 0
            
        return c+(theta_v)*(z_c-w_c)+s/2*((z_c-w_c)^2)
            

    def cal_video_qoe():
        
        w_gate=self.video_bitrate_frame/self.rate_perHz

        for i in range(User_number):
            P1=cal_Pvideo(self.w_c[0,i]-self.theta_v[0,i]/self.s,self.w_c[0,i],self.w_gate[0,i],self.biterate_utility[0,i],self.mu_1,self.theta_v[0,i])
            P2=cal_Pvideo(self.w_gate[0,i],self.w_c[0,i],self.w_gate[0,i],self.biterate_utility[0,i],self.mu_1,self.theta_v[0,i])
            if (w_gate[0,i]>=self.w_c[0,i]-self.theta_v[0.i]/s) && (P1>=P2):
                self.z_c[0,i]=self.w_gate[0,i]
            else:
                self.z_c[0,i]=self.w_c[0,i]-self.theta_v[0,i]/self.s
                
        


    def cal_pos_qoe():
        
        w = cp.Variable(M)
        Y = [cp.Variable((2, 2), symmetric=True) for _ in range(N)]
        Y1 = cp.Variable(N)
        J = [cp.Variable((2, 2), symmetric=True) for _ in range(N)]
        
        P1 = cp.Variable(N)
        P2 = cp.Variable(M)
        P2 = cp.Variable(M)
        
        objective = cp.Minimize(sum(P1)+sum(P2)+sum(P3))


        for m in range(M):
            constraints += [w[m] >= 0]
            constraints += [P2[n]>=self.theta_p[n,0]*(w[m]-self.w_p[m,0]*self.w_p[m,0])]
            constraints += [P2[n]>=self.theta_p[n,0]*(w[m]-self.w_p[m,0]*self.w_p[m,0])]

        for n in range(N):  
            constraints += [P1[n]>=cp.exp(Y1[n]/self.position_error_requirment[0,n])]
            constraints += [(Y1[n]) == cp.trace(Y[n])]
            constraints += [
                cp.bmat([[Y[n], np.eye(2)], [np.eye(2), 8*np.pi*np.pi/30/30 * sum((w[m]) * G[m, n] for m in range(M))]]) >> 0,
                J[n] == 8*np.pi*np.pi/30/30 * sum((w[m]) * G[m, n] for m in range(M))
            ]
    
        prob = cp.Problem(objective, constraints)
    
        prob.solve(solver=cp.SCS, verbose = True,max_iters=2000000,eps=1e-2)        


    def cal_admm():
        
        s=0.1
        
        cnt=0
        while (cnt<10){
            cnt=cnt+1
            cal_video_qoe()
            cal_pos_qoe()
            
        } 
        
    
