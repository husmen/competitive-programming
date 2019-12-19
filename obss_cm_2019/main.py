# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(U, L, C):
    # write your code in Python 3.6
    sol_found = False
    u_row, l_row = None, None
    N, S = len(C), sum(C)

    possible = True if (S == U + L and 0 <= U <= N and 0 <= L <= N) else False
    if(possible):
        # get initial values shared between both rows
        tmp = [1 if x == 2 else (0 if x == 0 else None) for i, x in enumerate(C)]

        # get sum and diffs so far
        tmp_sum = sum([_ for _ in tmp if _ is not None])
        u_diff = U - tmp_sum
        l_diff = L - tmp_sum

        # get all values of first row
        if u_diff > 0:
            u_none = [(i, x) for i, x in enumerate(tmp) if x is None][:u_diff]
            u_limit = u_none[-1][0]
            u_row = [1 if x is None else x for x in tmp[:u_limit+1]] + [0 if x is None else x for x in tmp[u_limit+1:]]
            tmp = [0 if x is None else x for x in tmp[:u_limit+1]] + tmp[u_limit+1:]
        else:
            u_row = [0 if x is None else x for x in tmp] 

        # get all values of second row
        if l_diff > 0:
            l_none = [(i, x) for i, x in enumerate(tmp) if x is None][-l_diff:]
            l_limit = l_none[0][0]
            l_row = [0 if x is None else x for x in tmp[:l_limit]] + [1 if x is None else x for x in tmp[l_limit:]]
        else:
            l_row = [0 if x is None else x for x in tmp] 

        sol_found = True

    if sol_found:
        return "".join([str(_) for _ in u_row]) + "," + "".join([str(_) for _ in l_row])
    else:
        return "IMPOSSIBLE"

if __name__ == "__main__":
    tests = []
    tests.append(solution(1, 1, [2]))
    tests.append(solution(3, 2, [2, 1, 1, 0, 1]))
    tests.append(solution(5, 7, [2, 1, 0, 1, 0, 1, 2, 1, 0, 0, 2, 1, 1]))
    
    for _ in tests:
        print(_)
