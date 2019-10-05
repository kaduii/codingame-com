while True:
    
    mountainAll = []
    
    for i in range(8):
        mountainHeight = int(input())  # represents the height of one mountain.
        mountainAll.append(mountainHeight)

    print(mountainAll.index(max(mountainAll)))