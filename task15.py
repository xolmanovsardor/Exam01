text = "{n1} soni {n2} ga bulinadi."
n = int(input("son kiriting ->>"))
if n % 2 == 0:
    print(text.format(n1 = n, n2 = 2))
if n % 3 ==0:
    print(text.format(n1 = n,n2 = 3 ))
if n % 5 ==0:
    print(text.format(n1 = n,n2 = 5 ))   