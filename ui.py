from service import Service


class UI(object):

    def run(self):
        # print("Introduceti nodul de pornire:")
        # start = int(input())-1
        # print("Introduceti nodul de final:")
        # finish = int(input())-1

        populationSize = 500
        nrGeneration = 3000

        service = Service()

        matrix = service.readFromFile()
        nrNodes = int(matrix[0][0])
        matrix= matrix[1:]
        start = int(matrix[-2][0])-1
        finish = int(matrix[len(matrix)-1][0])-1
        matrix = matrix[:-2]

        # print(start, finish,matrix)

        problParam={}
        problParam["noNodes"] = nrNodes
        problParam["mat"] = matrix

        service.ga(populationSize, nrGeneration, problParam)



        # result = service.path(matrix, nrNodes, 0,0)
        # result2 = service.path(matrix, nrNodes, start,finish)


        #
        #
        # f = open("data.out", "w")
        # # f.write(len(matrix))
        #
        #
        # #First
        # print(len(matrix))
        # f.write(str(len(matrix)))
        # f.write("\n")
        #
        # result[1].pop()
        #
        # for elem in result[1]:
        #     print(elem+1, end =" ")
        #     f.write(str(elem+1))
        #     f.write(" ")
        #
        #
        # print()
        # f.write("\n")
        #
        # print(result[0])
        # f.write(str(result[0]))
        # f.write("\n")
        #
        #
        # #Second
        # print(len(result2[1]))
        # f.write(str(len(result2[1])))
        # f.write("\n")
        #
        #
        # for elem in result2[1]:
        #     print(elem+1, end =" ")
        #     f.write(str(elem+1))
        #     f.write(" ")
        #
        # print()
        # f.write("\n")
        #
        # print(result2[0])
        # f.write(str(result2[0]))
        #
        # f.close()
