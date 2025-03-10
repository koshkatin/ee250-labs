import requests
import json

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            #print(f"{joke_data['setup']} - {joke_data['punchline']}")
            print("\nHere's a random joke for you! \n")
            print(f"{joke_data['setup']}")
            print(f"{joke_data['punchline']}\n")
            print("Have a great day!\n-Faith and Tina")
        else:
            print(f"Error: Unable to fetch joke. Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    get_random_joke()
