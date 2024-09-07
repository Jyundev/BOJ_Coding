import sys
cnt = int(input())

for _ in range(cnt):
    n = int(sys.stdin.readline().strip())

    def rec(num):
        if num < 2 :
            if num == 0 :
                return [1,0]
            elif num == 1:
                return [0,1]
        else:
            var_dict = {i:[0,0] for i in range(num+1)}
            var_dict[0] = [1,0]
            var_dict[1] = [0,1]

            for i in range(2,num+1):
                var_dict[i] = [var_dict[i-1][0] + var_dict[i-2][0], var_dict[i-1][1] + var_dict[i-2][1]]
            return var_dict[num]    
    a,b = rec(n)
    sys.stdout.write(f'{a} {b}\n')


