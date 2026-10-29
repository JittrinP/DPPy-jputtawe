#!/usr/bin/env python3
# Game of the Year Vote - vote for your favorite game, once per day

# ============================================================
# DATA (mock data so the demo has something to show)
# ============================================================
games = {
    "G1": {"title": "Starfall Odyssey", "genre": "RPG", "platform": "PC"},
    "G2": {"title": "Pixel Kingdom", "genre": "Strategy", "platform": "Switch"},
    "G3": {"title": "Shadow Circuit", "genre": "Action", "platform": "PS5"},
    "G4": {"title": "Farm Tales", "genre": "Simulation", "platform": "Mobile"},
}
voters = ["base", "mint", "ton"]
votes = [
    {"voter": "base", "game": "G1", "day": 1},
    {"voter": "mint", "game": "G2", "day": 1},
    {"voter": "ton", "game": "G1", "day": 1},
]
# Program starts on Day 2, so Day 1 is already closed (history for results)


# ============================================================
# INPUT HELPERS (done) - these handle most of criterion 7
# ============================================================
def get_int(prompt, min_value, max_value):
    """Ask until the user types a whole number in range. Returns the number."""
    while True:
        text = input(prompt).strip()
        try:
            number = int(text)
        except ValueError:
            print("Please enter a number.")
            continue
        if number < min_value or number > max_value:
            print(f"Please enter a number from {min_value} to {max_value}.")
            continue
        return number


def get_text(prompt):
    """Ask until the user types something not empty. Returns lowercase text."""
    while True:
        text = input(prompt).strip().lower()
        if text == "":
            print("Input cannot be empty.")
        else:
            return text


# ============================================================
# LOOKUP / CALCULATION (return values - criterion 5)
# ============================================================
def find_game(games, keyword):
    """Return the game id ("G1") that matches an id or a title, else None."""
    # TODO
    # 1. for game_id, game in games.items():
    # 2.   if keyword == game_id.lower() or keyword == game["title"].lower()
    #        -> return game_id
    # 3. after the loop -> return None
    pass


def find_today_vote(votes, voter, day):
    """Return this voter's vote dict for this day, else None."""
    # TODO
    # for each vote in votes:
    #   if vote["voter"] == voter and vote["day"] == day -> return vote
    # after the loop -> return None
    pass


def count_votes(votes, day=None):
    """Return a dict {game_id: number_of_votes}.
    day=None counts every day, day=3 counts only Day 3."""
    # TODO
    # 1. result = {}
    # 2. for each vote: skip it if day is not None and vote["day"] != day
    # 3.   result[vote["game"]] = result.get(vote["game"], 0) + 1
    # 4. return result
    pass


# ============================================================
# SCREENS / ACTIONS
# ============================================================
def show_menu(day):
    print()
    print(f"===== GAME OF THE YEAR VOTE  |  Day {day} =====")
    print("1. View nominated games")
    print("2. Register voter")
    print("3. Vote")
    print("4. Change today's vote")
    print("5. Cancel today's vote")
    print("6. Vote history")
    print("7. Results & statistics")
    print("8. End day")
    print("0. Exit")


def show_games(games):
    # TODO
    # for game_id, game in games.items(): print id, title, genre, platform
    pass


def register_voter(voters):
    # TODO
    # 1. name = get_text("Your name: ")
    # 2. RULE: name already in voters -> reject
    # 3. else voters.append(name) and confirm
    pass


def cast_vote(votes, voters, games, day):
    # TODO
    # 1. voter = get_text("Your name: ")
    # 2. RULE: voter not in voters -> "please register first", return
    # 3. RULE: find_today_vote(...) is not None -> "already voted today", return
    # 4. show_games(games), keyword = get_text(...), game_id = find_game(...)
    # 5. game_id is None -> "game not found", return
    # 6. votes.append({"voter": voter, "game": game_id, "day": day})
    pass


def change_vote(votes, games, day):
    # TODO
    # 1. voter = get_text(...)
    # 2. vote = find_today_vote(votes, voter, day)
    #    RULE: only today's vote can change -> None means "no vote today"
    # 3. ask new game, find_game(...), not found -> reject
    # 4. vote["game"] = new_game_id
    pass


def cancel_vote(votes, day):
    # TODO
    # 1. voter = get_text(...)
    # 2. vote = find_today_vote(votes, voter, day)
    # 3. None -> "you have no vote today"
    # 4. votes.remove(vote) and confirm
    pass


def show_history(votes, games):
    # TODO
    # 1. if votes is empty -> "No votes yet", return
    # 2. for each vote: print(f"Day {d} - {voter} -> {title}")
    #    (title = games[vote["game"]]["title"])
    pass


def show_results(votes, games, day):
    # TODO
    # PROCESSING 1 - leaderboard (all days)
    #   totals = count_votes(votes)
    #   if totals is empty -> "No votes yet", return (avoid dividing by 0)
    #   ranking = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    #   for each: title, "█" * count, count, percent
    # PROCESSING 2 - winner of each closed day (1 .. day - 1)
    #   for d in range(1, day): count_votes(votes, d) -> highest
    #   decide what happens on a tie!
    pass


def end_day(votes, games, day):
    """Show today's result and return the next day number."""
    # TODO
    # 1. show today's winner using count_votes(votes, day)
    # 2. return day + 1
    return day + 1


# ============================================================
# MAIN LOOP
# ============================================================
def main():
    current_day = 2
    while True:
        show_menu(current_day)
        choice = get_int("Choose: ", 0, 8)
        if choice == 1:
            show_games(games)
        elif choice == 2:
            register_voter(voters)
        elif choice == 3:
            cast_vote(votes, voters, games, current_day)
        elif choice == 4:
            change_vote(votes, games, current_day)
        elif choice == 5:
            cancel_vote(votes, current_day)
        elif choice == 6:
            show_history(votes, games)
        elif choice == 7:
            show_results(votes, games, current_day)
        elif choice == 8:
            current_day = end_day(votes, games, current_day)
        else:
            print("Goodbye!")
            break


main()