from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["github_events"]
collection = db["events"]


def format_timestamp():
    return datetime.utcnow().strftime("%d %b %Y - %I:%M %p UTC")


@app.route("/webhook", methods=["POST"])
def webhook():
    print("\n========== WEBHOOK RECEIVED ==========")

    data = request.json
    event = request.headers.get("X-GitHub-Event")

    print("Event:", event)

    try:
        if event == "push":
            print("\n--- Processing PUSH ---")

            author = data["pusher"]["name"]
            to_branch = data["ref"].split("/")[-1]
            request_id = data["head_commit"]["id"]
            commit_message = data["head_commit"]["message"]

            print("Author:", author)
            print("Branch:", to_branch)
            print("Message:", commit_message)

            if "Merge pull request" in commit_message:
                print("⚠️ Skipping merge push event")
                return {"status": "ignored"}, 200

            if collection.find_one({"request_id": request_id}):
                print("⚠️ Duplicate PUSH ignored")
                return {"status": "duplicate"}, 200

            doc = {
                "request_id": request_id,
                "author": author,
                "action": "PUSH",
                "from_branch": None,
                "to_branch": to_branch,
                "timestamp": format_timestamp()
            }

            collection.insert_one(doc)
            print("✅ PUSH stored")

        elif event == "pull_request":
            print("\n--- Processing PULL REQUEST ---")

            pr = data["pull_request"]
            author = pr["user"]["login"]
            from_branch = pr["head"]["ref"]
            to_branch = pr["base"]["ref"]

            action_type = data["action"]

            print("PR Action:", action_type)
            print("Merged:", pr["merged"])

            if action_type == "closed" and pr["merged"]:
                action = "MERGE"
                print("🔥 MERGE detected")
            else:
                if action_type != "opened":
                    print("⚠️ Ignoring PR action:", action_type)
                    return {"status": "ignored"}, 200

                action = "PULL_REQUEST"

            request_id = f"{pr['id']}_{action}"

            if collection.find_one({"request_id": request_id}):
                print("⚠️ Duplicate PR/MERGE ignored")
                return {"status": "duplicate"}, 200

            doc = {
                "request_id": request_id,
                "author": author,
                "action": action,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": format_timestamp()
            }

            collection.insert_one(doc)
            print(f"✅ {action} stored")

        else:
            print("⚠️ Ignored event:", event)

        print("=====================================\n")
        return {"status": "ok"}, 200

    except Exception as e:
        print("❌ ERROR:", e)
        return {"error": str(e)}, 500


@app.route("/events", methods=["GET"])
def get_events():
    try:
        events = list(collection.find().sort("_id", -1).limit(20))

        for e in events:
            e["_id"] = str(e["_id"])

        print("✅ Returning events:", len(events))
        return jsonify(events)

    except Exception as e:
        print("❌ Error fetching events:", e)
        return jsonify([])


@app.route("/test")
def test():
    print("\nRunning TEST insert...")

    doc = {
        "request_id": "test_" + str(datetime.utcnow().timestamp()),
        "author": "test",
        "action": "PUSH",
        "from_branch": None,
        "to_branch": "main",
        "timestamp": format_timestamp()
    }

    result = collection.insert_one(doc)

    print("Inserted ID:", result.inserted_id)

    return f"Inserted {result.inserted_id}"


if __name__ == "__main__":
    print("🚀 Server running on http://localhost:5000")
    app.run(port=5000, debug=True)