# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for line in range(0, t):
    S = input()
    size_of_S = len(S)
    even = odd = ''
    for i in range(0, size_of_S):
        if i % 2 == 0:
            even += S[i]
        else:
            odd += S[i]

    print(even, odd)

