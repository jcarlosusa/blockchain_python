# Import dependencies
import subprocess
import json
import bit
from dotenv import load_dotenv
from bit import wif_to_key
import os

# Load and set environment variables
load_dotenv("mnemo.env")
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from constants import *
 
# Create a function called `derive_wallets`
def derive_wallets(mnemonic, coin, numderive):
    command = './hd-wallet-derive -g --mnemonic="mnemonic" --coin="coin" --numderive="numderive" --cols=path,address,privkey,pubkey --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {
  "Path": "path",
  "Address": "address",
  "Priv_key": "privkey",
  "Pub_key": "pubkey"
}

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    coin = constants.py
    if coin = ETH 
    return Account.privateKeyToAccount(priv_key)
    if coin = BTCTEST
    return PrivateKeyTestnet(priv_key)
    
    
# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    if coin = ETH
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
        "chainID": web3.eth.chain_id,
    }
    if coin = BTCTEST
    return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, to, amount):
    tx = create_tx(coin, account, to, amount)
    if coin = ETH
        signed_tx = account.sign_transaction(tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(result.hex())
        return result.hex()
    if coin = BTCTEST 
        NetworkAPI.broadcast_tx_testnet(signed)
