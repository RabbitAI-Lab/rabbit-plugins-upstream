#!/usr/bin/env python3
"""Read Agent World's fixed public health endpoint, without credentials or redirects."""
from __future__ import annotations

import json
import math
import ssl
import sys
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, HTTPSHandler, ProxyHandler, Request, build_opener

URL = "https://agentworldhub.com/api/v1/health"
MAX_BYTES = 16_384


class InvalidPublicStatus(ValueError):
    pass


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def _unique_pairs(pairs):
    value = {}
    for key, entry in pairs:
        if key in value:
            raise InvalidPublicStatus("Duplicate JSON member")
        value[key] = entry
    return value


def _reject_json_constant(value):
    raise InvalidPublicStatus("Non-finite JSON number")


def _finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        raise InvalidPublicStatus("Non-finite JSON number")
    return number


def validate_status(raw: bytes) -> dict:
    if not isinstance(raw, bytes) or len(raw) > MAX_BYTES:
        raise InvalidPublicStatus("Health response exceeds limit")
    try:
        data = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_pairs,
                          parse_constant=_reject_json_constant,
                          parse_float=_finite_float)
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise InvalidPublicStatus("Invalid health JSON") from exc
    if not isinstance(data, dict):
        raise InvalidPublicStatus("Health JSON is not an object")
    if data.get("status") not in ("read_only", "active", "ok"):
        raise InvalidPublicStatus("Unexpected health status")
    required_bools = (
        "real_original_market_data", "public_agent_registration_open",
        "public_agent_write_API_online", "one_original_ledger"
    )
    for field in required_bools:
        if type(data.get(field)) is not bool:
            raise InvalidPublicStatus(f"Invalid health flag: {field}")
    if data["one_original_ledger"] is not True:
        raise InvalidPublicStatus("One-ledger invariant not confirmed")
    # Never present a mere public HTTP status as a trading authorization.
    available_for_registration = data["public_agent_registration_open"] is True
    return {
        "source": URL,
        "health_status": data["status"],
        "original_market_data": data["real_original_market_data"],
        "single_ledger_reported": True,
        "registration_advertised_open": available_for_registration,
        "write_api_online": data["public_agent_write_API_online"],
        "public_trading_authorized_by_this_check": False,
        "next_step": (
            "Public agent registration is advertised open; an independent agent must still complete its own signed onboarding. Health does not authorize trading."
            if available_for_registration
            else "Public agent registration is advertised closed; do not attempt to enroll from this health response."
        ),
    }


def get_public_status(opener=None) -> dict:
    if opener is None:
        opener = build_opener(ProxyHandler({}), HTTPSHandler(context=ssl.create_default_context()), NoRedirect())
    request = Request(URL, headers={"Accept": "application/json", "User-Agent": "AgentWorldDiscovery/1.0.2"}, method="GET")
    try:
        with opener.open(request, timeout=8) as response:
            if response.status != 200 or response.geturl() != URL:
                raise InvalidPublicStatus("Unexpected response status or origin")
            media_type = response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
            if media_type != "application/json":
                raise InvalidPublicStatus("Unexpected non-JSON media type")
            raw = response.read(MAX_BYTES + 1)
    except (OSError, HTTPError, URLError, TimeoutError, ValueError) as exc:
        raise InvalidPublicStatus("Public endpoint not verified") from exc
    return validate_status(raw)


def main() -> int:
    try:
        result = get_public_status()
    except InvalidPublicStatus as exc:
        print(json.dumps({"status": "unavailable", "reason": str(exc), "registration_verified_open": False}), file=sys.stdout)
        return 2
    print(json.dumps(result, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
