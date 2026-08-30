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
from x402 import x402Client, max_amount
from x402.http.clients import x402_requests
from x402.mechanisms.evm import EthAccountSigner
from x402.mechanisms.evm.exact.register import register_exact_evm_client

from dotenv import load_dotenv
load_dotenv()



DEFAULT_USDC_SPEND_LIMIT = 1
USDC_DECIMALS = 6



class ErrorCode:
    """Stable, machine-matchable error identifiers returned as ``error_code``."""

    INVALID_ARGUMENT = "invalid_argument"
    INVALID_JSON = "invalid_json"
    MISSING_ENV_VAR = "missing_env_var"
    NETWORK_ERROR = "network_error"
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


def _http_request(
    url: str,
    request_header: Optional[Dict[str, Any]] = None,
    request_type: str = "post",
    request_data: Optional[Dict[str, Any]] = None,
    timeout: int = 60,
) -> Tuple[int, Dict[str, Any]]:
    """
    Make a plain HTTP request without x402 signing.
    
    Used for dry-run/inspection to see what the server returns (typically 402 Payment Required).

    Returns:
        (status_code, response_data) where response_data is a dict parsed from JSON if possible,
        otherwise {"raw": "..."}.
    """
    if request_type.lower() not in ("get", "post"):
        raise CliError(f"Unsupported request method: {request_type}", ErrorCode.INVALID_ARGUMENT)

    header = request_header or dict()

    try:
        match request_type.lower():
            case "post":
                service_response = requests.post(url, headers=header, json=request_data, timeout=timeout)
            case "get":
                service_response = requests.get(url, headers=header, params=request_data, timeout=timeout)
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



