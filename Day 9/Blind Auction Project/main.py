import art

bids = {}
active_bidding = True

print(art.logo)
print("Welcome to the secret auction programs")


def make_bid():
# TODO-1: Ask the user for input
    name = input("What is your name? ")
    bid = input("What's your bid? ")

# TODO-2: Save data into dictionary {name: price}
    bids[name] = int(bid)

# TODO-3: Whether if new bids need to be added
    new_bidder = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    return new_bidder

# TODO-4: Compare bids in dictionary
def compare_bids():
    max_bidder = max(bids, key=bids.get)
    print("\n" * 100)
    print(f"The winner is {max_bidder} with a bid of ${bids[max_bidder]}.")


while active_bidding:
    continue_bidding = make_bid()
    if continue_bidding == "no":
        active_bidding = False
        compare_bids()
        continue
    else:
        print("\n" * 100)