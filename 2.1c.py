route = [[0,1,1,1,0,1],
         [0,1,0,1,0,1],
         [0,0,0,1,0,1],
         [0,1,0,0,0,1],
         [0,1,1,1,0,1],
         [0,1,1,1,0,1]]
cs = [0,0]
ce = [4,5]
openlist = []
closedlist = []
    
def openList(lab = route, coord = cs):
    global openlist, closedlist, cs
    c = coord[::-1]
    openlistdraft = []
    if coord == cs:
        start = {'pp':coord, 'cp':coord, 'F':0, 'G':0, 'H':0}
    else:
        start = openlist[0]
    openlistdraft.append(start)
    for x in (-1,0,1):
        for y in (-1,0,1):
            if x == y: continue
            if c[0]+x == c[0] and c[1]+y == c[1] or c[0]+x < 0 or c[1]+y < 0:
                continue
            if c[0] >= len(lab) or c[1] >= len(lab[0]):
                raise IndexError
            try:
                if lab[c[0]+x][c[1]+y] == 1: continue
                point = {'pp':coord, 'cp':[c[0]+x,c[1]+y][::-1], 'F':0, 'G':0, 'H':0}
                if point['cp'] in [item['pp'] for item in closedlist]: continue    
                openlistdraft.append(point)
            except IndexError:
                continue
    for item in openlistdraft:
        openlist.append(item)
    computeG()
    computeH()
    computeF()
    return openlist

def computeG():
    global openlist
    for item in openlist[1:]:
        if item['H'] != 0: continue
        if abs(item['cp'][1] - item['pp'][1]) == 1 and abs(item['cp'][0] - item['pp'][0]) == 1:
            item['G'] = openlist[0]['G'] + 14
        else:
            item['G'] = openlist[0]['G'] + 10
    return openlist

def computeH():
    global ce, openlist
    for item in openlist:
        dX = ce[1] - item['cp'][1]
        dY = ce[0] - item['cp'][0]
        item['H'] = (dX + dY) * 10
    return openlist

def computeF():
    global openlist
    for item in openlist:
        item['F'] = item['G'] + item['H']
    return openlist

def closedList(): #add one item with min(F) from items in openlist
    global closedlist, openlist
    closedlist.append(openlist.pop(0))
    return closedlist, openlist

def cycle():
    global closedlist, openlist
    while openlist:
        
    return closedlist

def wayBack():
    way = []
    global closedlist,cs
    for item in closedlist[::-1]:
        way.append(item['cp'])
    way = way[::-1]
    if cs in way: return way
    else: return "You've an error"

if __name__ == '__main__':
    openList()
    openList(route, [0,1])
    openList(route, [0,2])
    
    for item in openlist:
        print("I'm in openlist:   ", item)
    
    for item in closedlist:
        print("I'm in closedlist: ", item)
      
