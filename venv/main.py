import time

def writer():
    #stupid method, i'm sorry((
    f = open("code.py", 'w')
    f.write("n = 999999\n")
    for i in range(0, 100000):
        f.write(f"if n == {i}:\n")
        f.write(f"\tprint({i})\n")
    f.close()

def check_my_theory():
    n = 999999
    for i in range(0, 1000000):
        #print(f"hello!{i} hello\n hello")
        if n == i:
            print(i)
            print("Ura!!")
            break

if __name__ == "__main__":
    time_start = time.time()
    #
    #writer()
    check_my_theory()
    #
    time_end = time.time()
    print("It took: " + str(time_end - time_start) + "  sec")

# What I understtod:
# If we used one million iterations of "IF N = *I*" in python, it took less one sec time
# But if at every iteration we will call print(""), this task took 4-8 sec
# If we change just print("") on print("hello"), this task can took 10-16 sec
# Bot bad, but not high-performance
