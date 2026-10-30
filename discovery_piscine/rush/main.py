#!/usr/bin/env python3
# Game of the Year Vote
# Each user logs in and can vote for one game per day.

from datetime import date, timedelta

BOX_WIDTH = 46                            # width of the game board boxes
BAR_MAX = 10                              # longest leaderboard bar


def today():
    """Return today's date as text, e.g. "2026-10-29".
    FIX: a function (not a constant) so the date stays correct after midnight."""
    return date.today().isoformat()


def days_ago(n):
    """Return the date n days before today as text, e.g. "2026-10-27"."""
    return (date.today() - timedelta(days=n)).isoformat()


# ============================================================
# DATA (mock data so the demo already has results to show)
# ============================================================
games = {
    1: {"title": "Starfall Odyssey", "genre": "RPG",
        "platform": "PC", "studio": "Nova Forge"},
    2: {"title": "Pixel Kingdom", "genre": "Strategy",
        "platform": "Switch", "studio": "Tiny Crown"},
    3: {"title": "Shadow Circuit", "genre": "Action",
        "platform": "PS5", "studio": "Neon Wolf"},
    4: {"title": "Farm Tales", "genre": "Simulation",
        "platform": "Mobile", "studio": "Green Leaf"},
    5: {"title": "Echoes of Atlas", "genre": "Adventure",
        "platform": "Xbox", "studio": "Blue Harbor"},
}

users = {
    "base": {"password": "1234"},
    "mint": {"password": "1234"},
    "ton": {"password": "1234"},
    "fah": {"password": "1234"},
}

votes = [
    {"user": "base", "game": 1, "date": days_ago(2)},
    {"user": "mint", "game": 2, "date": days_ago(2)},
    {"user": "ton", "game": 1, "date": days_ago(2)},
    {"user": "fah", "game": 3, "date": days_ago(2)},
    {"user": "base", "game": 1, "date": days_ago(1)},
    {"user": "mint", "game": 3, "date": days_ago(1)},
    {"user": "ton", "game": 5, "date": days_ago(1)},
    {"user": "fah", "game": 1, "date": days_ago(1)},
    {"user": "ton", "game": 2, "date": today()},
]


# ============================================================
# INPUT HELPERS - the program never crashes on bad input
# ============================================================
def get_int(prompt, min_value, max_value):
    """Ask until the user types a whole number in range. Returns it."""
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


def get_text(prompt, lower=True):
    """Ask until the user types something not empty. Returns the text."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("Input cannot be empty.")
            continue
        if lower:
            return text.lower()
        return text


def pause():
    input("\nPress Enter to continue...")


# ============================================================
# DATA PROCESSING (functions that return values)
# ============================================================
def find_today_vote(votes, username):
    """Return this user's vote for today, or None if they have not voted."""
    for vote in votes:
        if vote["user"] == username and vote["date"] == today():
            return vote
    return None


def count_votes(votes, only_date=None):
    """Return {game_id: number_of_votes}. only_date limits it to one day."""
    result = {}
    for vote in votes:
        if only_date is not None and vote["date"] != only_date:
            continue
        result[vote["game"]] = result.get(vote["game"], 0) + 1
    return result


def get_ranking(votes, games):
    """Return a list of (game_id, votes), most votes first.
    Games with no votes are included with 0. Ties are sorted by title."""
    totals = count_votes(votes)
    ranking = []
    for game_id in games:
        ranking.append((game_id, totals.get(game_id, 0)))
    ranking.sort(key=lambda item: (-item[1], games[item[0]]["title"]))
    return ranking


def get_ranks(ranking):
    """Return {game_id: rank}. FIX: games with the same votes share a rank
    (e.g. 1, 2, 2, 4) instead of getting different ranks."""
    ranks = {}
    previous_count = None
    rank = 0
    for position, (game_id, count) in enumerate(ranking, 1):
        if count != previous_count:
            rank = position
            previous_count = count
        ranks[game_id] = rank
    return ranks


