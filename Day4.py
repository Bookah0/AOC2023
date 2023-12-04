import re


def parse_input():
    cards = []
    with open('Input/Day4.txt', "r") as f:
        for line in f.readlines():
            match = re.match(r'Card (.+): (.+) \| (.+)', line)
            cards.append((int(match.group(1)), match.group(2), match.group(3)))
    return cards


def solve_input1(cards, points=0):
    for card in cards:
        n_wins = sum(1 for number in card[1].split() if number in card[2].split())
        if n_wins != 0:
            points += 2**(n_wins-1)
    return points


def solve_input2(cards):
    for card in cards:
        n_wins = sum(1 for number in card[1].split() if number in card[2].split())
        cards.extend(cards[i] for i in range(card[0], card[0]+n_wins) if i < len(cards))
    return len(cards)


if __name__ == '__main__':
    print(solve_input2(parse_input()))