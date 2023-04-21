# NFT Wallet CSV Exporter

This Python script exports all NFTs held by a particular wallet to a CSV file, including token addresses and IDs. It also generates a second CSV file containing the token addresses and their corresponding token names for reference.


## Prerequisites

Before you begin, make sure you have Python 3.6 or later installed on your system. You can check your Python version by running the following command in your terminal (Command Prompt on Windows, Terminal on macOS/Linux):

`python3 --version`

If you don't have Python installed or your version is older than 3.6, you can download the latest version from the official website: https://www.python.org/downloads/


## Installation

1. Clone this repository or download it as a ZIP file and extract it to a directory of your choice.

2. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and navigate to the directory where you have extracted the project files.

3. Install the required Python library, `requests`, by running the following command:

`python3 -m pip install requests`


## Configuration

1. In the project directory, you'll find a file named `config.example.ini`. Make a copy of this file and name it `config.ini`.

2. Open the `config.ini` file in a text editor and replace `your_wallet_address_here` with your own wallet address and `your_etherscan_api_key_here` with your own Etherscan API key.


## Usage

1. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and navigate to the directory where you have extracted the project files.

2. Run the Python script by executing the following command:

`python3 getlist.py`

3. Once the script has completed, you'll find two new CSV files in the project directory: `nfts.csv` and `token_reference.csv`. The `nfts.csv` file contains the exported NFT data, including token addresses and IDs, while the `token_reference.csv` file contains the token addresses and their corresponding token names for reference.


## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for details.