def search_games(games, keyword):
    """Return a list of game ids whose title contains the keyword."""
    found = []
    for game_id, game in games.items():
        if keyword in game["title"].lower():
            found.append(game_id)
    return found


# ============================================================
# DISPLAY
# ============================================================
def box_line(text=""):
    """Return one line of a box: | text            |"""
    return f"| {text:<{BOX_WIDTH - 4}} |"


def show_game_card(game_id, game, extra_lines=None):
    border = "+" + "-" * (BOX_WIDTH - 2) + "+"
    print(border)
    print(box_line(f"GAME #{game_id}  {game['title']}"))
    print(box_line())
    print(box_line(f"   Genre    : {game['genre']}"))
    print(box_line(f"   Platform : {game['platform']}"))
    print(box_line(f"   Studio   : {game['studio']}"))
    if extra_lines:
        print(box_line())
        for line in extra_lines:
            print(box_line(f"   {line}"))
    print(border)


def show_games(games):
    print("\n========== NOMINATED GAMES ==========")
    for game_id, game in games.items():
        show_game_card(game_id, game)


def show_welcome_menu():
    print()
    print("=========== GAME OF THE YEAR VOTE ===========")
    print(f"Today: {today()}")
    print("1. View nominated games")
    print("2. Login")
    print("3. Register")
    print("0. Exit")


def show_user_menu(username):
    print()
    print(f"=========== Welcome, {username}! ===========")
    print(f"Today: {today()}")
    if find_today_vote(votes, username) is None:
        print("You have not voted today.")
    else:
        print("You already voted today.")
    print("1. View nominated games")
    print("2. Vote")
    print("3. Change today's vote")
    print("4. Cancel today's vote")
    print("5. My vote history")
    print("6. Results")
    print("0. Logout")


# ============================================================
# ACCOUNT
# ============================================================
def register(users):
    print("\n----- REGISTER -----")
    username = get_text("Username: ")
    # RULE: usernames must be unique
    if username in users:
        print("This username is already taken.")
        return
    if " " in username:
        print("Username cannot contain spaces.")
        return
    password = get_text("Password (at least 4 characters): ", lower=False)
    if len(password) < 4:
        print("Password is too short.")
        return
    users[username] = {"password": password}
    print(f"Account '{username}' created. You can login now.")


def login(users):
    """Return the username if login works, otherwise None."""
    print("\n----- LOGIN -----")
    username = get_text("Username: ")
    if username not in users:
        print("User not found. Please register first.")
        return None
    password = get_text("Password: ", lower=False)
    if password != users[username]["password"]:
        print("Wrong password.")
        return None
    return username


# ============================================================
# VOTING
# ============================================================
def choose_game(games):
    """Show the games and return the game id the user picks."""
    print()
    for game_id, game in games.items():
        print(f"  {game_id}. {game['title']} ({game['genre']})")
    # FIX: check the id really exists, so non-consecutive ids never crash
    while True:
        game_id = get_int("Choose a game number: ", min(games), max(games))
        if game_id in games:
            return game_id
        print("There is no game with that number.")


def cast_vote(votes, games, username):
    # RULE: one vote per user per day
    if find_today_vote(votes, username) is not None:
        print("You already voted today. Use 'Change today's vote' instead.")
        return
    game_id = choose_game(games)
    votes.append({"user": username, "game": game_id, "date": today()})
    print(f"Thank you! You voted for {games[game_id]['title']}.")


def change_vote(votes, games, username):
    # RULE: only today's vote can be changed
    vote = find_today_vote(votes, username)
    if vote is None:
        print("You have no vote today to change.")
        return
    print(f"Your vote today: {games[vote['game']]['title']}")
    new_game = choose_game(games)
    if new_game == vote["game"]:
        print("That is already your vote. Nothing changed.")
        return
    vote["game"] = new_game
    print(f"Vote changed to {games[new_game]['title']}.")


