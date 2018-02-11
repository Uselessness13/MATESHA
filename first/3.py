class Node:
    # def __init__(self, coord):
    #

    def __init__(self, father, coordFrom, coordWhere):
        if type(coordWhere) is int and type(coordFrom) is int and father is None:
            self.circuit = [[0 for i in range(8)] for j in range(8)]
            self.circuit[coordFrom][coordWhere] = 1
            self.figureCoord = [coordFrom, coordWhere]
            self.num = 0
            print("Node created")
        else:
            self.father = father
            self.coordFrom = coordFrom
            self.coordWhere = coordWhere
            father.children.append(self)
            self.num = father.num + 1

    def castleMove(self):
        tempX = self.figureCoord.x
        tempY = self.figureCoord.y
        while tempX < 8:
            a = Node(self, [tempX, self.figureCoord.y], [tempX + 1, self.figureCoord.y])
            a.castleMove()
            tempX += 1
        while tempY < 8:
            b = Node(self, [self.figureCoord.x, tempY], [self.figureCoord.x, tempY + 1])
            b.castleMove()
            tempY += 1

    def printer(self):
        for i in range(8):
            st = ""
            for j in range(8):
                st += (str(self.circuit[i][j]) + ' ')
            print(st)


node = Node(None, 7, 0)
node.printer()
