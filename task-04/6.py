def find_clems_town(n, travel_times):
    min_time = min(travel_times)
    if travel_times.count(min_time) == 1:
        return travel_times.index(min_time) + 1
    else:
        return "Still Aetheria"

def main():
    n = int(input())
    travel_times = list(map(int, input().split()))
    result = find_clems_town(n, travel_times)
    print(result)

if __name__ == "__main__":
    main()
