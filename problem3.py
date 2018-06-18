# 素因数分解します

# inputした数の素因数を配列で返す関数
def calc_prime(num):
    num_prime_list=[num]
    limit=(num//2)+1
    while num%2==0:
        num/=2
        num_prime_list.append(2)

    for i in range(3,limit,2):
        while num%i==0:
            num/=i
            num_prime_list.append(i)

    if len(num_prime_list)!=1:
        del num_prime_list[0]

    return sorted(num_prime_list)


# 素因数っぽいのを求める関数(素数ではない可能性がある)
def calc_divisor(num):
    div_list=[]
    num1=num

    for i in [2,3]:
        if num%i==0:
            while num%i==0:
                num/=i
                div_list.append(i)
                div_list.append(num//i)
    
    i=1
    while True:
        div=6*i-1
        if div*div>num1:
            break
        if num%div==0:
            num/=div
            div_list.append(div)
        div+=2
        if num%div==0:
            num/=div
            div_list.append(div)
        i+=1
    div_list.append(int(num))

    return sorted(div_list)



# 素因数分解する
# とりあえず素因数候補を出す
div_list=calc_divisor(600851475143)
prime_list=[]

# それらが素数か確かめる
for key in div_list:
    for prime in calc_prime(key):
        prime_list.append(prime)      
print(prime_list)
print(max(prime_list))
# 6857   