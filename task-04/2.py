def is_stable(n, forces):
    total_force = [0, 0, 0]
    for force in forces:
        total_force[0] += force[0]
        total_force[1] += force[1]
        total_force[2] += force[2]
    return "YES" if all(coord == 0 for coord in total_force) else "NO"

def main():
    n = int(input())
    forces = [list(map(int, input().split())) for _ in range(n)]
    result = is_stable(n, forces)
    print(result)

if __name__ == "__main__":
    main()