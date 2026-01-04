import os

import requests
from dotenv import load_dotenv


def main():
    print("Hello from holon!")

    load_dotenv()
    LICHESS_TOKEN = os.getenv("LICHESS_TOKEN")

    lichess = requests.get(
        "https://lichess.org/api/user/The_Skeleton",
        headers={"Authorization": f"Bearer {LICHESS_TOKEN}"},
        params={"trophies": "false", "profile": "true", "rank": "false"},
    )
    print(lichess)


    h = requests.get("https://api.chess.com/context/Player.jsonld")

    chesscom = requests.get("https://api.chess.com/pub/player/emersh0w", headers=h)
    print(chesscom)
    
    with open("chesscom.json", "w") as f:
        f.write(str(chesscom.json()))
        
    with open("lichess.json", "w") as f:
        f.write(str(lichess.json()))
        
    

if __name__ == "__main__":
    main()
