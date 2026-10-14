import random

MAX_ATTEMPTS = 7
LOW, HIGH = 1, 100


def play_round():
    """Play one round. Returns (won, attempts_used, points_earned)."""
    secret = random.randint(LOW, HIGH)
    attempts = 0
    print(f"\nI'm thinking of a number between {LOW} and {HIGH}.")
    print(f"You have {MAX_ATTEMPTS} attempts. Good luck!")

    while attempts < MAX_ATTEMPTS:
        guess_text = input(f"\nAttempt {attempts + 1}/{MAX_ATTEMPTS} - Your guess: ").strip()
        if not guess_text.isdigit():
            print("Please enter a valid whole number.")
            continue
        guess = int(guess_text)
        if guess < LOW or guess > HIGH:
            print(f"Enter a number between {LOW} and {HIGH}.")
            continue

        attempts += 1
        if guess == secret:
            points = (MAX_ATTEMPTS - attempts + 1) * 10
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            print(f"You earned {points} points.")
            return True, attempts, points
        elif guess > secret:
            print("Too High! ⬇️")
        else:
            print("Too Low! ⬆️")
        print(f"Attempts left: {MAX_ATTEMPTS - attempts}")

    print(f"\n😢 Out of attempts! The number was {secret}.")
    return False, attempts, 0


def main():
    total_score = 0
    rounds = 0
    wins = 0
    total_attempts = 0

    print("===== NUMBER GUESSING GAME =====")
    name = input("Enter your name: ").strip() or "Player"

    while True:
        won, attempts, points = play_round()
        rounds += 1
        total_attempts += attempts
        total_score += points
        if won:
            wins += 1

        print(f"\n--- {name}'s Stats ---")
        print(f"Rounds played : {rounds}")
        print(f"Wins          : {wins}")
        print(f"Total attempts: {total_attempts}")
        print(f"Total score   : {total_score}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print(f"Thanks for playing, {name}! Final score: {total_score}")
            break


if __name__ == "__main__":
    main()