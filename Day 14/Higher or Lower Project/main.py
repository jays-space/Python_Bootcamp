# TODO: Day 14 solution walkthrough
import random

import art
from game_data import data
from art import *

def main():
    score = 0
    has_lost = False
    nof_loops = 0

    # TODO: loop -> while winning, tally score until lose. Then show score
    while not has_lost:
        nof_loops += 1
        # TODO: Generate 2 random samples: random.sample(range(len(data)), 2) -> sample = [5, 9] (DONE
        samples = random.sample(range(len(data)), 2)

        # TODO: Extract the samples from the dataset -> comparison_a = data[sample[0]], comparison_b = data[sample[1]] (DONE)
        comparison_a = data[samples[0]]
        comparison_b = data[samples[1]]

        # TODO: Put comparisons in dict with keys as 'a' , and 'b':{name, follower_count, description, country, index} (DONE)
        comparisons = {
            'a': comparison_a,
            'b': comparison_b
        }

        # TODO: print comparison (DONE)
        #   ->      Compare A: {comparison_a['name']}, a {comparison_a['description']}, from {comparison_a['country']}
        #   ->      vs
        #   ->      Compare B: {comparison_b['name']}, a {comparison_b['description']}, from {comparison_b['country']}
        print(art.logo)
        print(f"Compare A: {comparisons['a']['name']}, a {comparisons['a']['description']}, from {comparisons['a']['country']}")
        print(art.vs)
        print(f"Compare B: {comparisons['b']['name']}, a {comparisons['b']['description']}, from {comparisons['b']['country']}")

        # TODO: Ask user comparison question input("Who has more followers? Type 'A' or 'B': ").lower() (DONE)
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        # TODO: Extract input answer as (comparisons['answer']['follower_count'])
        if answer == 'a':
            is_a_winner = comparisons[answer]['follower_count'] > comparisons['b']['follower_count']
            if is_a_winner:
                score += 1
                if nof_loops > 1:
                    print(f"\n" * 20)
                print(f"You're right! Current score: {score}")
            else:
                has_lost = True
                print("You lose")
        elif answer == 'b':
            is_b_winner = comparisons[answer]['follower_count'] > comparisons['a']['follower_count']
            if is_b_winner:
                score += 1
                if nof_loops > 1:
                    print(f"\n" * 20)
                print(f"You're right! Current score: {score}")
            else:
                has_lost = True
                print("You lose")
        else:
            print("Invalid input.")

    if has_lost:
        print(f"You have {score} tally.")


main()