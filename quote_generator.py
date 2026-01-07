import random
import datetime

def load_quotes(file_path="quotes.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            quotes = f.readlines()
        return [q.strip() for q in quotes if q.strip()]
    except FileNotFoundError:
        return []

def get_random_quote(quotes):
    return random.choice(quotes)

def main():
    quotes = load_quotes()
    if not quotes:
        print("No quotes found. Add some quotes to quotes.txt")
        return

    quote = get_random_quote(quotes)
    today = datetime.date.today()

    print("📅 Date:", today)
    print("💡 Quote of the Day:")
    print(f"“{quote}”")

if __name__ == "__main__":
    main()
