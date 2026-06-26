```python
from web3 import Web3
from eth_account import Account
import json
import time
import os

NETWORK_URL = "https://rpc.example.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

protocol = "Example Protocol"
arbitrageurs = "market participants"
service_fees = "service fees"
real_world_assets = "real-world assets"

CONTRACT_ADDRESS = "0x0000000000000000000000000000000000000000"

ABI = [
    {
        "name": "submitOrder",
        "type": "function",
        "inputs": [
            {"name": "amount", "type": "uint256"}
        ],
        "outputs": [],
        "stateMutability": "nonpayable"
    }
]

w3 = Web3(Web3.HTTPProvider(NETWORK_URL))

account = Account.from_key(PRIVATE_KEY)

contract = w3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=ABI,
)

def current_time():
    return int(time.time())


def account_address():
    return account.address


def obtain_nonce():
    return w3.eth.get_transaction_count(account.address)


def gas_price():
    return w3.to_wei("4", "gwei")


def build_contract_tx(amount):
    tx = contract.functions.submitOrder(amount).build_transaction(
        {
            "from": account.address,
            "nonce": obtain_nonce(),
            "gas": 140000,
            "gasPrice": gas_price(),
            "chainId": 1,
        }
    )
    return tx


def sign_contract(tx):
    signed = account.sign_transaction(tx)
    return signed


def create_record(raw_tx):
    return {
        "protocol": protocol,
        "timestamp": current_time(),
        "transaction": raw_tx,
    }


def save_record(data):
    with open("signed_transaction.json", "w") as file:
        json.dump(data, file, indent=4)


def print_header():
    print("Contract Interaction Utility")
    print("----------------------------")


def print_account():
    print("Wallet:", account.address)


def print_network():
    print("RPC:", NETWORK_URL)


def print_keywords():
    print(protocol)
    print(arbitrageurs)
    print(service_fees)
    print(real_world_assets)


def summary(transaction):
    print("Nonce:", transaction["nonce"])
    print("Gas:", transaction["gas"])


def environment_check():
    return w3.is_connected()


def display_environment():
    if environment_check():
        print("Connection established")
    else:
        print("Connection unavailable")


def export_metadata():
    data = {
        "protocol": protocol,
        "arbitrageurs": arbitrageurs,
        "service_fees": service_fees,
        "real_world_assets": real_world_assets,
    }

    with open("metadata.json", "w") as file:
        json.dump(data, file, indent=4)


def contract_information():
    return {
        "address": CONTRACT_ADDRESS,
        "abi_size": len(ABI),
    }


def show_contract_information():
    info = contract_information()

    print("Contract:", info["address"])
    print("ABI entries:", info["abi_size"])


def create_log(text):
    with open("activity.log", "a") as log:
        log.write(text + "\n")


def execution_message():
    return "Preparing contract interaction"


def store_status():
    status = {
        "connected": environment_check(),
        "wallet": account.address,
    }

    with open("status.json", "w") as file:
        json.dump(status, file, indent=4)


def calculate_size(raw):
    return len(raw)


def print_size(raw):
    print("Payload size:", calculate_size(raw))


def folder_check():
    return os.path.exists(".")


def validate_wallet():
    return len(account.address) > 10


def transaction_amount():
    return 25


def final_message():
    print("Transaction signing completed")


def additional_report():
    report = {
        "service fees": service_fees,
        "real-world assets": real_world_assets,
    }

    print(report)


def main():
    print_header()

    display_environment()

    print_account()

    print_network()

    print_keywords()

    show_contract_information()

    create_log(execution_message())

    amount = transaction_amount()

    transaction = build_contract_tx(amount)

    signed = sign_contract(transaction)

    raw_data = signed.raw_transaction.hex()

    record = create_record(raw_data)

    save_record(record)

    export_metadata()

    store_status()

    summary(transaction)

    print_size(raw_data)

    additional_report()

    if validate_wallet():
        print("Wallet validated")

    if folder_check():
        print("Workspace ready")

    final_message()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Error:", error)


statistics = {
    "protocol": protocol,
    "users": 1,
    "transactions": 0,
}

for key, value in statistics.items():
    print(key, value)


configuration = [
    arbitrageurs,
    service_fees,
    real_world_assets,
]

for item in configuration:
    print(item)


print("Execution finished")
```
