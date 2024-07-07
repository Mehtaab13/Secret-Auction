from art import logo

print(logo)

print("Welcome to the secret auction. Let the bidding begin!")

bids = {}
initial_bidder = input("What is your name? ")
initial_bid = input("Hello " + initial_bidder + ", how much would you like to bid? ")
bids[initial_bidder] = int(initial_bid)
highest_bidder = initial_bidder

keep_playing = "yes"

keep_play = input("Are there any other bidders? ")
if keep_play == "yes":
    keep_playing = "yes"
else:
    keep_playing = "no"

while keep_playing == "yes":
    bidder = input("What is your name? ")
    bid = input("Hello " + bidder + ", how much would you like to bid? ")
    bids[bidder] = int(bid)
    current_highest_bid = bids[highest_bidder]
    if int(bid) > current_highest_bid:
        highest_bidder = bidder
    continue_keep_play = input("Are there any other bidders? ")
    if continue_keep_play == "yes":
        keep_playing = "yes"
    else:
        keep_playing = "no"

print("Congratulations " + highest_bidder + ", you have won the bid with a bid of $" + str(bids[highest_bidder]) + ".")
