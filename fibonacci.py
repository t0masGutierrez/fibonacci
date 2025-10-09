import turtle as t

def generate_fibonacci(n):
    x = [0, 1]
    for i in range(n+1):
        sum = x[i+1] + x[i]
        x.append(sum)
    return x

def plot_fibonacci(fib):
    for num in fib:
        t.circle(num, 90)

def main():
    n0 = input("n = "); n0 = int(n0)
    fib0 = generate_fibonacci(n0)
    plot_fibonacci(fib0)

main()
    