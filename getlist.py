import requests
import csv
import configparser
import os
from tkinter import Tk, filedialog

def get_save_directory():
    print("Select a folder to save the CSV files or press 'Cancel' to use the default Downloads folder.")

    Tk().withdraw()
    save_directory = filedialog.askdirectory()

    if not save_directory:
        save_directory = os.path.join(os.path.expanduser("~"), "Downloads")

    return save_directory

ETHERSCAN_API_URL = "https://api.etherscan.io/api"

def fetch_nfts(wallet_address, api_key):
    url = f"{ETHERSCAN_API_URL}?module=account&action=tokennfttx&address={wallet_address}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["result"]
    else:
        raise ValueError(f"Error fetching NFTs: {response.status_code}, {response.text}")

def write_nfts_to_csv(nfts, file_name):
    with open(file_name, mode="w", newline="") as csvfile:
        fieldnames = ["token_type", "token_address", "receiver", "amount", "id"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for nft in nfts:
            writer.writerow({
                "token_type": "nft",
                "token_address": nft["contractAddress"],
                "receiver": "",
                "amount": "",
                "id": nft["tokenID"]
            })

def write_token_reference_to_csv(nfts, file_name):
    unique_tokens = {}
    for nft in nfts:
        token_address = nft["contractAddress"]
        if token_address not in unique_tokens:
            unique_tokens[token_address] = nft["tokenName"]

    with open(file_name, mode="w", newline="") as csvfile:
        fieldnames = ["token_address", "token_name"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for token_address, token_name in unique_tokens.items():
            writer.writerow({"token_address": token_address, "token_name": token_name})

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")
    wallet_address = config.get("DEFAULT", "wallet_address")
    api_key = config.get("DEFAULT", "etherscan_api_key")

    save_directory = get_save_directory()

    nfts = fetch_nfts(wallet_address, api_key)
    write_nfts_to_csv(nfts, os.path.join(save_directory, "nfts.csv"))
    write_token_reference_to_csv(nfts, os.path.join(save_directory, "token_reference.csv"))

    print(f"CSV files saved to: {save_directory}")