def count_differences(s):
    reference = "amfoss"
    return sum(1 for a, b in zip(s, reference) if a != b)

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        result = count_differences(s)
        print(result)

    main()
