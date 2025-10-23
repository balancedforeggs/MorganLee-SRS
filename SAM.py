def bananabid(my_player_number, my_bananas, monkey_position, opponent_bananas, past_bid_list, turn_number):

  # figuring out how far away the monkey is
  #(easier than using positions because the meaning of the positions flips depending on whether you're player 1 or 2)
  if my_player_number == 1:
    monkey_distance = 3 + monkey_position
  else:
    monkey_distance = 3 - monkey_position

  #idk put strategy here i guess
  if monkey_distance == 1 and my_bananas > opponent_bananas:
    bid = my_bananas

  if turn_number == 1:
    bid = 21
  else:
    last_turn = past_bid_list[-1]
    last_bid = last_turn[2 - my_player_number]
    if last_bid <= my_bananas/monkey_distance:
      bid = last_bid + 1
    else:
      bid = my_bananas/monkey_distance

  return bid
