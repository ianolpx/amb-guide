from web3.types import RPCEndpoint, RPCResponse
from web3.providers.async_rpc import AsyncHTTPProvider
from requests_auth_aws_sigv4 import AWSSigV4
from eth_typing import URI
from settings import settings
from web3 import Web3
from typing import Any
import requests_async as requests


class AsyncAMBHTTPProvider(AsyncHTTPProvider):

    def __init__(self, endpoint_uri: URI) -> None:
        self.aws_auth = AWSSigV4(
            'managedblockchain',
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region=settings.aws_region
        )
        super().__init__(endpoint_uri)

    async def make_request(
        self,
        method: RPCEndpoint,
        params: Any
    ) -> RPCResponse:
        request_data = self.encode_rpc_request(method, params).decode()
        raw_response = await self.make_custom_post_request(
            self.endpoint_uri,
            request_data,
            **self.get_request_kwargs()
        )
        response = self.decode_rpc_response(raw_response)
        return response

    def get_request_kwargs(self) -> dict:
        return {
            "headers": {
                "Content-Type": "application/json",
                "X-Amz-Target": "ManagedBlockchain_v2018_09_24.CreateMember",
            }
        }

    async def make_custom_post_request(
        self,
        endpoint_uri: URI,
        data: bytes,
        *args: Any,
        **kwargs: Any
    ) -> bytes:
        kwargs.setdefault('timeout', 10)
        # session = await requests.Session()
        response = await requests.post(endpoint_uri, data=data,
                                       *args, **kwargs, auth=self.aws_auth)
        await response.raise_for_status()
        return response.content


amb_provider = AsyncAMBHTTPProvider(settings.endpoint_url)


async def main():
    provider = AsyncAMBHTTPProvider(settings.endpoint_url)
    w3 = Web3(provider)
    connection_valid = await w3.is_connected()
    print(connection_valid)

    encode_test = w3.is_encodable('uint256', 1)
    print(encode_test)

    block_number = w3.eth.block_number
    print(block_number)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