def _init_x402_evm_client(usdc_spend_limit: float) -> x402Client:

    # Create the eth wallet for the agent to use
    evm_wallet_secret = os.getenv("CLIENT_EVM_WALLET_SECRET")
    if evm_wallet_secret is None:
        raise CliError(
            "CLIENT_EVM_WALLET_SECRET is not set; set it via a .env file or the shell environment.",
            ErrorCode.MISSING_ENV_VAR,
        )
    evm_wallet = Account.from_key(evm_wallet_secret)

    # Init the x402 client
    x402_client = x402Client().register_policy(max_amount(usdc_spend_limit * 10**USDC_DECIMALS))
    register_exact_evm_client(
        x402_client, 
        EthAccountSigner(evm_wallet),
        networks=[
            # Base
            "eip155:8453",      # -> base 
            # "eip155:84532",   # -> base-sepolia
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
    Request an x402-paywalled endpoint with automatic payment signing.

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


# Header names whose values are redacted before being written to disk. Matched
# case-insensitively; covers common auth/session/API-key header conventions.
_SENSITIVE_HEADER_NAMES = {
    "authorization",
    "cookie",
    "set-cookie",
    "proxy-authorization",
    "x-api-key",
    "api-key",
    "x-auth-token",
    "x-access-token",
    "x-session-token",
}


def _redact_sensitive_headers(headers: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Return a copy of ``headers`` with sensitive values replaced by ``"[REDACTED]"``.

    Only header *values* are redacted; header names are kept so the saved file still
    shows which headers were sent. Request/response bodies are not redacted here —
    use ``--no-save`` if a request body itself carries secrets.
    """
    if not headers:
        return headers
    return {
        key: ("[REDACTED]" if key.lower() in _SENSITIVE_HEADER_NAMES else value)
        for key, value in headers.items()
    }


def _warn_saving_to_disk(output_dir: Optional[str]) -> None:
    """Print a stderr notice that request/response contents will be persisted locally."""
    location = output_dir or "."
    print(
        "[!] SAVE WARNING: writing request headers, request data, and the response to a "
        f"JSON file in '{location}'. Common auth headers (Authorization, Cookie, API keys, "
        "etc.) are redacted, but the request body/data and the service response are stored "
        "as-is. Pass --no-save if either may contain secrets or sensitive data.",
        file=sys.stderr,
    )


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


def _save_request_output(
    command_name: str,
    request_header: Optional[Dict[str, Any]],
    request_data: Optional[Dict[str, Any]],
    response: Dict[str, Any],
    output_dir: Optional[str] = None,
) -> str:
    """Save a request/response pair to a timestamped JSON file.

    The file has the shape ``{"input": {"header": ..., "data": ...}, "response": ...}``,
    where ``response`` is either the successful ``{"status_code": ..., "data": ...}``
    payload or an ``{"error": ..., "error_code": ...}`` payload on failure.

    Sensitive header values (Authorization, Cookie, API keys, etc.) are redacted before
    writing; request data/body and the response are stored as-is.
    """
    _warn_saving_to_disk(output_dir)
    payload = {
        "input": {"header": _redact_sensitive_headers(request_header), "data": request_data},
        "response": response,
    }
    return _save_discovery_output(payload, command_name, output_dir)


def command_discover_list(args: argparse.Namespace) -> Dict[str, Any]:
    """
    List available x402 resources from the Coinbase CDP discovery catalog.
    
    Returns a paginated list of x402 services. Each resource in the response includes:
    - resource: The HTTPS endpoint URL for this service
    - description: Human-readable service description
    - accepts: Array of payment options (amount, network, token, etc.)
    - quality: Usage metrics (total calls, unique payers in last 30 days)
    - extensions.bazaar.info: Example input/output for this service
    
    Example output structure:
    {
        "ok": true,
        "action": "discover-list",
        "resources": {
            "items": [
                {
                    "resource": "https://api.example.com/service",
                    "description": "Service description",
                    "accepts": [
                        {
                            "scheme": "exact",
                            "network": "eip155:8453",
                            "asset": "0x...(token_address)",
                            "amount": "1000",
                            "payTo": "0x...(recipient_address)"
                        }
                    ],
                    "quality": {
                        "l30DaysTotalCalls": 1000,
                        "l30DaysUniquePayers": 625
                    }
                }
            ]
        }
    }
    
    Pagination:
    - Use --limit to control page size (default 50, max 100)
    - Use --offset to fetch additional pages (default 0)
    - When --save is set, the response is also written to a timestamped JSON file
    """
    resources = _list_x402_resources(limit=args.limit, offset=args.offset)
    result: Dict[str, Any] = {"ok": True, "action": "discover-list", "resources": resources}
    if args.save:
        result["saved_to"] = _save_discovery_output(resources, "discover_list", args.output_dir)
    return result


def command_discover_search(args: argparse.Namespace) -> Dict[str, Any]:
    """
    Semantically search for x402 resources matching a query string.
    
    Returns a list of matching services sorted by relevance. The search index includes:
    - service descriptions and names
    - tags (e.g., "weather", "crypto news", "blockchain data")
    - quality metrics
    
    Example output structure:
    {
        "ok": true,
        "action": "discover-search",
        "resources": {
            "meta": {
                "searchToken": "<search_token>"
            },
            "partialResults": false,
            "resources": [
                {
                    "resource": "https://api.example.com/service",
                    "serviceName": "Service Provider Name",
                    "description": "Service description",
                    "tags": ["tag1", "tag2", "tag3"],
                    "accepts": [
                        {
                            "scheme": "exact",
                            "network": "eip155:8453",
                            "asset": "0x...(token_address)",
                            "amount": "1000"
                        }
                    ],
                    "quality": {
                        "l30DaysTotalCalls": 1595,
                        "l30DaysUniquePayers": 116
                    }
                }
            ]
        }
    }
    
    Parsing guidance:
    - Extract .resources[].resource to get the URL for request info/pay
    - Check .resources[].accepts[0].amount to verify the cost
    - Use .resources[].description and .tags to understand the service
    - partialResults: true means the search timed out; results are incomplete
    """
    resources = _search_x402_resources(args.query)
    result: Dict[str, Any] = {"ok": True, "action": "discover-search", "resources": resources}
    if args.save:
        result["saved_to"] = _save_discovery_output(resources, "discover_search", args.output_dir)
    return result


def command_request_info(args: argparse.Namespace) -> Dict[str, Any]:
    """
    Inspect an x402 endpoint without payment to see what it requires.
    
    Makes a plain HTTP request and captures the response, typically a 402 Payment Required
    with payment instructions. Use this BEFORE calling request pay to verify:
    - The endpoint is reachable
    - The payment amount and recipient
    - The input/output format
    - Whether the service is working
    
    Does NOT require CLIENT_EVM_WALLET_SECRET (no payment is attempted).
    
    Example output structure (typical 402 response):
    {
        "ok": true,
        "action": "request-info",
        "status_code": 402,
        "data": {
            "payment_instruction": {
                "amount": "1000",
                "asset": "0x...(token_address)",
                "payTo": "0x...(recipient_address)",
                "scheme": "exact",
                "network": "eip155:8453"
            }
        }
    }
    
    Parsing guidance:
    - Check .status_code: 402 = payment required (expected), others = service error
    - Extract payment details to confirm amount before paying
    - HTTP 4xx/5xx errors from the destination are still .ok: true (they're valid responses)
    - Transport errors (DNS, timeout, connection refused) produce .ok: false

    Saving:
    - --save is opt-in (disabled by default); pass --save to enable it
    - When enabled, writes a JSON file shaped like
      {"input": {"header": ..., "data": ...}, "response": {...}}, where "response" is
      either {"status_code": ..., "data": ...} on success or {"error": ..., "error_code": ...}
      on failure
    - Sensitive header values (Authorization, Cookie, API keys, etc.) are redacted before
      writing; request data/body and the response are stored as-is
    """
    request_data = _parse_request_data(args.data)
    request_header = _parse_request_header(args.header)

    try:
        status_code, response = _http_request(
            url=args.url,
            request_header=request_header,
            request_type=args.method,
            request_data=request_data,
            timeout=args.timeout,
        )
    except CliError as error:
        if args.save:
            _save_request_output(
                "request_info",
                request_header,
                request_data,
                {"error": str(error), "error_code": error.error_code},
                args.output_dir,
            )
        raise

    result: Dict[str, Any] = {"ok": True, "action": "request-info", "status_code": status_code, "data": response}
    if args.save:
        result["saved_to"] = _save_request_output(
            "request_info",
            request_header,
            request_data,
            {"status_code": status_code, "data": response},
            args.output_dir,
        )
    return result


def command_request_pay(args: argparse.Namespace) -> Dict[str, Any]:
    """
    Make a signed x402 payment request to a paywalled endpoint.
    
    This command:
    1. Reads CLIENT_EVM_WALLET_SECRET from environment
    2. Creates an EVM wallet instance
    3. Initiates the x402 payment flow (signing, authorization)
    4. Sends the paywalled request
    5. Returns the service response
    
    WARNING: THIS SPENDS REAL MONEY ON BASE MAINNET IMMEDIATELY
    No confirmation prompt is shown — the payment is authorized the moment this runs.
    Always call request info first to verify the endpoint.
    
    Example output structure (successful payment + service response):
    {
        "ok": true,
        "action": "request-pay",
        "status_code": 200,
        "data": {...service response data...}
    }
    
    Example output structure (service error after payment):
    {
        "ok": true,
        "action": "request-pay",
        "status_code": 500,
        "data": {"raw": "...error message..."}
    }
    
    Example output structure (wallet funding error):
    {
        "ok": false,
        "error": "Insufficient balance in wallet for payment",
        "error_code": "network_error",
        "type": "PaymentError"
    }
    
    Parsing guidance:
    - .ok: true means the payment went through (even if status_code is 4xx/5xx from service)
    - Check .status_code: 200+ = service response received, 4xx/5xx = service error
    - .data contains either JSON response or {"raw": "..."} if response is not JSON
    - .ok: false means payment failed or network error; check .error_code
    - Critical error codes: missing_env_var, network_error, internal_error
    
    Wallet/Payment Requirements:
    - CLIENT_EVM_WALLET_SECRET must be set (read-only from environment)
    - Wallet must have sufficient USDC on Base mainnet
    - Network must be Base mainnet (eip155:8453) only

    Saving:
    - --save is opt-in (disabled by default); pass --save to enable it
    - When enabled, writes a JSON file shaped like
      {"input": {"header": ..., "data": ...}, "response": {...}}, where "response" is
      either {"status_code": ..., "data": ...} on success or {"error": ..., "error_code": ...}
      on failure
    - Sensitive header values (Authorization, Cookie, API keys, etc.) are redacted before
      writing; request data/body and the response are stored as-is
    """
    request_data = _parse_request_data(args.data)
    request_header = _parse_request_header(args.header)

    usdc_spend_limit = args.spend_limit

    try:
        x402_client = _init_x402_evm_client(usdc_spend_limit)

        print(
            "\n[!] PAID REQUEST WARNING\n"
            f"    Destination: {args.method.upper()} {args.url}\n"
            f"    Headers provided: {'yes' if request_header else 'no'}\n"
            f"    Data provided: {'yes' if request_data else 'no'}\n"
            "    This will transmit the request (including any headers/data above) to the\n"
            "    third-party endpoint shown and immediately authorize an on-chain payment\n"
            "    from your wallet. There is no further confirmation prompt — review the\n"
            "    destination and payload carefully before running this command.\n"
            "    To inspect what this endpoint requires before paying, first run with: request info\n",
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
    except CliError as error:
        if args.save:
            _save_request_output(
                "request_pay",
                request_header,
                request_data,
                {"error": str(error), "error_code": error.error_code},
                args.output_dir,
            )
        raise

    result: Dict[str, Any] = {"ok": True, "action": "request-pay", "status_code": status_code, "data": response}
    if args.save:
        result["saved_to"] = _save_request_output(
            "request_pay",
            request_header,
            request_data,
            {"status_code": status_code, "data": response},
            args.output_dir,
        )
    return result


def _build_parser() -> argparse.ArgumentParser:
    parser = AgentArgumentParser(
        description="CLI for x402 discovery and paywalled requests",
        epilog=(
            "Related skills:\n"
            "  create-crypto-wallets  Generate and manage crypto wallets securely\n"
            "                         Install: openclaw skills install @beocca/create-crypto-wallets\n"
            "  keepass-cli            Manage secrets and credentials securely in encrypted vaults\n"
            "                         Install: openclaw skills install @beocca/keepass-cli\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
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

    request_parser = subparsers.add_parser("request", help="Make requests to x402 endpoints")
    request_subparsers = request_parser.add_subparsers(
        dest="request_command", required=True, parser_class=AgentArgumentParser
    )

    # request info: inspect server response without payment
    info_parser = request_subparsers.add_parser(
        "info", help="Inspect server response (likely 402 Payment Required) without sending payment"
    )
    info_parser.add_argument("url", help="Endpoint URL to inspect")
    info_parser.add_argument(
        "--method",
        choices=["get", "post"],
        default="post",
        help="HTTP method to use for the request",
    )
    info_parser.add_argument(
        "--data",
        default=None,
        help='Request payload as a JSON object string, for example \'{"foo":"bar"}\'',
    )
    info_parser.add_argument(
        "--header",
        default=None,
        help='Request headers as a JSON object string, for example \'{"Authorization":"Bearer ..."}\'',
    )
    info_parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="Request timeout in seconds",
    )
    info_parser.add_argument(
        "--save",
        dest="save",
        action="store_true",
        default=False,
        help="Save the request input and response to a JSON file (default: disabled)",
    )
    info_parser.add_argument(
        "--no-save",
        dest="save",
        action="store_false",
        help="Explicitly disable saving (default already disabled; kept for backward compatibility)",
    )
    info_parser.add_argument(
        "--output-dir",
        "-o",
        default=None,
        help="Directory where the JSON file should be written",
    )
    info_parser.set_defaults(handler=command_request_info)

    # request pay: make signed x402 payment
    pay_parser = request_subparsers.add_parser(
        "pay", help="Make a signed x402 payment request (immediately moves funds)"
    )
    pay_parser.add_argument("url", help="Paywalled endpoint URL")
    pay_parser.add_argument(
        "--method",
        choices=["get", "post"],
        default="post",
        help="HTTP method to use for the request",
    )
    pay_parser.add_argument(
        "--data",
        default=None,
        help='Request payload as a JSON object string, for example \'{"foo":"bar"}\'',
    )
    pay_parser.add_argument(
        "--header",
        default=None,
        help='Request headers as a JSON object string, for example \'{"Authorization":"Bearer ..."}\'',
    )
    pay_parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="Request timeout in seconds",
    )
    pay_parser.add_argument(
        "--spend-limit",
        type=float,
        default=DEFAULT_USDC_SPEND_LIMIT,
        help="Maximum USDC to authorize for this payment request",
    )
    pay_parser.add_argument(
        "--save",
        dest="save",
        action="store_true",
        default=False,
        help="Save the request input and response to a JSON file (default: disabled)",
    )
    pay_parser.add_argument(
        "--no-save",
        dest="save",
        action="store_false",
        help="Explicitly disable saving (default already disabled; kept for backward compatibility)",
    )
    pay_parser.add_argument(
        "--output-dir",
        "-o",
        default=None,
        help="Directory where the JSON file should be written",
    )
    pay_parser.set_defaults(handler=command_request_pay)

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
