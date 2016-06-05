class Astar:
    openlist = []
    closedlist = []
    way = []
    def __init__(self, array=[], start=[0,0], finish=[]):
        self.lab = array
        self.start = start
        self.finish = finish

    def openList(self, lab = self.lab, coordinates = self.start):
        c = coordinates[::-1]
        openlistdraft = []
        for x in (-1,0,1):
            for y in (-1,0,1):
                if c[0]+x == c[0] and c[1]+y == c[1] or c[0]+x < 0 or c[1]+y <0:
                    continue
                if c[0] >= len(lab) or c[1] >= len(lab[0]):
                    raise IndexError
                try:
                    if lab[c[0]+x][c[1]+y] == 1: continue
                    openlistdraft.append([c[0]+x,c[1]+y])
                except IndexError:
                    continue
        
        for i in openlistdraft:
            Astar.openlist.append(i[::-1])
        return Astar.openlist
        
    def closedList(self):
        Astar.closedlist = Asatar.closedlist + Astar.openlist[0:2]
        return Astar.closedlist

    def computeH(self, A =[]):
        dX = int(self.finish[1]) - int(A[1])
        dY = int(self.finish[0]) - int(A[0])
        H = (dX + dY)*10
        return H

    def computeG(self, prev_G = 0, prev = [0,0], cur = []):
        if abs(cur[1] - prev[1]) == 1 and abs(cur[0] - prev[0]) == 1:
            G = prev_G + 14
        else:
            G = prev_G + 10
        return G

    def computeF(self, G, H):
        F = G + H
        return F

    def way(self):
        return Astar.way

if __name__=='__main__':
    route = [[0,1,1,1,0,1],
             [0,1,0,1,0,1],
             [0,0,0,1,0,1],
             [0,1,0,0,0,1],
             [0,1,1,1,0,1],
             [0,1,1,1,0,1]]
    cs = [0,0]
    ce = [4,5]
    way = Astar(route, cs, ce)
    
    cl = []
    ol = way.openList(route, cs)
    cl = cl + way.closedList(ol)
    print(ol)
    print(cl)
    for i in ol[2:]:
        print(way.computeG(cs,i))
        print(way.computeF(way.computeG(cs,i),way.computeH(i)))
