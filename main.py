from web3 import Web3
import json
import hashlib

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"  # change if needed
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]

# Contract ABI (paste your actual ABI string here)
abi = [...]  # Replace with your contract's ABI as a Python list

# Contract address from Remix deployment
contract_address = '0xYourContractAddressHere'  # replace with actual address
contract = web3.eth.contract(address=contract_address, abi=abi)

# Proof-of-Work simulation
def mine(message, difficulty_prefix='00000'):
    nonce = 0
    while True:
        guess = f'{message}{nonce}'.encode()
        guess_hash = hashlib.sha3_256(guess).hexdigest()
        if guess_hash.startswith(difficulty_prefix):
            print(f"Valid PoW found: nonce={nonce}, hash={guess_hash}")
            return nonce
        nonce += 1

# Message to be hashed
message = "Ganache POW test"
nonce = mine(message)

# Submit mined work to smart contract
tx_hash = contract.functions.submitWork(message, nonce).transact()
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print("Transaction complete. Block number:", receipt.blockNumber)
