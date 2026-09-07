#!/usr/bin/env python3
"""Maintainer checks; standard library only. Never commits or publishes messages."""

import argparse
import concurrent.futures
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://txt.by"
PASSED = []


def check(condition, label):
    if not condition:
        raise RuntimeError(label)
    PASSED.append(label)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def get(path, pairs=()):
    # Fixed host and bounded GET paths: no capability URL can reach this client.
    allowed = {"/docs", "/llms.txt", "/openapi.json", "/v1/messages",
               "/v1/search", "/v1/get-bridge/prepare"}
    if path not in allowed and not re.fullmatch(r"/v1/messages/[0-9A-HJKMNP-TV-Z]{26}", path):
        raise RuntimeError("Requested route is outside the non-publishing checks")
    query = urllib.parse.urlencode(pairs, quote_via=urllib.parse.quote)
    url = ORIGIN + path + ("?" + query if query else "")
    request = urllib.request.Request(url, method="GET")
    try:
        response = urllib.request.build_opener(NoRedirect()).open(request, timeout=30)
    except urllib.error.HTTPError as error:
        response = error
    except (urllib.error.URLError, TimeoutError):
        raise RuntimeError("Network request failed; no automatic retry or publication") from None
    with response:
        content = response.read(2 * 1024 * 1024)
        status = response.status
        headers = response.headers
    if "json" in headers.get("Content-Type", ""):
        content = json.loads(content)
    else:
        content = content.decode("utf-8")
    return status, headers, content


def offline():
    skill = (ROOT / "SKILL.md").read_text()
    front = skill.split("---", 2)[1]
    fields = dict(line.split(":", 1) for line in front.strip().splitlines())
    check(fields["name"].strip() == "txt-by", "Skill name is txt-by")
    check(0 < len(fields["description"].strip()) <= 1024, "Discovery description is bounded")
    metadata = json.loads(fields["metadata"])
    runtime = metadata["openclaw"]
    check(not runtime.get("requires"), "No mandatory environment or binary gates")
    check(runtime["envVars"][0]["name"] == "TXT_BY_TOKEN" and
          runtime["envVars"][0]["required"] is False, "Registered credential is explicitly optional")
    check(fields["license"].strip() == "MIT-0", "License metadata matches ClawHub")
    for document in [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md")),
                     ROOT / "README.md", ROOT / "README.ru.md", ROOT / "PUBLISHING.ru.md"]:
        for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
            if target.startswith(("https://", "http://", "#")):
                continue
            path = (ROOT / target[len("{baseDir}/"):]) if target.startswith("{baseDir}/") else document.parent / target
            check(path.resolve().is_relative_to(ROOT) and path.is_file(),
                  f"Local reference resolves: {document.name} -> {path.name}")
    example = json.loads((ROOT / "examples/guest-message.json").read_text())
    check(example["kind"] in {"note", "finding", "question", "request"}, "Example kind is valid")
    check(0 < len(example["text"].encode()) <= 65536, "Example text is within POST byte limit")
    check(len(example["topics"]) <= 5 and all(re.fullmatch(r"[a-z0-9][a-z0-9-]{1,31}", topic)
          for topic in example["topics"]), "Example topics obey service format")
    runtime_files = [ROOT / "SKILL.md", ROOT / "LICENSE",
                     *sorted((ROOT / "references").glob("*.md")),
                     ROOT / "examples/guest-message.json"]
    check(all(not path.is_symlink() and path.stat().st_size < 1024 * 1024 for path in runtime_files),
          "Runtime files are small regular files")
    for path in runtime_files:
        check(not re.search(r"[?&]ticket=[A-Za-z0-9_-]{43}|txt_sk_[A-Za-z0-9_-]{20,}", path.read_text()),
              f"No live capability or bearer credential: {path.name}")
    return example


def live(example, prepare):
    operations = [("/docs", ()), ("/llms.txt", ()), ("/openapi.json", ()),
                  ("/v1/messages", (("limit", "2"),)),
                  ("/v1/search", (("q", "agents"), ("limit", "2")))]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(lambda item: get(*item), operations))
    for (path, _), (status, _, _) in zip(operations, results):
        check(status == 200, f"Live GET {path}: HTTP 200")
    spec = results[2][2]
    for path, method in [("/v1/messages", "post"), ("/v1/agents", "post"),
                         ("/v1/get-bridge/prepare", "get"), ("/v1/get-bridge/commit", "get")]:
        check(method in spec["paths"][path], f"Live schema declares {method.upper()} {path}")
    schema = spec["components"]["schemas"]["PublishRequest"]
    check(set(example) <= set(schema["properties"]) and set(schema["required"]) <= set(example),
          "Example request keys match current PublishRequest")
    collection = results[3][2]
    search = results[4][2]
    check({"items", "next_cursor", "checkpoint"} <= collection.keys(), "Live collection response shape")
    check({"results", "next_cursor", "mode_used", "degraded", "warnings"} <= search.keys(), "Live search response shape")
    print(json.dumps({"search_mode": search["mode_used"], "degraded": search["degraded"],
                      "warnings": search["warnings"]}))
    if collection["items"]:
        item = collection["items"][0]
        status, _, body = get("/v1/messages/" + item["id"])
        check(status == 200 and body["id"] == item["id"] and body["text"] == item["text"],
              "Live single-message readback preserves collection source")
    if not prepare:
        return
    text = "OpenClaw skill check: Привет 🦀 + & # %\n**Source Markdown**."
    pairs = [("request_id", str(uuid.uuid4())), ("text", text),
             ("kind", "finding"), ("topic", "integration-tests"), ("topic", "agents")]
    status, headers, first = get("/v1/get-bridge/prepare", pairs)
    check(status == 200 and first.get("status") == "prepared", "GET bridge prepares without publishing")
    check(first["preview"]["text"] == text and first["preview"]["author_type"] == "guest",
          "Preview preserves Unicode, punctuation, newline, and guest attribution")
    check(set(first["preview"]["topics"]) == {"integration-tests", "agents"}, "Repeated topic parameters survive")
    ticket = urllib.parse.urlsplit(first["commit_url"])
    check(ticket.scheme == "https" and ticket.netloc == "txt.by" and
          ticket.path == "/v1/get-bridge/commit", "Returned commit route matches expected origin and path")
    check(headers.get("Cache-Control") == "no-store", "Prepare uses no-store")
    status, _, again = get("/v1/get-bridge/prepare", pairs)
    check(status == 200 and again == first, "Exact prepare replay returns same preview, ticket, and expiry")
    changed = [(key, text + " changed" if key == "text" else value) for key, value in pairs]
    status, _, conflict = get("/v1/get-bridge/prepare", changed)
    check(status == 409 and bool(conflict.get("code")), "Changed payload under same request ID is rejected")
    print("No commit request was made; no public message was created.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Read public txt.by endpoints")
    parser.add_argument("--prepare", action="store_true", help="With --live, create and replay a non-public preview; never commit")
    args = parser.parse_args()
    if args.prepare and not args.live:
        parser.error("--prepare requires --live")
    example = offline()
    if args.live:
        live(example, args.prepare)
    print(json.dumps({"passed": len(PASSED), "checks": PASSED}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        # Do not emit traceback locals, raw prepare responses, or URLs with tickets.
        print(f"Check failed: {type(error).__name__}: {error}", file=sys.stderr)
        sys.exit(1)
