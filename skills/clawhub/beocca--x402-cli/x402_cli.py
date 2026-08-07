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


class ErrorCode:
    """Stable, machine-matchable error identifiers returned as ``error_code``."""

    INVALID_ARGUMENT = "invalid_argument"
    INVALID_JSON = "invalid_json"
    MISSING_ENV_VAR = "missing_env_var"
    NETWORK_ERROR = "network_error"
    HTTP_ERROR = "http_error"
    WALLET_EXISTS = "wallet_exists"
    FILE_NOT_FOUND = "file_not_found"
    INTERNAL_ERROR = "internal_error"


class CliError(Exception):
    """An expected command-line error that can be returned as JSON."""

    def __init__(self, message: str, error_code: str = ErrorCode.INVALID_ARGUMENT) -> None:
        super().__init__(message)
        self.error_code = error_code


class AgentArgumentParser(argparse.ArgumentParser):
    """An ArgumentParser that reports failures as ``CliError`` instead of
    printing usage text and calling ``sys.exit`` directly, so agents always
    receive a single JSON error object rather than plain-text usage output."""

    def error(self, message: str) -> None:  # type: ignore[override]
        raise CliError(message, ErrorCode.INVALID_ARGUMENT)


def emit(payload: Dict[str, Any], status: int = 0) -> int:
    """Write one JSON result and return its intended process status."""
    print(json.dumps(payload, sort_keys=True))
    return status


def emit_error(error: CliError, status: int, type_name: Optional[str] = None) -> int:
    payload: Dict[str, Any] = {
        "ok": False,
        "error": str(error),
        "error_code": error.error_code,
    }
    if type_name is not None:
        payload["type"] = type_name
    return emit(payload, status)


def _create_new_evm_wallet(save_dir: Optional[str] = None) -> Dict[str, Any]:
    """ Create a new EVM wallet and save to json """

    # Create new evm wallet
    account = Account.create()
    time_created = datetime.now().isoformat()
    wallet_data = {
        "time_created": time_created,
        "type": "evm",
        "address": account.address,
        "key": account.key.hex(),
        "notes": "NEW_WALLET"
    }
    # Save wallet to json file
    save_dir = save_dir or str()
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"evm_{account.address}.json")
    if os.path.exists(save_path):
        raise CliError(f"Wallet file already exists: {save_path}", ErrorCode.WALLET_EXISTS)
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

    # Output (never includes the private key)
    return {
        "address": account.address,
        "path": save_path,
        "time_created": time_created,
    }



def _list_x402_resources(limit: int = 50, offset: int = 0) -> Any:
    """
    Lists x402 resources from the Coinbase CDP Bazaar.

    Returns:
        The parsed JSON catalog response (dict or list).
    """
    base_url = "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources"

    params = {"limit": limit, "offset": offset}

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        raise CliError(f"Error listing services: {e}", ErrorCode.NETWORK_ERROR) from e


def _search_x402_resources(query: str) -> Any:
    """
    Searches x402 resources from the Coinbase CDP Bazaar.

    Args:
        query: A search string for semantic search.

    Returns:
        The parsed JSON search response (dict or list).
    """
    base_url = "https://api.cdp.coinbase.com/platform/v2/x402/discovery/search"

    params = {"query": query}

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        raise CliError(f"Error searching services: {e}", ErrorCode.NETWORK_ERROR) from e


def _init_x402_evm_client() -> x402ClientSync:

    # Create the eth wallet for the agent to use
    evm_wallet_secret = os.getenv("CLIENT_EVM_WALLET_SECRET")
    if evm_wallet_secret is None:
        raise CliError(
            "CLIENT_EVM_WALLET_SECRET is not set; set it via a .env file or the shell environment.",
            ErrorCode.MISSING_ENV_VAR,
        )
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
    if request_type.lower() not in ("get", "post"):
        raise CliError(f"Unsupported request method: {request_type}", ErrorCode.INVALID_ARGUMENT)

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
            raise CliError(f"Request to {url} failed: {e}", ErrorCode.NETWORK_ERROR) from e


def _parse_request_data(raw_request_data: Optional[str]) -> Optional[Dict[str, Any]]:
    if raw_request_data is None:
        return None

    try:
        parsed = json.loads(raw_request_data)
    except json.JSONDecodeError as exc:
        raise CliError(f"request-data must be valid JSON: {exc.msg}", ErrorCode.INVALID_JSON) from exc

    if not isinstance(parsed, dict):
        raise CliError("request-data must decode to a JSON object", ErrorCode.INVALID_JSON)

    return parsed


