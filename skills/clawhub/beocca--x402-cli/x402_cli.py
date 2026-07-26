"""
Very basic CLI-tool to use x402-paywalled endpoints.

## x402 Payment Protocol

x402 is an HTTP-native payment protocol built on the `402 Payment Required` status code, enabling:
- **Direct on-chain transactions** without intermediaries
- **Stateless and programmatic** interactions between agents
- **Micropayments** with near-instant settlement
- **Machine-to-machine economy** where agents autonomously discover, request, and pay for services
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Any, Optional, Dict, Tuple
from datetime import datetime

import requests
from eth_account import Account
from x402 import x402ClientSync
from x402.http.clients import x402_requests
from x402.mechanisms.evm import EthAccountSigner
from x402.mechanisms.evm.exact.register import register_exact_evm_client

from dotenv import load_dotenv
load_dotenv()



def _create_new_evm_wallet(save_dir: Optional[str] = None) -> str:
    """ Create a new EVM wallet and save to json """

    # Create new evm wallet
    account = Account.create()
    wallet_data = {
        "time_created": datetime.now().strftime("%d/%m/%Y, %H:%M:%S.%s"),
        "type": "evm", 
        "address": account.address, 
        "key": account.key.hex(),
        "notes": "NEW_WALLET"
    }
    # Save wallet to json file
    save_dir = save_dir or str()
    save_path = os.path.join(save_dir, f"evm_{account.address}.json")
    with open(save_path, "w") as file:
        file.write(json.dumps(wallet_data, indent=4))
    os.chmod(save_path, 0o600)

    print(
        "\n[!] SECURITY WARNING\n"
        f"    Wallet file saved to: {save_path}\n"
        "    This file contains an UNENCRYPTED, spend-capable EVM private key stored in plaintext.\n"
        "    - Do NOT commit this file to version control.\n"
        "    - Do NOT back it up to cloud storage.\n"
        "    - File permissions have been set to 600 (owner read/write only).\n"
        "    - Use a dedicated low-balance wallet to limit exposure.\n",
        file=sys.stderr,
    )

    # Output
    return f"[+] EVM Wallet created successfully: {account.address} and saved to {save_path}."



def _list_x402_resources(limit: int = 50, offset: int = 0) -> str:
    """
    Lists x402 resources from the Coinbase CDP Bazaar.

    Returns:
        A JSON-formatted string of catalog resources.
    """
    base_url = "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources"

    params = {"limit": limit, "offset": offset}

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)

    except requests.RequestException as e:
        return f"Error listing services: {str(e)}"


def _search_x402_resources(query: str) -> str:
    """
    Searches x402 resources from the Coinbase CDP Bazaar.

    Args:
        query: A search string for semantic search.

    Returns:
        A JSON-formatted string of matching services.
    """
    base_url = "https://api.cdp.coinbase.com/platform/v2/x402/discovery/search"

    params = {"query": query}

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)

    except requests.RequestException as e:
        return f"Error searching services: {str(e)}"


def _init_x402_evm_client(evm_wallet_secret: Optional[str] = None) -> x402ClientSync:

    # Create the eth wallet for the agent to use
    evm_wallet_secret = os.getenv("CLIENT_EVM_WALLET_SECRET", evm_wallet_secret)
    assert evm_wallet_secret is not None, "evm_wallet_secret missing! Pass evm_wallet_secret or set env-variable CLIENT_EVM_WALLET_SECRET"
    evm_wallet = Account.from_key(evm_wallet_secret)

    # Init the x402 client
    x402_client = x402ClientSync()
    register_exact_evm_client(
        x402_client, 
        EthAccountSigner(evm_wallet),
        networks=[
            # Base
            "eip155:8453",      # -> base 
            "eip155:84532",     # -> base-sepolia
        ]
    )

    return x402_client


def _x402_request(
    x402_client: x402ClientSync,
    url: str,
    request_header: Optional[Dict[str, Any]] = None,
    request_type: str = "post",
    request_data: Optional[Dict[str, Any]] = None,
    timeout: int = 60,
) -> Tuple[int, Dict[str, Any]]:
    """
    Request an x402-paywalled endpoint

    Returns:
        (status_code, response_data) where response_data is a dict parsed from JSON if possible,
        otherwise {"raw": "..."}.
    """
    assert request_type.lower() in ["get", "post"]

    with x402_requests(x402_client) as session:

        header = request_header or dict()

        try:
            match request_type.lower():
                case "post":
                    service_response = session.post(url, headers=header, json=request_data, timeout=timeout)
                case "get":
                    service_response = session.get(url, headers=header, params=request_data, timeout=timeout)
                case _:
                    raise ValueError(f"Unknown request type: {request_type}")

            try:
                payload = service_response.json()
                if isinstance(payload, dict):
                    return service_response.status_code, payload
                return service_response.status_code, {"data": payload}
            except ValueError:
                return service_response.status_code, {"raw": service_response.text}

        except requests.RequestException as e:
            return 0, {"error": "request_failed", "details": str(e), "url": url}


def _parse_request_data(raw_request_data: Optional[str]) -> Optional[Dict[str, Any]]:
    if raw_request_data is None:
        return None

    try:
        parsed = json.loads(raw_request_data)
    except json.JSONDecodeError as exc:
        raise ValueError(f"request-data must be valid JSON: {exc.msg}") from exc

    if not isinstance(parsed, dict):
        raise ValueError("request-data must decode to a JSON object")

    return parsed


def _parse_request_header(raw_request_header: Optional[str]) -> Optional[Dict[str, Any]]:
    if raw_request_header is None:
        return None

    try:
        parsed = json.loads(raw_request_header)
    except json.JSONDecodeError as exc:
        raise ValueError(f"request-header must be valid JSON: {exc.msg}") from exc

    if not isinstance(parsed, dict):
        raise ValueError("request-header must decode to a JSON object")

    return parsed


def _print_response(response: Any) -> None:
    if isinstance(response, (dict, list)):
        print(json.dumps(response, indent=2, sort_keys=True))
        return

    print(response)


def _generate_discovery_filename(command_name: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"x402_{command_name}_{timestamp}.json"


def _save_discovery_output(output: Any, command_name: str, output_dir: Optional[str] = None) -> str:
    target_dir = Path(output_dir or ".")
    target_dir.mkdir(parents=True, exist_ok=True)
    output_path = target_dir / _generate_discovery_filename(command_name)

    with output_path.open("w", encoding="utf-8") as file:
        if isinstance(output, str):
            try:
                parsed_output = json.loads(output)
            except json.JSONDecodeError:
                file.write(output)
            else:
                json.dump(parsed_output, file, indent=2)
                file.write("\n")
        else:
            json.dump(output, file, indent=2)
            file.write("\n")

    return str(output_path)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI for x402 discovery and paywalled requests")
    subparsers = parser.add_subparsers(dest="command", required=True)

    discover_parser = subparsers.add_parser("discover", help="Discover x402 services")
    discover_subparsers = discover_parser.add_subparsers(dest="discover_command", required=True)

    list_parser = discover_subparsers.add_parser("list", help="List available x402 resources")
    list_parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Maximum number of resources to fetch",
    )
    list_parser.add_argument(
        "--offset",
        type=int,
        default=0,
        help="Starting offset for pagination",
    )
    list_parser.add_argument(
        "--save",
        action="store_true",
        help="Save the discovery response to a JSON file",
    )
    list_parser.add_argument(
        "--output-dir",
        "-o",
        default=None,
        help="Directory where the JSON file should be written",
    )

    search_parser = discover_subparsers.add_parser("search", help="Search x402 resources")
    search_parser.add_argument("query", help="Semantic search query")
    search_parser.add_argument(
        "--save",
        action="store_true",
        help="Save the discovery response to a JSON file",
    )
    search_parser.add_argument(
        "--output-dir",
        "-o",
        default=None,
        help="Directory where the JSON file should be written",
    )

    wallet_parser = subparsers.add_parser("wallet", help="Manage local EVM wallets")
    wallet_subparsers = wallet_parser.add_subparsers(dest="wallet_command", required=True)

    wallet_create_parser = wallet_subparsers.add_parser("create", help="Create a new EVM wallet")
    wallet_create_parser.add_argument(
        "--save-dir",
        default=None,
        help="Directory where the generated wallet JSON should be saved",
    )

    request_parser = subparsers.add_parser("request", help="Make an x402-paid request")
    request_parser.add_argument("url", help="Paywalled endpoint URL")
    request_parser.add_argument(
        "--method",
        choices=["get", "post"],
        default="post",
        help="HTTP method to use for the request",
    )
    request_parser.add_argument(
        "--data",
        default=None,
        help='Request payload as a JSON object string, for example \'{"foo":"bar"}\'',
    )
    request_parser.add_argument(
        "--header",
        default=None,
        help='Request headers as a JSON object string, for example \'{"Authorization":"Bearer ..."}\'',
    )
    request_parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="Request timeout in seconds",
    )
    request_parser.add_argument(
        "--evm-wallet-secret",
        default=None,
        help="Private key for the EVM wallet, or set CLIENT_EVM_WALLET_SECRET",
    )

    return parser



if __name__ == "__main__":
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "discover":
        if args.discover_command == "list":
            discovered = _list_x402_resources(limit=args.limit, offset=args.offset)
            if args.save:
                saved_path = _save_discovery_output(discovered, "discover_list", args.output_dir)
                print(f"saved_to: {saved_path}")
            _print_response(discovered)
            sys.exit(0)

        if args.discover_command == "search":
            discovered = _search_x402_resources(args.query)
            if args.save:
                saved_path = _save_discovery_output(discovered, "discover_search", args.output_dir)
                print(f"saved_to: {saved_path}")
            _print_response(discovered)
            sys.exit(0)

    if args.command == "wallet" and args.wallet_command == "create":
        created_wallet = _create_new_evm_wallet(save_dir=args.save_dir)
        _print_response(created_wallet)
        sys.exit(0)

    if args.command == "request":
        request_data = _parse_request_data(args.data)
        request_header = _parse_request_header(args.header)
        x402_client = _init_x402_evm_client(evm_wallet_secret=args.evm_wallet_secret)
        status_code, response = _x402_request(
            x402_client=x402_client,
            url=args.url,
            request_header=request_header,
            request_type=args.method,
            request_data=request_data,
            timeout=args.timeout,
        )

        print(f"status_code: {status_code}")
        _print_response(response)
        sys.exit(0)