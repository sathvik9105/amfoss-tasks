def check_hello(s):
    reference = "hello"
    idx = 0
    for char in s:
        if char == reference[idx]:
            idx += 1
            if idx == 5:
                return "YES"
    return "NO"

def main():
    s = input()
    result = check_hello(s)
    print(result)
    
if __name__ == "__main__":
    main()