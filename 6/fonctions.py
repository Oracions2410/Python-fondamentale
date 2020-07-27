# Les fonctions

def addition(n):
    return 5 + n

# Fonction récursive
def add(a):
    a += 1
    print(a)
    if (a < 10):
        add(a)


if __name__ == '__main__':
    print(addition(4))
    print(addition(6))
    print(addition(7))
    add(2)