import matplotlib.pyplot as plt

import modules.problem as problem
from modules.genetics import operators
from modules.genetics import utils
from modules.genetics.chromossome import Chromossome

if __name__ == "__main__":
    population = [Chromossome() for _ in range(10)]

    generation = 0
    population_score = problem.g_average(population)
    print(f"Generation # {generation} -> Average population score = {population_score:.3f}\n")

    generation_plot = []
    generation_plot.append(generation)

    population_score_plot = []
    population_score_plot.append(population_score)

    while generation < 50:
        # pylint: disable=unbalanced-tuple-unpacking
        parent1, parent2 = operators.selection(population)

        operators.crossover(population, parent1, parent2)
        operators.mutation(population)
        operators.elitism(population)

        generation += 1
        population_score = problem.g_average(population)

        generation_plot.append(generation)
        population_score_plot.append(population_score)

        print(f"Generation # {generation} -> Average population score = {population_score:.3f}\n")

        if generation <= 40:
            # Start with a high mutation rate to cover a lot of the solution space and then cool
            # it down to better optimize local optima.
            # 100% -> 5% in 40 generations
            # Keep 5% until last generation
            
            operators.MUTATION_PROBABILITY -= 2.375

    best_chromossome = utils.find_best_chromossome(population)
    print(f"Best individual: {utils.format_chromossome(best_chromossome)}")
    
    plt.gca().set_xlabel("Generation")
    plt.gca().set_ylabel("Average fitness")
    plt.gca().set_title("Average fitness per generation")
    plt.plot(generation_plot, population_score_plot)
    plt.show()