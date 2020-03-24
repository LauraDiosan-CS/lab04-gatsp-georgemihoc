# input:
#
# first line: number of cities (n)
# second line: distances between the first city and all the other cities (n real values)
# third line: distances between the second city and all the other cities (n real values)
# ...
# n + 1 line: distances between the n-th city and all the other cities (n real values)

# 4
# 0,1,2,4
# 1,0,3,15
# 2,3,0,6
# 4,15,6,0

#
#
# solution:
# first line: number of cities (n)
# second line: the optimal traversing path (indexes of cities, starting by 1)
# third line: the length of the optimal path (real value)
#
# 4
# 1,2,3,4
# 14

import heapq
from random import randint

from Cromozom import Chromosome


# 7542

class Service(object):
    '''
    Functie care citeste un fisier linie cu linie
    input -
    output - matricea formata din toate liniile fisierului
    '''
    def readFromFile(self):
        matrix = []
        f = open("data.in", "r")
        for line in f:
            array = []
            currentline = line.split(",")
            for elem in currentline:
                array.append(int(elem))
            matrix.append(array)
        return matrix


    def fitness(self, reprez,problParam):
        d = 0
        mat = problParam['mat']
        for i in range(len(reprez) - 1):
            d += mat[reprez[i]][reprez[i + 1]]

        d += mat[reprez[len(reprez) - 1]][reprez[0]]

        return d


    def ga(self, populationSize, nrGeneration, problParam):
        population = []
        weakestFitness = 0
        for i in range(populationSize):
            c= Chromosome(problParam)
            population.append(c)

            if self.fitness(c.repres, problParam) > weakestFitness:
                weakestFitness = self.fitness(c.repres, problParam)

        for i in range(0,nrGeneration):
            for j in range(populationSize):
                parent1 = randint(0,populationSize-1)
                parent2 = randint(0,populationSize-1)
                while parent1 == parent2:
                    parent2 = randint(0, populationSize - 1)
                child = population[parent1].crossover(population[parent2])
                child.mutation()

                if self.fitness(child.repres, problParam) < weakestFitness:
                    for i in range(len(population)):
                        if self.fitness(population[i].repres,problParam) == weakestFitness:
                            population.pop(i)
                            break
                    population.append(child)
                    weakestFitness = 99999
                    for i in range(len(population)):
                        if self.fitness(population[i].repres, problParam) < weakestFitness:
                            # weakest = population[i]
                            weakestFitness = self.fitness(population[i].repres, problParam)
            bestFitness = 9999
            best = []
            for i in population:
                scor = self.fitness(i.repres, problParam)
                if scor < bestFitness:
                    bestFitness = scor
                    best = i
            print(best.repres)
            print(bestFitness)


    # '''
    # Functie care gaseste drumul optim prin toate orasele si drumul optim de la sursa la destinatie
    # input - matrix,n , start, finish
    # output - [cost, path]
    # '''
    # def path(self, matrix, n, start, finish):
    #
    #     heap = []
    #     heapq.heapify(heap)
    #     for i in range(n):
    #         if i != start:
    #             heapq.heappush(heap,(matrix[start][i], [start, i]))
    #
    #     while 1:
    #         cost, path = heapq.heappop(heap)
    #
    #         #Verificam daca suntem la sursa sau la destinatie
    #         #Prima cerinta - sursa
    #         #A doua cerinta - destinatie
    #         if finish == path[-1] or start==path[-1]:
    #             return cost, path
    #
    #         #Prima cerinta
    #         #Cand am vizitat toate orasele, ne intoarcem la sursa
    #         if len(path) == n:
    #             copyPath = path.copy()
    #             copyPath.append(start)
    #             heapq.heappush(heap,(cost + matrix[path[-1]][start], copyPath))
    #
    #         for i in range(n):
    #             if i not in path:
    #                 copyPath = path.copy()
    #                 copyPath.append(i)
    #                 heapq.heappush(heap,(cost + matrix[path[-1]][i], copyPath))