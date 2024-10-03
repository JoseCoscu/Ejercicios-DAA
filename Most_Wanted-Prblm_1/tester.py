pol = [0, 2, 4, 6, 9]
c = 5
m = 10


def simulation(pol, c, m):
    pol = sorted(pol)
    limit_right = 0
    limit_left = m - 1
    criminal = True
    pol_left = [x for x in pol if x < c]
    pol_right = [x for x in pol if x > c]
    while True:
        # print(pol_left)
        # print(pol_right)

        if not criminal or len(pol_left) + len(pol_right) == 0:
            break
        while len(pol_right) + len(pol_left) > 0:
            print(pol_left + pol_right, '------', c)
            if not (c - 1 in pol_left):
                for i in range(0, len(pol_left)):
                    pol_left[i] += 1

            elif c - 1 in pol_left:
                dist = False
                pos_1 = 0
                pos_2 = 0
                for i in range(0, len(pol_left) - 1):
                    if pol_left[i + 1] - pol_left[i] >= 3:
                        pos_2 = i + 1
                        dist = True
                        break
                if dist:
                    for i in range(0, pos_2):
                        pol_left[i] += 1
                    for i in range(pos_2, len(pol_left)):
                        pol_left[i] -= 1
                elif not (0 in pol_left):
                    for i in range(0, len(pol_left)):
                        pol_left[i] -= 1
                else:
                    pol_left.remove(c - 1)
                    for i in range(0, len(pol_left)):
                        pol_left[i] += 1
            # caso de right

            if not (c + 1 in pol_right):
                for i in range(0, len(pol_right)):
                    pol_right[i] -= 1

            elif c + 1 in pol_right:
                dist = False
                # pos_1=0
                pos_2 = 0
                for i in range(0, len(pol_right) - 1):
                    if pol_right[i + 1] - pol_right[i] >= 3:
                        #pos_1=i
                        pos_2 = i + 1
                        dist = True
                        break
                if dist:
                    for i in range(0, pos_2):
                        pol_right[i] += 1
                    for i in range(pos_2, len(pol_right)):
                        pol_right[i] -= 1
                elif not (m - 1 in pol_right):
                    for i in range(0, len(pol_right)):
                        pol_right[i] += 1
                else:
                    pol_right.remove(c + 1)
                    for i in range(0, len(pol_right)):
                        pol_right[i] -= 1

            if len(pol_left) >= 0 and len(pol_right) > 0:
                if c - pol_left[-1] >= pol_right[0] - c:
                    if c - pol_left[-1] == 1:
                        criminal = False
                        break
                    if not (c + 1 in pol_right):
                        c += 1
                    else:
                        c -= 1
                else:
                    if not (c - 1 in pol_left):
                        c -= 1
                    elif not (c + 1 in pol_right):
                        c += 1
                    else:
                        criminal = False
                        break
            elif len(pol_left) == 0:
                if not (c + 1 in pol_right):
                    c += 1
                elif c - 1 >= 0:
                    c -= 1
                else:
                    criminal = False
                    break
            else:
                if not (c - 1 in pol_left):
                    c -= 1
                elif c + 1 <= m - 1:
                    c += 1
                else:
                    criminal = False
                    break
    print('final', pol_left + pol_right , '---------', criminal)
    return (len(pol_left) + len(pol_right)),criminal



def solution(pol, c, m):
    pol = sorted(pol)
    antecesor=-1
    sucesor=len(pol)

    for i in range(0, len(pol)):
        if(c-pol[i]>0 and (c-pol[i])%2==0):
            antecesor=i
    for i in range(0, len(pol)):
        if(pol[i]-c>0 and (pol[i]-c)%2==0):
            sucesor=i
            break
    print('antecesor', antecesor, 'sucesor', sucesor)
    if(antecesor==-1 and sucesor==len(pol)):
        return (len(pol)),True
    elif(antecesor!=-1 and sucesor==len(pol)):
        return len(pol)-antecesor-1,False
    elif(antecesor==-1 and sucesor!=len(pol)):
        return len(pol)-sucesor-1,False
    else:
        return sucesor-antecesor-2



print(solution(pol, c, m))








# simulation(pol, c, m)