def cancel_vote(votes, games, username):
    vote = find_today_vote(votes, username)
    if vote is None:
        print("You have no vote today to cancel.")
        return
    title = games[vote["game"]]["title"]
    answer = get_text(f"Cancel your vote for {title}? (y/n): ")
    if answer in ("y", "yes"):           # FIX: accept "yes" too
        votes.remove(vote)
        print("Your vote was cancelled.")
    else:
        print("Nothing changed.")


def show_history(votes, games, username):
    print(f"\n----- VOTE HISTORY: {username} -----")
    my_votes = []
    for vote in votes:
        if vote["user"] == username:
            my_votes.append(vote)
    if len(my_votes) == 0:
        print("You have not voted yet.")
        return
    my_votes.sort(key=lambda vote: vote["date"])
    for vote in my_votes:
        mark = "  <- today" if vote["date"] == today() else ""
        print(f"{vote['date']}  {games[vote['game']]['title']}{mark}")
    print(f"Total votes: {len(my_votes)}")


# ============================================================
# RESULTS
# ============================================================
def show_all_results(votes, games):
    ranking = get_ranking(votes, games)
    total = len(votes)
    print("\n================ LEADERBOARD ================")
    if total == 0:
        print("No votes yet.")
        return
    ranks = get_ranks(ranking)
    top = ranking[0][1]
    for game_id, count in ranking:
        percent = count * 100 / total
        # FIX: scale the bar so it never gets longer than BAR_MAX
        bar = "█" * round(count * BAR_MAX / top) if top > 0 else ""
        title = games[game_id]["title"]
        print(f"{ranks[game_id]}. {title:<18} {bar:<{BAR_MAX}} {count:>2} ({percent:.0f}%)")
    print(f"Total votes: {total}")


def search_result(votes, games):
    keyword = get_text("Search game name: ")
    found = search_games(games, keyword)
    if len(found) == 0:
        print(f"No game matches '{keyword}'.")
        return
    ranking = get_ranking(votes, games)
    ranks = get_ranks(ranking)
    totals = dict(ranking)
    today_totals = count_votes(votes, today())
    total = len(votes)
    for game_id in found:
        rank = ranks[game_id]
        count = totals[game_id]
        percent = count * 100 / total if total > 0 else 0
        show_game_card(game_id, games[game_id], [
            f"Rank        : {rank} of {len(games)}",
            f"Total votes : {count} ({percent:.0f}%)",
            f"Today       : {today_totals.get(game_id, 0)}",
        ])


def results_menu(votes, games):
    while True:
        print("\n----- RESULTS -----")
        print("1. Show all")
        print("2. Search a game")
        print("0. Back")
        choice = get_int("Choose: ", 0, 2)
        if choice == 1:
            show_all_results(votes, games)
        elif choice == 2:
            search_result(votes, games)
        else:
            return


# ============================================================
# MAIN LOOPS
# ============================================================
def user_session(username):
    """Menu after login. Returns when the user logs out."""
    while True:
        show_user_menu(username)
        choice = get_int("Choose: ", 0, 6)
        if choice == 1:
            show_games(games)
            pause()
        elif choice == 2:
            cast_vote(votes, games, username)
        elif choice == 3:
            change_vote(votes, games, username)
        elif choice == 4:
            cancel_vote(votes, games, username)
        elif choice == 5:
            show_history(votes, games, username)
        elif choice == 6:
            results_menu(votes, games)
        else:
            print(f"Goodbye, {username}. You are logged out.")
            return


def main():
    while True:
        show_welcome_menu()
        choice = get_int("Choose: ", 0, 3)
        if choice == 1:
            show_games(games)
            pause()
        elif choice == 2:
            username = login(users)
            if username is not None:
                user_session(username)
        elif choice == 3:
            register(users)
        else:
            print("Goodbye!")
            return


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")