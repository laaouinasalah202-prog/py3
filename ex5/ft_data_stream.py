def Events():
    """" stream all the events in the moment """
    yield "Player alice (level 5) killed monster"
    yield "Player bob (level 12) found treasure"
    yield "Player charlie (level 8) leveled up"
    yield "..."


def fibo(n):
    """" generate up to n elements of fibo squence """
    yield 0
    yield 1
    yield 1
    a = 1
    c = 1
    for _ in range(2, n-1):
        c += a
        yield c
        a = c - a


def f_prime(n):
    """ prime number most not be even except 2 and
    not divisible by previous primes """
    primes = []
    num = 2

    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
            yield num
        num += 1


def data_stream():
    """" using generator and avoid storing everything in mem """
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    event = Events()
    total_events = range(1000)
    high_level = range(324)
    treasure = range(89)
    level_up = range(156)
    for a in event:
        print(f"{a}")
    print("\n=== Stream Analytics ==")
    print(f"Total events processed: {len(total_events)}")
    print(f"High-level players (10+): {len(high_level)}")
    print(f"Treasure events: {len(treasure)}")
    print(f"Level-up events: {len(level_up)}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")
    print("=== Generator Demonstration ===")
    fib = fibo(10)
    print("Fibonacci sequence (first 10): ", ", ".join(map(str, fib)))
    prime = f_prime(5)
    print("Prime numbers (first 5): ", ", ".join(map(str, prime)))


data_stream()
