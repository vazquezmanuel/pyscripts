def exp(num,pot=2):
    ans = 1
    for i in range(pot):
        ans *= num 
    return ans

def more_args(iterable, *args):
    if args:
        s = [len(iterable)]
        for a in args:
            s.append(len(a))
        return s
    return len(iterable)

def main():
    print(exp(4))
    print(exp(4,3))
    print(more_args("hello"))
    print(more_args("hello", "world"))

if __name__ == "__main__":
    main()    
