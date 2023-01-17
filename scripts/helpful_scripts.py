from brownie import FundMe, MockV3Aggregator, network, config, accounts
from web3 import Web3

FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
decimals = 8
starting_price = 200000000000


def get_account():
    # .yaml works like a dictionary :)
    # account = accounts.add(config["wallets"]["from_key"]
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENT):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f"Deplyoing mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(decimals, starting_price, {
                                "from": get_account()})

    print("Mocks Deployed")
