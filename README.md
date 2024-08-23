# amb-guide
amb-guide is a guide to using the AWS Managed Blockchain service. It is a work in progress.

The guide is written in Python and uses the web3.py library to interact with the AWS Managed Blockchain service.

More information is located in [Wiki](https://github.com/ianolpx/amb-guide/wiki)

### Setting up the environment
make .env file with the following variables:

```
AWS_ACCESS_KEY_ID=[your_aws_access_key_id]
AWS_SECRET_ACCESS_KEY=[your_aws_secret_access_key]
AWS_REGION=[your_aws_region]
ENDPOINT_URL=[your_endpoint_url]
```

### Installation
Clone the repository and install the requirements:

```bash
git clone https://github.com/ianolpx/amb-guide.git

cd amb-guide

pip install -r requirements.txt

```

### Usage
```python
from handlers.provider import amb_provider
from web3 import Web3

if __name__ == '__main__':
    w3 = Web3(amb_provider)
    connection_valid = w3.is_connected()
    print(connection_valid)

```

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License
[MIT](https://choosealicense.com/licenses/mit/)



