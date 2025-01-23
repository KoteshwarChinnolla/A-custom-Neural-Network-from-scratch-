import numpy as np
class ANNmodel: 
    def __init__(self):
        self.w=[]
        self.b=[]
    def add(self,l1,l2):
        self.w.append(np.random.randn(l1,l2))
        self.b.append(np.random.randn(l2))
        return self.w,self.b
    def far_test(self,X,w,b):
        h=[]
        z=[]
        h.append(X)
        for i in range(len(w)):
            z.append(np.dot(h[i],w[i])+b[i])
            h.append(self.activation(z[i]))
            # print(w[i].shape)
        Y=h[-1]
        return Y,h[:-1],z
    def back_test(self,X,Y,y_train,w,b,z,h,N):
        n=len(w)
        dl_w=[]
        dl_h=[]
        dl_z=[]
        dl_b=[]
        dl_h.append(-(2/n)*(y_train-Y))
        dl_z.append(dl_h[0]*1)
        dl_w.append(np.dot(h[n-1].T,dl_z[0]))
        dl_b.append(np.sum(dl_z[0],axis=0))
        for i in range(1,len(w)):
            dl_h.append(np.dot(dl_z[i-1],w[n-i].T))
            dl_z.append(dl_h[i]*self.deactivate(z[n-i-1]))
            dl_w.append(np.dot(h[n-i-1].T,dl_z[i]))
            dl_b.append(np.sum(dl_z[i],axis=0))
        lr=0.01
        for i in range(len(w)):
            w[i]=w[i]-lr*dl_w[n-i-1]
            b[i]=b[i]-lr*dl_b[n-i-1]
        return w,b
    def activation(self,x):
        return np.maximum(0, x)

    def Loss(self,Y,y_train,N):
        return np.sum((y_train-Y)**2)/N

    def deactivate(self,x):
        return np.where(x > 0, 1, 0)
        
    def train(self,e,X_train,y_train):
        l=[]
        N=len(y_train)
        Loss = lambda Y, y, N: np.sum((y - Y) ** 2) / N
        w,b=self.w,self.b
        Y,h,z=self.far_test(X_train,w,b)
        loss_old=self.Loss(Y,y_train,N)
        for i in range(e):
            # print(Y)
            print(loss_old)
            l.append(loss_old)
            w,b=self.back_test(X_train,Y,y_train,w,b,z,h,N)
            Y,h,z=self.far_test(X_train,w,b)
            loss_new=self.Loss(Y,y_train,N)
            
            # if(abs(loss_old-loss_new)<0.001):
            #     break
            loss_old=loss_new
        return w,b,l
    