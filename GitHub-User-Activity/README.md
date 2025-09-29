# GitHub User Activity CLI

A simple command-line tool to fetch and display the recent activity of a GitHub user.

## Features
- Fetches recent activity using the GitHub API.
- Displays up to 10 recent events in the terminal.
- Handles common event types such as pushes, issues, stars, and forks.
- Provides error handling for invalid usernames or API errors.

## Usage

Run the script from the command line:

```bash
python3 github_activity.py <username>
```

### Example

```bash
python3 github_activity.py JayGemawat
```

**Output:**

```
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened an issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- Forked kamranahmedse/developer-roadmap
```

## Requirements
- Python 3.x
- No external libraries required (uses built-in `urllib` and `json` modules).

## Project Structure
```
GitHub-User-Activity/
│
├── github_activity.py   # Main CLI script
├── README.md            # Project documentation
```

