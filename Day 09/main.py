
discription = print('welcome to secret auction program')

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input('please enter your name:')
    price = input('how much is your bid price? $')
    bids[name] = int(price)
    should_continue = input('are there any other bidders?yes or no?')

    if should_continue == 'no':
        bidding_finished = True
        
        
def find_highest_bidder(bidding_record):
    winner = ''
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'the winner is {winner} with a bid of ${highest_bid}')
    
find_highest_bidder(bids)