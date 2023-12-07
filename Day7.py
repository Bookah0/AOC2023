import re
from collections import defaultdict

hand_type_dicts = {'high_card': [],
                  'one_pair': [],
                  'two_pair': [],
                  'four_of_a_kind': [],
                  'three_of_a_kind': [],
                  'five_of_a_kind': [],
                  'full_house': []}


def parse_input(part):
    value_dict = {}
    if part == 1:
        value_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    elif part == 2:
        value_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': -1, 'Q': 12, 'K': 13, 'A': 14}

    lines = open('Input/Day7.txt', "r").readlines()

    for line in lines:
        hand, bid = re.match(r'(.+) (.+)', line).groups()
        value_hand = [value_dict[suite] for suite in hand]
        hand_type_dicts[get_hand_type(value_hand)].append((value_hand, int(bid)))

    return len(lines)


def get_hand_type(hand):
    n_jokers, n_list = get_n_cards_in_hand(hand)
    found_pair, used_jokers, has_three = False, False, False

    if n_jokers == 5:
        return 'five_of_a_kind'

    for i in range(len(n_list)-1, -1, -1):
        count = n_list[i]
        if count + n_jokers == 5:
            return 'five_of_a_kind'
        elif count + n_jokers == 4:
            return 'four_of_a_kind'
        elif count == 3 and not has_three:
            has_three = True
        elif count + n_jokers == 3 and not used_jokers:
            has_three, used_jokers = True, True
        elif count == 2:
            if found_pair:
                return 'two_pair'
            found_pair = True
        elif count + n_jokers == 2 and not used_jokers:
            if found_pair:
                return 'two_pair'
            found_pair, used_jokers = True, True

    if has_three:
        if found_pair:
            return 'full_house'
        else:
            return 'three_of_a_kind'
    if found_pair:
        return 'one_pair'
    else:
        return 'high_card'


def get_n_cards_in_hand(hand):
    temp_dict = defaultdict(int)
    n_jokers = 0

    for suite in hand:
        if suite != -1:
            temp_dict[suite] += 1
        else:
            n_jokers += 1

    return n_jokers, sorted(temp_dict.values())


def solve_input():
    max_rank = parse_input(2)
    hands_by_rank = sort_hands_by_rank()
    tot_winnings = 0

    for i, hand in enumerate(hands_by_rank):
        tot_winnings += hand[1] * (max_rank-i)

    return tot_winnings


def sort_hands_by_rank():
    hands_by_rank = []
    hand_types_by_rank = ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']
    for hand_type in hand_types_by_rank:
        hands_by_rank.extend(sorted(hand_type_dicts[hand_type], key=get_tuple_items))
    return hands_by_rank


def get_tuple_items(t):
    return tuple(-x for x in t[0]), t[0]


if __name__ == '__main__':
    print(solve_input())


