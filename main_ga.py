from enum import Enum
import time
import pygad
import numpy as np

from actions.move_down import MoveDown
from actions.move_left import MoveLeft
from actions.move_right import MoveRight
from actions.move_up import MoveUp
from entities.game import Game

movement_to_action_mapper = {
    1: MoveUp(),
    2: MoveDown(),
    3: MoveLeft(),
    4: MoveRight()
}

def round_move_value(value: int):
    if value < 1: return 1
    elif value > 4: return 4
    else: return value

def fitness_func(pygad, solution, solution_idx):
    game = Game()
    actions = [movement_to_action_mapper[round_move_value(int(move))] for move in solution]
    step_backs = len(list(filter(lambda move: move == 1, [round_move_value(int(move)) for move in solution])))
    (steps, max_score, score) = game.simulate(actions)
    fit = max_score * max_score / ( steps * step_backs)
    return fit if score > 0 else -fit

np.random.seed(10)
sol_per_pop = 20
num_genes = 200

init_range_low = 1
init_range_high = 4

mutation_probability = 0.25
num_generations=1000
num_parents_mating=8

ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    init_range_low=init_range_low,
    init_range_high=init_range_high,
    mutation_probability=mutation_probability
)

ga_instance.run()
ga_instance.plot_fitness()

best_actions = [movement_to_action_mapper[round_move_value(int(move))] for move in ga_instance.best_solution()[0]]

game = Game()
(steps, max_score, score) = game.simulate(best_actions)
print(steps)
print(score)

game = Game()
for action in best_actions:
    game.show()
    time.sleep(0.5)
    game.play(action)
    print("\033[H\033[2J", end='')
    if game.is_over():
        print("GAME OVER\n")
        break