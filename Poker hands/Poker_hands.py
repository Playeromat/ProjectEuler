def analyse_hand(hand):
    hand_value = [0, 0]

    card_values = {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "T": 0,
        "J": 0,
        "Q": 0,
        "K": 0,
        "A": 0
    }

    card_colours = {
        "C": 0,
        "S": 0,
        "D": 0,
        "H": 0
    }

    for card in hand:
        card_values[list(card)[0]] += 1
        card_colours[list(card)[1]] += 1

    pairs = count_pairs(card_values)

    if is_straight(card_values):
        hand_value[0] = 5
        if is_flush(card_colours):
            hand_value[0] = 9
            if card_values["A"] == 1:
                hand_value[0] = 10
    if is_flush(card_colours):
        hand_value[0] = 6
    if is_foak(card_values):
        hand_value[0] = 8
    if pairs >= 1:
        hand_value[0] = 2
        if pairs == 2:
            hand_value[0] = 3
    if has_triple(card_values):
        hand_value[0] = 4
        if pairs == 1:
            hand_value[0] = 7

    hand_value[1] = get_highest_card_value(card_values)

    return hand_value


def get_highest_card_value(card_values):
    highest_card_value = 0
    index = 0
    for card_value in card_values:
        if card_values[card_value] >= 1:
            highest_card_value = index
        index += 1

    return highest_card_value


def is_foak(card_values):
    for card_value in card_values:
        if card_values[card_value] == 4:
            return True
    return False


def count_pairs(card_values):
    pairs = 0
    for card_value in card_values:
        if card_values[card_value] == 2:
            pairs += 1

    return pairs


def has_triple(card_values):
    for card_value in card_values:
        if card_values[card_value] == 3:
            return True


def is_straight(card_values):
    cards_in_a_row = 0
    for card_value in card_values:
        if cards_in_a_row == 5:
            return True

        if card_values[card_value] > 1 or card_values[card_value] == 0 and cards_in_a_row > 0:
            return False

        if card_values[card_value] == 1:
            cards_in_a_row += 1


def is_flush(card_colours):
    for colour in card_colours:
        if colour == 5:
            return True

        if colour == 0:
            continue

        return False


def analyse_file():
    file = open('poker.txt', 'r')

    player1_wins = 0
    player2_wins = 0

    for match in file:
        cards = match.split()

        index = 0
        player1_hand = []
        player2_hand = []
        for card in cards:
            if index < 5:
                player1_hand.append(card)
            else:
                player2_hand.append(card)
            index += 1

        player1_hand_value = analyse_hand(player1_hand)
        player2_hand_value = analyse_hand(player2_hand)

        if player1_hand_value[0] == player2_hand_value[0]:
            if player1_hand_value[1] > player2_hand_value[1]:
                player1_wins += 1
            else:
                player2_wins += 1
        else:
            if player1_hand_value[0] > player2_hand_value[0]:
                player1_wins += 1
            if player2_hand_value[0] > player1_hand_value[0]:
                player2_wins += 1

    print(player1_wins)
    print(player2_wins)

    file.close()


analyse_file()
