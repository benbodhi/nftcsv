# NFT Wallet CSV Exporter

This Python script exports all NFTs held by a particular wallet to a CSV file, including token addresses and IDs. It also generates a second CSV file containing the token addresses and their corresponding token names for reference.

I made this for the purpose of exporting a list of all NFTs held by a Safe for easy use of the CSV Airdrop app.

## Prerequisites

Before you begin, make sure you have the following:

1. Python 3.6 or later installed on your system. You can check your Python version by running the following command in your terminal (Command Prompt on Windows, Terminal on macOS/Linux):

    `python3 --version`

    If you don't have Python installed or your version is older than 3.6, you can download the latest version from the official website: https://www.python.org/downloads/

2. An Etherscan account with an API key:

    a. Sign up for a free Etherscan account at https://etherscan.io/register.

    b. Once you have registered and logged in, navigate to the "API-KEYs" tab in your account settings, or visit https://etherscan.io/myapikey directly.

    c. Click on "Add" to create a new API key. You can give it a name to help you remember its purpose (e.g., "NFT Wallet CSV Exporter").

    d. Copy the generated API key and keep it handy, as you'll need to add it to the `config.ini` file later.

Now that you have Python installed and an Etherscan API key, you can proceed with the installation and configuration steps.

## Installation

1. Clone this repository or download it as a ZIP file and extract it to a directory of your choice.

2. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and navigate to the directory where you have extracted the project files.

3. Install the required Python libraries, `requests` and `tkinter`, by running the following command:

    `python3 -m pip install requests tkinter`

## Configuration

1. In the project directory, you'll find a file named `config.example.ini`. Make a copy of this file and name it `config.ini`.

2. Open the `config.ini` file in a text editor and update the following placeholders with your actual information: replace `your_wallet_address_here` with the wallet address you want to scan for NFTs, and `your_etherscan_api_key_here` with the Etherscan API key you obtained earlier. Make sure to save the changes to the `config.ini` file before proceeding.

## Usage

1. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and navigate to the directory where you have extracted the project files.

2. Run the Python script by executing the following command:

    `python3 getlist.py`

3. The script will prompt you to select a folder and file name to save the `nfts.csv` file. You can either choose a custom location and file name or press 'Cancel' to use the default Downloads folder and file name.

4. A second prompt will appear, allowing you to choose a folder and file name for the `token_reference.csv` file. It defaults to the folder chosen for the `nfts.csv` file. You can either choose a custom location and file name or press 'Cancel' to use the default folder and file name.

5. Once the script has completed, the NFT and Token Reference CSV files will be saved to the chosen locations. The terminal will display the file paths of the saved CSV files.

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for details.
