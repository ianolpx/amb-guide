from handlers.provider import amb_provider
from web3 import Web3

if __name__ == '__main__':
    w3 = Web3(amb_provider)
    connection_valid = w3.is_connected()
    print(connection_valid)
