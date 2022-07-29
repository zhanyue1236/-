from gmssl import sm3,func
import random
import time
def Rho_attack(num,length):
    lst=[]
    i=0
    #ran_str=str(random.randint(0,pow(2,length)))
    ran_str=hex(random.randint(0,pow(2,length*4)))[2:].zfill(length)
    raw=ran_str
    for j in range(num):
        ran=bytes(ran_str,encoding='utf-8')
        RES=sm3.sm3_hash(func.bytes_to_list(ran))[:length]
        if RES in lst:
            if ran!=raw:
                print('success!')
                i=1
                return True
            else:
                print('fail!')
                return False
        else:
            lst.append(RES)
        ran_str=RES
    print('fail!')
    return False
t1=time.time()
Rho_attack(pow(2,64),7)
t2=time.time()
print('THE TOTAL TIME IS :',t2-t1,'s')