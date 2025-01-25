import random

# Function for rolling dice
def roll_dice():
    return random.randint(1, 6)

#Function to play single round of game
def play_round(players, scores):
    print("\n---New Round---")
    #Dictionary to store the scores
    round_scores = {}

    #Each player rolls the dice
    for player in players:
        total_roll = 0
        while True:
            roll = roll_dice()
            print(f"{player} rolls {roll}.")
            total_roll += roll
            if roll != 6:
                break
            print(f"{player} rolled 6 and gets an extra turn!")

        #Store the player's total score
        round_scores[player] = total_roll
        print(f"{player}'s total for this round: {total_roll}")

    #Determine the winner of the round
    max_score = max(round_scores.values())
    winners = [player for player, score in round_scores.items() if score == max_score]

    if len(winners) > 1:
        print(f"It's a tie between {' and ' .join(winners)} with {max_score}!")
    else:
        winner = winners[0]
        print(f"\n{winner} wins this round with score: {max_score}")
        scores[winner] += 1

    return scores

# Function to display the leaderboard with total wins
def display_leaderboard(scores):
    print(f"\n---Leaderboard---")
    for player, wins in scores.items():
        print(f"{player}: {wins} wins(s)")

# Main function to run the game
def main():
    print("Welcome to the virtual Dice-Rolling Game!")

    num_players = 0
    while num_players < 2 or num_players > 4:
        try:
            num_players = int(input("Enter the number of players: "))
        except ValueError:
            print("Please enter the valid number.")

    players = [input(f"Enter the name for player {i+1}: ") for i in range(num_players)]
    scores = {player: 0 for player in players}

    while True:
        scores = play_round(players, scores)
        display_leaderboard(scores)

        play_again = input("\nPlay another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    max_wins = max(scores.values())
    overall_winners = [player for player, wins in scores.items() if wins == max_wins]

    print("\n---Game Over---")
    if len(overall_winners) > 1:
        print(f"It's a tie between {' and '.join(overall_winners)} with {max_wins} win(s)!")
    else:
        print(f"Congratulations {overall_winners[0]}! You are the winner with {max_wins} win(s)!")

if __name__ == "__main__":
    main()