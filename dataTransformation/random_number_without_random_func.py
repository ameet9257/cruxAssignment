#lst_100 = [i for i in range(1,101)]


from time import time

def time_random():
 return time() - float(str(time()).split('.')[0])

def gen_random_range(min, max):
 return int(time_random() * (max - min) + min)

if __name__ == '__main__':
 for i in range(1):
     print(gen_random_range(1,100))