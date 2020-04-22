K_TOURNAMENT = 3
MUTATION_PROBABILITY = 1.00

import random

from modules import problem
from modules.genetics import utils
from modules.genetics.chromossome import Chromossome

def selection(population):
    # Tournament selection without selective pressure

    parents = []
    while len(parents) != 2:
        tournament_individuals = []

        for _ in range(K_TOURNAMENT):
            individual = random.choice(population)

            if not individual in tournament_individuals:
                tournament_individuals.append(individual)

        parent = parent_fitness = None
        for individual in tournament_individuals:
            individual_fitness = problem.g(individual)

            if parent is None or individual_fitness > parent_fitness:
                parent = individual
                parent_fitness = individual_fitness

        if parent not in parents:
            parents.append(parent)

    print(f"1st parent chosen for crossover: {utils.format_chromossome(parents[0])}")
    print(f"2nd parent chosen for crossover: {utils.format_chromossome(parents[1])}")

    return parents

def crossover(population, parent1, parent2):
    # Order crossover
    # http://mat.uab.cat/~alseda/MasterOpt/GeneticOperations.pdf

    parent1_genes = parent1.get_genes()
    parent2_genes = parent2.get_genes()

    genes_length = len(parent1_genes)

    child1_genes = [None] * genes_length
    child2_genes = [None] * genes_length

    parent1_subset_start = random.randint(0, genes_length - 1)
    parent2_subset_start = random.randint(0, genes_length - 1)

    parent1_subset_end = random.randint(parent1_subset_start + 1, genes_length)
    parent2_subset_end = random.randint(parent2_subset_start + 1, genes_length)

    print(f"1st parent subset indexes: {parent1_subset_start} (inclusive) to {parent1_subset_end} (exclusive)")
    print(f"2nd parent subset indexes: {parent2_subset_start} (inclusive) to {parent2_subset_end} (exclusive)")

    child1_genes[parent1_subset_start:parent1_subset_end] = parent1_genes[parent1_subset_start:parent1_subset_end]
    child2_genes[parent2_subset_start:parent2_subset_end] = parent2_genes[parent2_subset_start:parent2_subset_end]

    parent1_next_index = parent2_next_index = 0
    for i in range(genes_length):
        if child1_genes[i] is None:
            for k in range(parent2_next_index, genes_length):
                gene = parent2_genes[k]
                if gene in child1_genes:
                    continue
    
                child1_genes[i] = gene
                parent2_next_index = k + 1

                break

        if child2_genes[i] is None:
            for k in range(parent1_next_index, genes_length):
                gene = parent1_genes[k]
                if gene in child2_genes:
                    continue

                child2_genes[i] = gene
                parent1_next_index = k + 1

                break
                
    child1 = Chromossome()
    child1.set_genes(child1_genes)
    print(f"1st child generated from crossover: {utils.format_chromossome(child1)}")

    child2 = Chromossome()
    child2.set_genes(child2_genes)
    print(f"2nd child generated from crossover: {utils.format_chromossome(child2)}")

    population.append(child1)
    population.append(child2)

def mutation(population):
    # Swap mutation (avoid illegal genotype)

    prob = random.uniform(0, 1)

    if prob >= MUTATION_PROBABILITY:
        return

    target = random.choice(population)

    genes = target.get_genes()

    genes_length = len(genes)

    mutation_point_1 = mutation_point_2 = -1
    while mutation_point_1 == mutation_point_2:
        mutation_point_1 = random.choice(range(genes_length))
        mutation_point_2 = random.choice(range(genes_length))

    print(f"Invididual {target.to_string()} will mutate at points ({mutation_point_1}, {mutation_point_2})")

    genes[mutation_point_1], genes[mutation_point_2] = genes[mutation_point_2], genes[mutation_point_1]

    print(f"Individual {target.to_string()} mutated at points ({mutation_point_1}, {mutation_point_2})")

def elitism(population):
    for _ in range(2):
        worst_individual = utils.find_worst_chromossome(population)
        print(f"Removing worst individual from population: {utils.format_chromossome(worst_individual)}")
        population.remove(worst_individual)