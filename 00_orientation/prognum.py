
def fibo(n):
    if n < 3:
        return 1 # 最初の2つの数は1
    
    return fibo(n-1) +fibo(n-2)# 再帰的に呼び出す
