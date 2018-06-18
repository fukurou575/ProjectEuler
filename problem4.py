import time

#inputした数の3桁の約数を求める関数
def divisor(num):
    div_list=[]
    for i in range(100,1000):
        if num%i==0:
            div_list.append([i,(num//i)])
    return div_list


t1=time.time()
# 6桁を仮定
flag=False
for i in range(10):
    for j in range(10):
        for k in range(10):
            # 回文数の候補を上から潰す
            N=999999-100001*k-10010*j-1100*i
            print(N)
            N_divisors=divisor(N)
            for h in N_divisors:
                if h[1]<1000:
                    flag=True
                    print(h)
                    break
            break
        if flag:
            break
    if flag:
        break
t2=time.time()
print(t2-t1)
# 906609
# [913, 993]
# 0.008929967880249023