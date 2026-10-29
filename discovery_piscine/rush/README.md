# Game of the Year Vote

A terminal application for voting on the Game of the Year. Each registered user
can vote for one nominated game per day, change or cancel today's vote, and see
the live leaderboard.

## Purpose

Online polls are easy to spam and hard to follow. This app keeps the vote fair
(one vote per person per day) and shows clear results, both as a full ranking
and for any single game.

## How to run

```bash
python3 main.py
```

or, after `chmod +x main.py`:

```bash
./main.py
```

Demo accounts (password `1234` for all): `base`, `mint`, `ton`, `fah`.
You can also register a new account.

## Main features

**Before login**
- View nominated games (game board with genre, platform and studio)
- Login
- Register a new account
- Exit

**After login**
- View nominated games
- Vote for a game
- Change today's vote
- Cancel today's vote
- My vote history
- Results: show the full leaderboard, or search one game by name
- Logout

## Rules

1. A user can vote only once per day.
2. Only today's vote can be changed or cancelled. Past votes are locked.
3. Usernames must be unique, have no spaces, and passwords need at least 4 characters.
4. Only logged-in users can vote.

## Data processing

1. **Leaderboard**: counts every vote per game, sorts games from most to least
   votes (ties by title), and shows each game's share as a percentage and a bar.
2. **Search**: finds games whose title contains a keyword and shows each match's
   rank, total votes, share and votes received today.

## Data structures

- `games` — dictionary of game id to game details
- `users` — dictionary of username to account data
- `votes` — list of vote dictionaries (`user`, `game`, `date`)

Data lives in memory while the program runs and starts from mock data each time.