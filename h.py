def read_coords():
    coords = input().split(' ')
    x = int(coords[0])
    y = int(coords[1])
    return (x, y)


n_tests = int(input())

for n_test in range(n_tests):
    n_iters = int(input()) + 1

    home = read_coords()
    coords = [read_coords() for n_iter in range(n_iters)]
    berg = read_coords()

    # prev_coords = home

    # status = "happy"
    # for iter in range(n_iters):
    #     coords = read_coords()
    #     if abs(coords[0] - prev_coords[0]) + abs(coords[1] - prev_coords[1]) > 1000:
    #         status = "sad"
    #         break
    #     prev_coords = coords

    # print(status)
