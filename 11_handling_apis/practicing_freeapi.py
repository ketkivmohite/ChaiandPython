import requests

def fetch_user_id():
    url = 'https://api.freeapi.app/api/v1/todos'

    response = requests.get(url)

    data = response.json()

    print(data)

    if data["success"] and len(data["data"]) > 0:

        user_data = data["data"][0]

        user_id = user_data["_id"]
        title = user_data["title"]
        created_at = user_data["createdAt"]

        return user_id, title, created_at

    else:
        raise Exception("No todo data found")


def main():
    try:
        user_id, title, created_at = fetch_user_id()

        print(f"UserID: {user_id}")
        print(f"Title: {title}")
        print(f"Created At: {created_at}")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()