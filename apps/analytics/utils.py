import json
from config.settings.base import BASE_DIR


def read_json_data():
    post_file_path = BASE_DIR / "data/post.json"
    with open(post_file_path, "r", encoding="utf8") as file:
        data = json.load(file)
    return data


def generate_count_analytics():
    data = read_json_data()
    analytics = {
        "facebook": {"likes": 0, "reach": 0, "posts": 0},
        "instagram": {"likes": 0, "reach": 0, "posts": 0},
        "twitter": {"likes": 0, "reach": 0, "posts": 0},
    }

    for post in data.get("posts", []):
        if post["platform"] in analytics:
            analytics[post["platform"]]["likes"] += post.get("likes", 0)
            analytics[post["platform"]]["reach"] += post.get("reach", 0)
            analytics[post["platform"]]["posts"] += 1 
    
    return analytics
