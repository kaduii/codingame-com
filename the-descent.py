while True:
    
    mountainAll = []
    
    for i in range(8):
        mountainHeight = int(input())
        mountainAll.append(mountainHeight)

    print(mountainAll.index(max(mountainAll)))
