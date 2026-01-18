import sys
import requests

if float(sys.argv[1]) < 0:
    print("Command-line is not a positive or zero number")
    sys.exit()

elif len(sys.argv) >= 1:

    try:
        bit = float(sys.argv[1])
        resp = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=cde705e50a827c5a1b42230c1bc21559187f7ac7c13b456b8efcdcf6fcdbdb9b')
        o = resp.json()

        usd = float(o["data"]["priceUsd"])
        final_usd = usd * bit
        print(f"${final_usd:,.4f}")

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()

    except requests.RequestException:
        print("Invalid input.")
        sys.exit()
