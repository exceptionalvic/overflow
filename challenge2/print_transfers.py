"""Take in transaction_hash as input and print receipt data."""
import json
import requests

apiKey = "input api key"


def is_hex(string):
    """Check if a string is a valid hexadecimal."""
    try:
        int(string, 16)
        return True
    except ValueError:
        return False


def print_transfers(api_key, transaction_hash):
    """Print transaction receipt log data using transaction hash.

    Extracts the amount, sender address, and receiver address."""
    # Define the Etherscan API endpoint URL
    etherscan_url = "https://api.etherscan.io/api"

    # Define the parameters for the API request
    params = {
        "module": "proxy",
        "action": "eth_getTransactionReceipt",
        "apikey": api_key,
        "txhash": transaction_hash,
    }

    # Make the API request
    response = requests.get(etherscan_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        print(json.dumps(response_data, indent=4))

        # Check if the response contains result log
        if "result" in response_data:
            # Extract the "logs" list from the result
            logs = response_data["result"]["logs"]

            # Parse and print the transfer information from the logs
            transfers = []
            for log in logs:
                try:
                    # Get the hexadecimal data as a string
                    data_hex = log["data"]

                    # Check if data_hex is a valid hexadecimal string
                    if is_hex(data_hex):
                        # Convert the hexadecimal data to an integer
                        amount = int(data_hex, 16)

                        # Append the transfer details
                        transfer = {
                            "from": log["topics"][1],
                            "to": log["topics"][2],
                            "amount": amount,
                        }
                        transfers.append(transfer)
                except Exception as e:
                    print(f"Error occurred. Detail: {str(e)}")
                    continue

            # Print transfers
            print(transfers)
        else:
            print("No logs found for the transaction.")
    else:
        print("Error: Unable to fetch data from Etherscan API.")


# Replace with your Etherscan API key and transaction hash
api_key = apiKey
# Input any transaction_hash
transaction_hash = (
    "0x3fbb21da357fdd74a12319ee423b4f30829030ba53b1d8d9e005c0da138e2263"
)

print_transfers(api_key, transaction_hash)
