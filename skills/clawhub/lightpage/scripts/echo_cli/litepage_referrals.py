"""Origin-scoped referral handoff saved before credentials exist; Python 3.6 compatible."""

import json
import re

from echo_cli.compat import subparsers
from echo_cli.credentials import atomic_json, digest


def path(api):
    return api.store.path.parent / ("referral-" + digest(api.server) + ".json")


def load(api):
    target = path(api)
    if not target.exists():
        return None
    if target.is_symlink() or target.stat().st_mode & 0o077 or target.stat().st_size > 8192:
        raise RuntimeError("Referral source must be a bounded private file, not a symlink")
    value = json.loads(target.read_text())
    if value.get("server") != api.server:
        raise RuntimeError("Referral source belongs to another server")
    return value


def pending(api):
    with api.store.lock():
        value = load(api)
        return value["receipt"] if value and value.get("status") == "pending" else None


def acknowledge(api, receipt, status):
    with api.store.lock():
        value = load(api)
        if value and value.get("receipt") == receipt:
            value["status"] = status
            atomic_json(path(api), value)


def commands(root):
    referral = root.add_parser("referral", help="Save install source or manage promotion")
    actions = subparsers(referral, dest="referral_command")
    source = actions.add_parser(
        "source", help="Save a referral handoff locally; no network or login"
    )
    source.add_argument("receipt")
    actions.add_parser("status", help="Read local referral handoff status without credentials")
    link = actions.add_parser("link", help="Get your stable platform or work promotion link")
    link.add_argument("--site-id")
    link.add_argument("--parent-code")
    configure = actions.add_parser("configure", help="Enable or pause promotion for your work")
    configure.add_argument("site_id")
    configure.add_argument("--enabled", choices=["true", "false"], required=True)
    for name in ("links", "report"):
        listing = actions.add_parser(name)
        listing.add_argument("--cursor")
        listing.add_argument("--limit", type=int, default=10)
        if name == "report":
            listing.add_argument("--site-id")


def execute(api, args, ensure_identity):
    command = args.referral_command
    if command == "source":
        if not 64 <= len(args.receipt) <= 2048 or not re.fullmatch(
            r"[A-Za-z0-9_=-]+", args.receipt
        ):
            raise RuntimeError("Use the platform-issued handoff copied from the install page")
        with api.store.lock():
            value = load(api)
            # A second installation cannot silently replace the first local source.
            if value:
                return {"saved": False, "status": value["status"], "reason": "source_already_saved"}
            atomic_json(
                path(api), {"server": api.server, "receipt": args.receipt, "status": "pending"}
            )
        return {"saved": True, "status": "pending"}
    if command == "status":
        with api.store.lock():
            value = load(api)
        return {"status": value["status"] if value else "none"}
    if command == "link":
        ensure_identity(api)
        return api.request(
            "POST",
            "/v1/hosting/referrals/links",
            authenticated=True,
            json={"site_id": args.site_id, "parent_code": args.parent_code},
        )
    if command == "configure":
        return api.request(
            "PUT",
            "/v1/hosting/referrals/sites/" + args.site_id,
            authenticated=True,
            json={"enabled": args.enabled == "true"},
        )
    if not 1 <= args.limit <= 20:
        raise RuntimeError("Use a page size from 1 to 20")
    params = {"limit": args.limit}
    if args.cursor:
        params["cursor"] = args.cursor
    if command == "report" and args.site_id:
        params["site_id"] = args.site_id
    return api.request("GET", "/v1/hosting/referrals/" + command, authenticated=True, params=params)
