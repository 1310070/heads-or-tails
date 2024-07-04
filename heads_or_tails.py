import random

def coin_toss():
    return "Heads" if random.randint(0, 1) == 0 else "Tails"

def main():
    print("コインを投げます...")
    results = [coin_toss() for _ in range(3)]
    
    for i, result in enumerate(results, 1):
        print(f"ラウンド {i}: {result}")
    
    heads_count = results.count("Heads")
    tails_count = results.count("Tails")
    
    print(f"Heads: {heads_count}, Tails: {tails_count}")
    
    if heads_count > tails_count:
        print("あなたの勝ちです！")
    else:
        print("あなたの負けです。")

if __name__ == "__main__":
    main()
