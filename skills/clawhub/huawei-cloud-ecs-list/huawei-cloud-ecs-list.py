#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Huawei Cloud ECS Query Skill.

Lists ECS instances and shows instance details via the hcloud CLI.
Read-only operations only (List / Show). Authentication uses AK/SK
read dynamically from environment variables (never hardcoded).

Subcommands:
  list             Query ECS instance list with optional filters.
  show             Query details of a single ECS instance by ID.
  capability-list  Print the capabilities supported by this skill.

Output: JSON to stdout (all API fields preserved).
Errors: JSON to stderr with non-zero exit codes.
"""

import argparse
import json
import os
import subprocess
import sys

EXIT_OK = 0
EXIT_INVALID_INPUT = 2
EXIT_AK_SK_MISSING = 3
EXIT_API_ERROR = 4

HCLOUD_TIMEOUT = 30
DEFAULT_REGION = "cn-north-4"
VALID_STATUSES = [
    "ACTIVE", "BUILD", "ERROR", "HARD_REBOOT", "MIGRATING",
    "REBOOT", "REBUILD", "RESIZE", "REVERT_RESIZE", "SHUTOFF",
    "VERIFY_RESIZE",
]


def _load_credentials():
    """Dynamically scan environment variables for AK/SK.

    No hardcoded variable names — matches any HUAWEI*/HW*/HWC* env var
    whose name contains ACCESS_KEY / SECRET_KEY or ends with _AK / _SK.
    """
    ak, sk = "", ""
    for key, val in os.environ.items():
        upper = key.upper()
        if not (upper.startswith("HUAWEI") or upper.startswith("HW") or upper.startswith("HWC")):
            continue
        if "ACCESS_KEY" in upper or upper.endswith("_AK") or upper == "AK":
            ak = val or ak
        if "SECRET_KEY" in upper or upper.endswith("_SK") or upper == "SK":
            sk = val or sk
    return ak, sk


def _emit_error(message, code=EXIT_API_ERROR, details=None):
    """Print a JSON error object to stderr and exit."""
    payload = {"error": message}
    if details is not None:
        payload["details"] = details
    json.dump(payload, sys.stderr, ensure_ascii=False)
    sys.stderr.write("\n")
    sys.exit(code)


def _parse_first_json(text):
    """Parse the first JSON object from text.

    hcloud may append diagnostic text after the JSON body on API errors,
    so a plain json.loads can fail. Fall back to raw_decode to grab just
    the leading JSON object.
    """
    if not text:
        return None
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    try:
        decoder = json.JSONDecoder()
        obj, _ = decoder.raw_decode(text)
        return obj
    except (json.JSONDecodeError, ValueError):
        return None


def _handle_api_error(err):
    """Emit an appropriate error for an hcloud API error object."""
    if isinstance(err, dict):
        msg = str(err.get("message", ""))
        code = str(err.get("code", ""))
    else:
        msg = str(err)
        code = ""
    blob = (msg + " " + code).lower()
    if any(s in blob for s in ("could not be found", "not found", "not exist", "404")):
        _emit_error(
            "Instance not found. The specified server_id does not exist "
            "or is not accessible in this region.",
            code=EXIT_INVALID_INPUT,
            details=msg,
        )
    if any(s in blob for s in ("unauthorized", "invalid ak", "401", "forbidden", "403")):
        _emit_error(
            "Authentication failed. AK/SK is invalid or lacks ECS read permission.",
            code=EXIT_AK_SK_MISSING,
            details=msg,
        )
    _emit_error("API call failed: %s" % (msg or code), code=EXIT_API_ERROR, details=code)


def _run_hcloud(service, operation, params):
    """Invoke hcloud CLI with AK/SK injected from the environment.

    Returns the parsed JSON response. Exits with an error on failure.

    hcloud may return exit 0 even on API errors, placing the error JSON in
    stdout (optionally followed by diagnostic text). We parse the first JSON
    object and inspect it for an "error" key before trusting the response.
    """
    ak, sk = _load_credentials()
    if not ak or not sk:
        _emit_error(
            "AK/SK credentials missing. Set Huawei Cloud AK and SK as "
            "environment variables (e.g. HUAWEI_AK / HUAWEI_SK) and retry.",
            code=EXIT_AK_SK_MISSING,
        )

    cmd = [
        "hcloud", service, operation,
        "--cli-access-key=" + ak,
        "--cli-secret-key=" + sk,
    ] + params

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=HCLOUD_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        _emit_error(
            "hcloud CLI timed out after %d seconds." % HCLOUD_TIMEOUT,
            code=EXIT_API_ERROR,
        )
    except FileNotFoundError:
        _emit_error(
            "hcloud CLI not found. Install KooCLI (see references/cli-installation-guide.md).",
            code=EXIT_API_ERROR,
        )

    stdout = proc.stdout.strip()
    stderr = proc.stderr.strip()

    parsed = _parse_first_json(stdout)

    if isinstance(parsed, dict) and "error" in parsed:
        _handle_api_error(parsed["error"])

    if proc.returncode != 0:
        combined = stderr or stdout
        lower = combined.lower()
        if any(s in lower for s in ("not found", "not exist", "could not be found", "404")):
            _emit_error(
                "Instance not found. The specified server_id does not exist "
                "or is not accessible in this region.",
                code=EXIT_INVALID_INPUT,
                details=combined[:500],
            )
        if any(s in lower for s in ("unauthorized", "invalid ak", "401", "forbidden", "403")):
            _emit_error(
                "Authentication failed. AK/SK is invalid or lacks ECS read permission.",
                code=EXIT_AK_SK_MISSING,
                details=combined[:500],
            )
        _emit_error(
            "hcloud CLI failed (exit %d)." % proc.returncode,
            code=EXIT_API_ERROR,
            details=combined[:500],
        )

    if parsed is None:
        if not stdout:
            return {}
        _emit_error(
            "hcloud returned non-JSON output.",
            code=EXIT_API_ERROR,
            details=stdout[:500],
        )

    return parsed


def cmd_list(args):
    """Query ECS instance list with optional filters."""
    params = ["--cli-region=" + args.region]
    if args.status:
        params.append("--status=" + args.status)
    if args.name:
        params.append("--name=" + args.name)
    if args.flavor:
        params.append("--flavor=" + args.flavor)
    if args.ip:
        params.append("--ip=" + args.ip)
    if args.limit is not None:
        params.append("--limit=" + str(args.limit))
    if args.offset is not None:
        params.append("--offset=" + str(args.offset))

    result = _run_hcloud("ECS", "ListServersDetails", params)
    if isinstance(result, dict) and "servers" in result:
        servers = result.get("servers") or []
        count = result.get("count", len(servers))
        output = {"count": count, "servers": servers}
    else:
        output = {"count": 0, "servers": []}
    json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return EXIT_OK


def cmd_show(args):
    """Query details of a single ECS instance by ID."""
    params = [
        "--cli-region=" + args.region,
        "--server_id=" + args.server_id,
    ]
    result = _run_hcloud("ECS", "ShowServer", params)
    if isinstance(result, dict) and "server" in result:
        output = {"server": result.get("server")}
    else:
        output = {"server": result}
    json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return EXIT_OK


CAPABILITIES = [
    {
        "operation": "list",
        "description": "List ECS instances with optional filters.",
        "filters": ["region", "status", "name", "flavor", "ip", "limit", "offset"],
        "readonly": True,
        "api": "ECS ListServersDetails (GET /v1/{project_id}/cloudservers/detail)",
    },
    {
        "operation": "show",
        "description": "Show details of a single ECS instance by server_id.",
        "params": ["server_id (required)", "region"],
        "readonly": True,
        "api": "ECS ShowServer (GET /v1/{project_id}/cloudservers/{server_id})",
    },
]


def cmd_capability_list(args):
    """Print supported capabilities."""
    output = {
        "skill": "huawei-cloud-ecs-list",
        "service": "ECS",
        "mode": "CLI (hcloud)",
        "operations": CAPABILITIES,
    }
    json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return EXIT_OK


def build_parser():
    parser = argparse.ArgumentParser(
        prog="huawei-cloud-ecs-list",
        description="Query Huawei Cloud ECS instances (list / show). "
                    "Read-only. JSON output with all fields.",
    )
    sub = parser.add_subparsers(dest="command", metavar="{list|show|capability-list}")

    p_list = sub.add_parser("list", help="List ECS instances with optional filters.")
    p_list.add_argument("--region", default=DEFAULT_REGION,
                        help="Region (default: %s)." % DEFAULT_REGION)
    p_list.add_argument("--status", choices=VALID_STATUSES,
                        help="Filter by instance status.")
    p_list.add_argument("--name", help="Filter by instance name (fuzzy match).")
    p_list.add_argument("--flavor", help="Filter by flavor ID (e.g. s6.small.1).")
    p_list.add_argument("--ip", help="Filter by IPv4 address (fuzzy match).")
    p_list.add_argument("--limit", type=int,
                        help="Max results per page (default 25, max 1000).")
    p_list.add_argument("--offset", type=int, help="Page number (default 1).")
    p_list.set_defaults(func=cmd_list)

    p_show = sub.add_parser("show", help="Show details of a single ECS instance.")
    p_show.add_argument("--server-id", required=True, dest="server_id",
                        help="ECS instance ID (UUID).")
    p_show.add_argument("--region", default=DEFAULT_REGION,
                        help="Region (default: %s)." % DEFAULT_REGION)
    p_show.set_defaults(func=cmd_show)

    p_cap = sub.add_parser("capability-list", help="List supported operations.")
    p_cap.set_defaults(func=cmd_capability_list)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return EXIT_OK
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
