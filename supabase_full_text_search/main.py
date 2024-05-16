import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_ANON_KEY", "")
client = create_client(url, key)


def main():
    res = (
        client.table("movies")
        .select("*")
        .text_search("title", "'The Avenger'|'Mean'")
        .execute()
    )
    print(res.data)


if __name__ == "__main__":
    main()
