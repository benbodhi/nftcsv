import requests
import csv
import configparser
import os
from tkinter import Tk, filedialog

def get_save_directory(default_filename, initial_dir=None):
    print(f"Select a folder and file name to save the {default_filename} file or press 'Cancel' to use the default Downloads folder and file name.")

    root = Tk()
    root.withdraw()
    root.update()

    if initial_dir is None:
        initial_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    save_path = filedialog.asksaveasfilename(initialdir=initial_dir, initialfile=default_filename, title=f"Choose a location to save the {default_filename} file")
    root.destroy()

    if not save_path:
        save_path = os.path.join(initial_dir, default_filename)

    return save_path

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

    nft_csv_save_path = get_save_directory("nfts.csv")
    token_reference_csv_save_path = get_save_directory("token_reference.csv", initial_dir=os.path.dirname(nft_csv_save_path))

    nfts = fetch_nfts(wallet_address, api_key)
    write_nfts_to_csv(nfts, nft_csv_save_path)
    write_token_reference_to_csv(nfts, token_reference_csv_save_path)

    print(f"NFT CSV file saved to: {nft_csv_save_path}")
    print(f"Token Reference CSV file saved to: {token_reference_csv_save_path}")