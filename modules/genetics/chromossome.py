import random

from modules import problem

class Chromossome:
    def __init__(self, route = None):
        genes_length = len(problem.GRAPH) - 1

        genes = route is None and random.sample([i + 1 for i in range(genes_length)], genes_length) or Chromossome.get_genotype(route)

        self.__genes = genes

    def get_genes(self):
        return self.__genes

    def set_genes(self, genes):
        self.__genes = genes

    def to_string(self):
        chr_str = "G = [" + ", ".join(map(str, self.__genes)) + "], F = [" + ", ".join(map(str, Chromossome.get_fenotype(self.__genes))) + "]"

        return chr_str

    @staticmethod
    def get_genotype(route):
        return route[1:len(problem.GRAPH)]

    @staticmethod
    def get_fenotype(genes):
        total_vertexes = len(problem.GRAPH)

        route = [None] * (total_vertexes + 1)

        route[0] = 0
        route[total_vertexes] = 0
        route[1:total_vertexes] = genes

        return route