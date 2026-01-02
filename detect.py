from datetime import datetime

FAILED_LIMIT = 2

def parse_auth_log(path):
    events = []
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split()
            timestamp = " ".join(parts[0:2])
            user = parts[3].split("=")[1]
            status = parts[4].split("=")[1]
            events.append({
                "time": datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                "user": user,
                "status": status
            })
    return events


def detect_bruteforce(events):
    failures = {}
    alerts = []

    for event in events:
        user = event["user"]

        if event["status"] == "FAIL":
            failures[user] = failures.get(user, 0) + 1

        elif event["status"] == "SUCCESS":
            if failures.get(user, 0) >= FAILED_LIMIT:
                alerts.append(f"ALERT: Possible brute force on user {user}")
            failures[user] = 0  # reset after success

    return alerts


if __name__ == "__main__":
    auth_events = parse_auth_log("logs/simulated/auth.log")
    alerts = detect_bruteforce(auth_events)

    for alert in alerts:
        print(alert)
