import turtle as t

def generate_fibonacci():
    n = input("n = "); n = int(n)
    fib = [0, 1]

    for i in range(n+1):
        sum = fib[i+1] + fib[i]
        fib.append(sum)
    return fib

def plot_fibonacci(fib):
    for num in fib:
        t.circle(num, 90)

def main():
    fib0 = generate_fibonacci()
    plot_fibonacci(fib0)

main()
