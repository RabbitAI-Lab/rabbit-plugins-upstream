#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.28.0",
# ]
# ///
"""
aoment-hd-repair CLI

Agent API Key authenticated image HD repair/upscale powered by Aoment AI.
The client calls the dedicated skill API endpoint only.
"""

import argparse
import base64
import json
import mimetypes
import os
import re
import sys

import requests

API_BASE = "https://www.aoment.com"
DEFAULT_MODEL = "image-hd-repair"
REQUEST_TIMEOUT = 660


def _auth_headers(api_key: str) -> dict:
    return {"Authorization": f"Bearer {api_key}"}


def _json_or_error(response: requests.Response) -> dict:
    try:
        result = response.json()
    except ValueError:
        return {"success": False, "error": response.text or f"HTTP {response.status_code}"}

    if not response.ok and result.get("success") is not False:
        result["success"] = False
        result.setdefault("error", f"HTTP {response.status_code}")
    return result


def _read_image_source(source: str) -> tuple[str, bytes, str]:
    if source.startswith("http"):
        response = requests.get(source, timeout=60)
        response.raise_for_status()
        content_type = response.headers.get("content-type") or "image/png"
        return "input.png", response.content, content_type

    if os.path.exists(source):
        with open(source, "rb") as file:
            content = file.read()
        content_type = mimetypes.guess_type(source)[0] or "image/png"
        return os.path.basename(source) or "input.png", content, content_type

    try:
        content = base64.b64decode(source)
    except Exception as exc:
        raise ValueError(f"--image must be a local path, URL, or base64 image: {exc}") from exc

    return "input.png", content, "image/png"


def repair_image(api_base: str, args: argparse.Namespace) -> dict:
    url = f"{api_base}/api/skills/aoment-image-video/hd-repair"
    filename, image_bytes, content_type = _read_image_source(args.image)

    data = {
        "resolution": args.resolution,
        "model": args.model,
    }
    files = {
        "file": (filename, image_bytes, content_type),
    }

    response = requests.post(
        url,
        data=data,
        files=files,
        headers=_auth_headers(args.api_key),
        timeout=REQUEST_TIMEOUT,
    )
    result = _json_or_error(response)

    if not result.get("success"):
        return {"success": False, "error": result.get("error", "hd repair failed")}

    return {
        "success": True,
        "tool_type": "hd-repair",
        "data": {"image_url": result.get("imageUrl")},
    }


def _read_local_version() -> str | None:
    try:
        skill_md = os.path.join(os.path.dirname(__file__), "..", "SKILL.md")
        with open(skill_md, "r", encoding="utf-8") as file:
            content = file.read()
        match = re.search(r"^version:\s*(.+)$", content, re.MULTILINE)
        return match.group(1).strip() if match else None
    except Exception:
        return None


def _compare_versions(local: str, remote: str) -> int:
    def parse(version: str) -> tuple:
        return tuple(int(part) for part in version.split("."))

    try:
        local_parts, remote_parts = parse(local), parse(remote)
        return (local_parts > remote_parts) - (local_parts < remote_parts)
    except Exception:
        return 0


def _check_version(api_base: str) -> None:
    local_version = _read_local_version()
    if not local_version:
        return

    try:
        response = requests.get(f"{api_base}/api/skills/aoment-image-video/version", timeout=5)
        data = response.json()
        if not data.get("success"):
            return
        remote_version = data.get("data", {}).get("version")
        if remote_version and _compare_versions(local_version, remote_version) < 0:
            json.dump(
                {
                    "success": False,
                    "error": "update_required",
                    "current_version": local_version,
                    "latest_version": remote_version,
                    "message": (
                        f"Skill version is outdated (current {local_version}, "
                        f"latest {remote_version}). Download the latest package and retry."
                    ),
                },
                sys.stdout,
                ensure_ascii=False,
                indent=2,
            )
            print()
            sys.exit(1)
    except Exception:
        return


def main():
    parser = argparse.ArgumentParser(description="aoment-hd-repair CLI")
    parser.add_argument("--api-key", "-k", required=True, help="Agent API Key")
    parser.add_argument(
        "--image",
        "-i",
        required=True,
        help="Input image as a local path, URL, or base64 data",
    )
    parser.add_argument(
        "--resolution",
        default="4K",
        choices=["2K", "4K", "8K"],
        help="Target resolution",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Model ID. Only image-hd-repair is supported.",
    )
    args = parser.parse_args()

    _check_version(API_BASE)

    try:
        result = repair_image(API_BASE, args)
    except requests.exceptions.Timeout:
        result = {"success": False, "error": "request timed out"}
    except requests.exceptions.RequestException as exc:
        result = {"success": False, "error": f"network request failed: {exc}"}
    except Exception as exc:
        result = {"success": False, "error": f"internal error: {exc}"}

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()