def _parse_request_header(raw_request_header: Optional[str]) -> Optional[Dict[str, Any]]:
    if raw_request_header is None:
        return None

    try:
        parsed = json.loads(raw_request_header)
    except json.JSONDecodeError as exc:
        raise CliError(f"request-header must be valid JSON: {exc.msg}", ErrorCode.INVALID_JSON) from exc

    if not isinstance(parsed, dict):
        raise CliError("request-header must decode to a JSON object", ErrorCode.INVALID_JSON)

    return parsed


def _generate_discovery_filename(command_name: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"x402_{command_name}_{timestamp}.json"


def _save_discovery_output(output: Any, command_name: str, output_dir: Optional[str] = None) -> str:
    target_dir = Path(output_dir or ".")
    target_dir.mkdir(parents=True, exist_ok=True)
    output_path = target_dir / _generate_discovery_filename(command_name)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(output, file, indent=2)
        file.write("\n")

    return str(output_path)


def command_discover_list(args: argparse.Namespace) -> Dict[str, Any]:
    resources = _list_x402_resources(limit=args.limit, offset=args.offset)
    result: Dict[str, Any] = {"ok": True, "action": "discover-list", "resources": resources}
    if args.save:
        result["saved_to"] = _save_discovery_output(resources, "discover_list", args.output_dir)
    return result


def command_discover_search(args: argparse.Namespace) -> Dict[str, Any]:
    resources = _search_x402_resources(args.query)
    result: Dict[str, Any] = {"ok": True, "action": "discover-search", "resources": resources}
    if args.save:
        result["saved_to"] = _save_discovery_output(resources, "discover_search", args.output_dir)
    return result


def command_wallet_create(args: argparse.Namespace) -> Dict[str, Any]:
    wallet = _create_new_evm_wallet(save_dir=args.save_dir)
    return {"ok": True, "action": "wallet-create", "wallet": wallet}


def command_request(args: argparse.Namespace) -> Dict[str, Any]:
    request_data = _parse_request_data(args.data)
    request_header = _parse_request_header(args.header)
    x402_client = _init_x402_evm_client()

    print(
        "\n[!] PAID REQUEST WARNING\n"
        f"    Destination: {args.method.upper()} {args.url}\n"
        f"    Headers provided: {'yes' if request_header else 'no'}\n"
        f"    Data provided: {'yes' if request_data else 'no'}\n"
        "    This will transmit the request (including any headers/data above) to the\n"
        "    third-party endpoint shown and immediately authorize an on-chain payment\n"
        "    from your wallet. There is no further confirmation prompt — review the\n"
        "    destination and payload carefully before running this command.\n",
        file=sys.stderr,
    )

    status_code, response = _x402_request(
        x402_client=x402_client,
        url=args.url,
        request_header=request_header,
        request_type=args.method,
        request_data=request_data,
        timeout=args.timeout,
    )

    return {"ok": True, "action": "request", "status_code": status_code, "data": response}


def _build_parser() -> argparse.ArgumentParser:
    parser = AgentArgumentParser(description="CLI for x402 discovery and paywalled requests")
    subparsers = parser.add_subparsers(dest="command", required=True, parser_class=AgentArgumentParser)

    discover_parser = subparsers.add_parser("discover", help="Discover x402 services")
    discover_subparsers = discover_parser.add_subparsers(
        dest="discover_command", required=True, parser_class=AgentArgumentParser
    )

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
    list_parser.set_defaults(handler=command_discover_list)

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
    search_parser.set_defaults(handler=command_discover_search)

    wallet_parser = subparsers.add_parser("wallet", help="Manage local EVM wallets")
    wallet_subparsers = wallet_parser.add_subparsers(
        dest="wallet_command", required=True, parser_class=AgentArgumentParser
    )

    wallet_create_parser = wallet_subparsers.add_parser("create", help="Create a new EVM wallet")
    wallet_create_parser.add_argument(
        "--save-dir",
        default=None,
        help="Directory where the generated wallet JSON should be saved",
    )
    wallet_create_parser.set_defaults(handler=command_wallet_create)

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
    request_parser.set_defaults(handler=command_request)

    return parser


def main(argv: Optional[list] = None) -> int:
    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except CliError as error:
        return emit_error(error, 2)

    try:
        return emit(args.handler(args))
    except CliError as error:
        return emit_error(error, 2)
    except Exception as error:  # noqa: BLE001 - convert any unexpected failure to structured JSON
        return emit(
            {
                "ok": False,
                "error": str(error),
                "error_code": ErrorCode.INTERNAL_ERROR,
                "type": type(error).__name__,
            },
            1,
        )


if __name__ == "__main__":
    sys.exit(main())