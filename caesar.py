def caesar(message, key):
    abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    key=int(key)
    size=len(message)
    bool = False
    n=0
    for i in range(size):
        bool = False
        n = 0
        while n < 26 and not bool:
            if message[i] == abc[n]:
                if (n+key) >= 26:
                    r = (n+key) - 26
                    message[i] = abc[r]
                else:
                    message[i] = abc[n+key]
                bool = True
            n = n + 1
