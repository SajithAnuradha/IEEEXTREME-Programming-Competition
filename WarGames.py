n = int(input())
order = {'2':0 ,'3':1 ,'4':2 ,'5':3 ,'6':4 , '7' :5 , '8' :6 , '9':7 , 'T':8 , 'J' :9 , 'Q' :10 , 'K' :11 , 'A' :12}

for _ in range(n):
    playerCards1 = input().split(" ")
    playerCards2 = input().split(" ")
    len1 = len(playerCards1)
    len2 = len(playerCards2)

    while len(playerCards1) > 0 and len (playerCards2) > 0:
        if playerCards1 == playerCards2:
            print("draw")
            break
        if order[playerCards1[0]] > order[playerCards2[0]]:
            playerCards1.pop(0)
            playerCards1.append(playerCards2.pop(0))
        elif order[playerCards1[0]] < order[playerCards2[0]]:
            playerCards2.pop(0)
            playerCards2.append(playerCards1.pop(0))
        else:
            playerCards1.append(playerCards1.pop(0))
            playerCards2.append(playerCards2.pop(0))
    if len(playerCards1) == 0:
        print("player 2")
    elif len(playerCards2) == 0:
        print("player 1")






