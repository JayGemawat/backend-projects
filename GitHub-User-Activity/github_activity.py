#!/usr/bin/env python3
import sys
import urllib.request
import json

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                print(f"Error: Failed to fetch activity (status {response.status})")
                return []
            data = response.read().decode()
            return json.loads(data)
    except urllib.error.URLError as e:
        print(f"Error: Could not reach GitHub API ({e.reason})")
        return []
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return []

def display_activity(events):
    if not events:
        print("No recent activity found.")
        return

    for event in events[:10]:  
        event_type = event.get("type")
        repo_name = event["repo"]["name"]

        if event_type == "PushEvent":
            commit_count = len(event["payload"]["commits"])
            print(f"- Pushed {commit_count} commits to {repo_name}")
        elif event_type == "IssuesEvent":
            action = event["payload"]["action"]
            print(f"- {action.capitalize()} an issue in {repo_name}")
        elif event_type == "WatchEvent":
            print(f"- Starred {repo_name}")
        elif event_type == "ForkEvent":
            print(f"- Forked {repo_name}")
        else:
            print(f"- {event_type} in {repo_name}")

def main():
    if len(sys.argv) < 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1]
    events = fetch_github_activity(username) 
    display_activity(events)

if __name__ == "__main__":
    main()
