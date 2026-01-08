def counter (name, const):
    count = {}
    for const_char in const:
        for name_char in name:
            if name_char.lower() == const_char.lower() and const_char in count:
                count[const_char] += 1
            elif name_char.lower() != const_char.lower() and const_char not in count:
                count[const_char] = 0

    return count

def calc_score(name, true_const, love_const):
    true_counter = counter(name, true_const)
    love_counter = counter(name, love_const)

    return {
        "name": name,
        "true_counter": true_counter,
        "love_counter": love_counter
    }

def get_scores(name):
    const_true = "TRUE"
    const_love = "LOVE"
    return calc_score(name, true_const = const_true, love_const = const_love)

def calculate_love_score(name1, name2, verbose = False):
    name1_scores = get_scores(name1)
    name2_scores = get_scores(name2)

    true_score = 0
    love_score = 0

    true_counter = name1_scores["true_counter"]
    love_counter = name1_scores["love_counter"]

    for key in name2_scores["true_counter"]:
        true_counter[key] = name1_scores['true_counter'][key] + name2_scores['true_counter'][key]
        if true_counter[key] > 0:
            true_score += true_counter[key]

    for key in name2_scores["love_counter"]:
        love_counter[key] = name1_scores['love_counter'][key] + name2_scores['love_counter'][key]
        if love_counter[key] > 0:
            love_score += love_counter[key]

    if verbose:
        for char in true_counter:
            print(f"{char} occurs {true_counter[char]} times.")
        print(f"Total: {true_score} \n")

        for char in love_counter:
            print(f"{char} occurs {love_counter[char]} times.")
        print(f"Total: {love_score} \n")

    return print(f"Love Score: {true_score}{love_score}")

# Call your function with hard coded values
# calculate_love_score("Angela Yu", "Jack Bauer", verbose = True)
calculate_love_score("Kanye West", "Kim Kardashian")