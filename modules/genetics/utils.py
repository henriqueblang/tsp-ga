from modules import problem

def find_best_chromossome(population):
    best_chromossome = None

    for chromossome in population:
        score = problem.g(chromossome)

        if best_chromossome is None or score > problem.g(best_chromossome):
            best_chromossome = chromossome

    return best_chromossome

def find_worst_chromossome(population):
    worst_chromossome = None

    for chromossome in population:
        score = problem.g(chromossome)

        if worst_chromossome is None or score < problem.g(worst_chromossome):
            worst_chromossome = chromossome

    return worst_chromossome

def format_chromossome(chromossome):
    return f"{chromossome.to_string()}, Score = {problem.g(chromossome):.3f}"