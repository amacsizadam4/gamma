import random

def simulate_dice_rolls():
    results=[0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,1000):
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        outcome=dice1+dice2
        results[outcome-2]+=1
    # TÜM sonuçları görmek için (2'den 12'ye hepsi):
    for i in range(11):  # 0, 1, 2, ..., 10
        print(f"Toplam {i+2}: {results[i]} kez")

# a function to roll dice a million times and return the results
def roll_dice(num_rolls=1000000):
    results = [0] * 11  # Initialize a list to hold counts for sums 2-12
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        outcome = dice1 + dice2
        results[outcome - 2] += 1  # Increment the count for this outcome
    return results

if __name__ == "__main__":
    simulate_dice_rolls()