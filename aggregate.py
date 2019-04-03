import csv
import json

data = []

with open("data/commits.json") as f:
    for line in f:
        parsed = json.loads(line)

        email = parsed["payload"]["commits"][0]["author"]["email"]

        current = {}
        current["id"] = parsed["id"]
        current["repository_name"] = parsed["repo"]["name"]
        current["ref"] = parsed["payload"]["ref"]
        current["author_email"] = email
        current["author_domain"] = email.split("@")[1]
        current["author_name"] = parsed["payload"]["commits"][0]["author"]["name"]
        current["message"] = parsed["payload"]["commits"][0]["message"]
        current["sha"] = parsed["payload"]["commits"][0]["sha"]
        if "org" in parsed:
            current["organisation_name"] = parsed["org"]["login"]
        else:
            current["organisation_name"] = None
        current["created_at"] = parsed["created_at"]

        data.append(current)

with open("data/commits.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
