#!/usr/bin/env python3
"""flora-flow client: scan photos of a flower market, then find reference arrangements for the flowers the user likes
and what else to buy with them.

    flora.py quick PHOTO [PHOTO ...] [--flower NAME] [--flower-color COLOR] [--flower-photo N] [--say TEXT]
                   [--style-en TEXT] [--exclude-color COLOR]... [--anchor P:B]... [--wait SECONDS]   (the fast path)
    flora.py scan [--no-wait] [--wait SECONDS] PHOTO
    flora.py status [--wait SECONDS] [SCAN_ID]
    flora.py pair SCAN_ID [SCAN_ID ...] [--anchor 1:6] [--anchor 2:all] [--exclude-color pink] [--exclude 1:3] [--query-en TEXT] [--query TEXT]
                  [--top-k N] [--wait SECONDS] [--no-images]
    flora.py find SCAN_ID [--boxes 2,5] [--query-en TEXT] [--query TEXT] [--top-k N] [--wait SECONDS] [--no-images]
                  (the older single-photo search)
    flora.py whoami
    flora.py mcp-config [--remote]
    flora.py mcp                      (stdio MCP bridge; the agent host runs this)

Python 3.8+, standard library only. The last output line of every command except mcp and mcp-config is
`RESULT {...}` (one line of JSON, with exit_code in it). Exit codes: 0 done, 3 still running (or the GPU is still starting), 1 error,
2 usage error. Local data: ~/.flora-flow/ (FLORA_FLOW_HOME). Server: FLORA_FLOW_SERVER, else user.json, else the
address built into this file when it was downloaded.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import secrets
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

VERSION = "0.9.0"                # = SKILL.md version (a test keeps them equal)
DEFAULT_SERVER = "__FLORA_SERVER__"          # replaced with the public address when served from /skill/install/flora.py
PREFIX = "/skill/v1"
MAX_PHOTO_BYTES = 25 * 1024 * 1024
SHRINK_SIDE = 1600             # the server keeps photos at this long side anyway; shrinking first only makes the upload faster
SHRINK_OVER_BYTES = 1000000    # smaller files go up as they are
MAX_RETRY_WAIT_S = 30.0        # longest single wait before asking again while the GPU starts (the server's estimate runs high)
FINAL = ("done", "failed")
PROTOCOL_VERSIONS = ("2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05")
USER_AGENT = "flora-flow-client/" + VERSION


class Fail(Exception):
    """An error to report: message for the ERROR line, exit code, and what goes into RESULT.errors."""

    def __init__(self, message, code="error", exit_code=1, **extra):
        super().__init__(message)
        self.message, self.code, self.exit_code, self.extra = message, code, exit_code, extra


# --------------------------------------------------------------------------- local folder


def home():
    return Path(os.environ.get("FLORA_FLOW_HOME") or (Path.home() / ".flora-flow"))


def read_json(path, default=None):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def write_bytes(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)


def load_user():
    u = read_json(home() / "user.json")
    return u if isinstance(u, dict) and u.get("user_id") else None


LIVE_HOST = "flora.groundrl.com"
TEST_MODE = bool(os.environ.get("FLORA_FLOW_TEST"))   # tests set this (or a test copy sets it to True): never reach the live server


def server():
    s = os.environ.get("FLORA_FLOW_SERVER") or (load_user() or {}).get("server") or DEFAULT_SERVER
    s = (s or "").strip().rstrip("/")
    if TEST_MODE and LIVE_HOST in s:
        print("ERROR: test mode, but the server would be the live one (%s). Set FLORA_FLOW_SERVER and FLORA_FLOW_HOME to the test "
              "server and a test folder." % s, file=sys.stderr)
        sys.exit(4)
    if not s or s.startswith("__"):
        raise Fail("No server is configured. Ask the user to set FLORA_FLOW_SERVER (for example https://flora.groundrl.com, "
                   "without /skill/v1), or download flora.py again from the server.", "no_server")
    if s.endswith(PREFIX):
        s = s[: -len(PREFIX)]
    return s


def pending():
    p = read_json(home() / "pending.json", {})
    ids = p.get("scan_ids") if isinstance(p, dict) else None
    return [i for i in ids if isinstance(i, str)] if isinstance(ids, list) else []


def set_pending(ids):
    write_json(home() / "pending.json", {"scan_ids": list(dict.fromkeys(ids))})


def scan_dir(scan_id):
    return home() / "scans" / scan_id


# --------------------------------------------------------------------------- HTTP


def http(method, url, body=None, headers=None, timeout=60.0):
    """(status, parsed JSON or None, raw bytes). Raises Fail when the server cannot be reached or something in between answered."""
    h = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    h.update(headers or {})
    req = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            status, raw = r.status, r.read()
    except urllib.error.HTTPError as e:
        status = e.code
        try:
            raw = e.read()
        except OSError:                       # the server answered before it had read the upload and closed the connection
            raw = b""
    except (urllib.error.URLError, OSError, TimeoutError) as e:
        reason = getattr(e, "reason", e)
        raise Fail("Cannot reach the flora-flow server at %s (%s). If a sandbox, proxy or firewall blocks it, ask the user to allow "
                   "network access to that host, then run the same command again." % (url.split("/skill/")[0], reason), "unreachable")
    data = None
    if raw:
        try:
            data = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            data = None
    if data is None and status in (403, 407, 451):
        raise Fail("HTTP %d that is not from the flora-flow server: a sandbox, proxy or firewall is blocking it. Ask the user to "
                   "allow network access to %s, then run the same command again. Do not work around it with curl."
                   % (status, url.split("/skill/")[0]), "blocked")
    return status, data, raw


def api(method, path, user_id=None, payload=None, body=None, headers=None, timeout=60.0, ok=(200, 201, 202)):
    h = dict(headers or {})
    if user_id:
        h["X-Flora-User"] = user_id
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        h["Content-Type"] = "application/json"
    status, data, raw = http(method, server() + path, body, h, timeout)
    if status in ok and isinstance(data, dict):
        return status, data
    err = data.get("error") if isinstance(data, dict) else None
    if isinstance(err, dict):
        extra = {k: v for k, v in err.items() if k not in ("code", "message")}
        raise Fail("%s (HTTP %d %s)" % (err.get("message"), status, err.get("code")), str(err.get("code") or "error"), **extra)
    if status == 401:
        raise Fail("The server does not recognise this user ID (HTTP 401). Tell the user; do not create a new ID on your own.", "bad_user")
    if status == 413:
        raise Fail("The upload is too large (HTTP 413). One photo, at most 25 MB.", "photo_too_large")
    raise Fail("Unexpected answer from the server: HTTP %d %s" % (status, raw[:120].decode("utf-8", "replace")), "bad_answer")


def download(url, path, timeout=60.0):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
        write_bytes(path, data)
        return str(path)
    except (urllib.error.URLError, OSError, TimeoutError, ValueError):
        return None


def ensure_user():
    """(user_id, created). Creates an ID on first use and stores it in user.json."""
    u = load_user()
    if u:
        return u["user_id"], False
    _, data = api("POST", PREFIX + "/users")
    record = {"user_id": data["user_id"], "server": server(), "created_at": data.get("created_at")}
    path = home() / "user.json"
    write_json(path, record)
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass
    return data["user_id"], True


def multipart(field, filename, data):
    boundary = "----flora" + secrets.token_hex(16)
    ctype = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    safe = filename.replace('"', "_").replace("\r", "_").replace("\n", "_")
    head = ('--%s\r\nContent-Disposition: form-data; name="%s"; filename="%s"\r\nContent-Type: %s\r\n\r\n'
            % (boundary, field, safe, ctype)).encode("utf-8")
    return head + data + ("\r\n--%s--\r\n" % boundary).encode("ascii"), "multipart/form-data; boundary=" + boundary


# --------------------------------------------------------------------------- scans


def read_photo(path_text):
    p = Path(os.path.expanduser(path_text))
    if not p.is_file():
        raise Fail("Not a file: %s" % path_text, "usage", 2)
    size = p.stat().st_size
    if size == 0:
        raise Fail("The file is empty: %s" % path_text, "usage", 2)
    if size > MAX_PHOTO_BYTES:
        raise Fail("The photo is larger than 25 MB: %s. Send a smaller JPEG." % path_text, "photo_too_large", 2)
    return p, p.read_bytes()


def upload(user_id, path, data):
    body, ctype = multipart("photo", path.name, data)
    _, scan = api("POST", PREFIX + "/scans", user_id, body=body, headers={"Content-Type": ctype}, timeout=180.0)
    return scan


def fetch_scan(user_id, scan_id, wait_s=0.0):
    wait_s = max(0.0, min(float(wait_s), 50.0))
    _, scan = api("GET", "%s/scans/%s?wait_s=%s" % (PREFIX, scan_id, ("%.1f" % wait_s)), user_id, timeout=wait_s + 30.0)
    return scan


def wait_for(user_id, scan_id, seconds):
    """Poll until the scan is final or `seconds` have passed. Returns the last Scan."""
    deadline = time.monotonic() + max(0.0, seconds)
    while True:
        left = deadline - time.monotonic()
        scan = fetch_scan(user_id, scan_id, min(40.0, max(0.0, left)))
        if scan.get("status") in FINAL or deadline - time.monotonic() <= 0:
            return scan
        log("  %s: %s (queue %s, about %s s left, GPU %s)" % (scan_id, scan.get("status"), scan.get("queue_ahead"), scan.get("eta_s"),
                                                             (scan.get("gpu") or {}).get("state")))


def save_scan(scan, images=True):
    """Write scan.json (+ the two pictures once done). Returns {"scan_file", "overview", "sheet"} with local paths or None."""
    d = scan_dir(scan["scan_id"])
    write_json(d / "scan.json", scan)
    files = {"scan_file": str(d / "scan.json"), "overview": None, "sheet": None}
    if scan.get("status") == "done" and images and not scan.get("expired"):
        if scan.get("overview_url"):
            files["overview"] = download(scan["overview_url"], d / "overview.jpg")
        if scan.get("sheet_url"):
            files["sheet"] = download(scan["sheet_url"], d / "sheet.jpg")
    if scan.get("status") in FINAL:
        set_pending([i for i in pending() if i != scan["scan_id"]])
    return files


def describe_scan(scan, files=None):
    lines = ["Scan %s (%s): %s" % (scan["scan_id"], scan.get("filename") or "photo", scan.get("status"))]
    status = scan.get("status")
    if status == "failed":
        e = scan.get("error") or {}
        lines.append("FAILED %s: %s" % (e.get("code"), e.get("message")))
    elif status != "done":
        lines.append("Still running: queue_ahead=%s, about %s s, GPU %s. Run: flora.py status --wait 300 %s"
                     % (scan.get("queue_ahead"), scan.get("eta_s"), (scan.get("gpu") or {}).get("state"), scan["scan_id"]))
    else:
        photo = scan.get("photo") or {}
        lines.append("Photo %sx%s, %d flower boxes." % (photo.get("width"), photo.get("height"), len(scan.get("boxes") or [])))
        if scan.get("expired"):
            lines.append("The photo was deleted from the server after the retention period. Upload it again to search.")
        if scan.get("notice"):
            lines.append("NOTICE %s: %s" % (scan["notice"].get("code"), scan["notice"].get("message")))
        for b in scan.get("boxes") or []:
            x, y, w, h = b["box"]
            lines.append("  box %d: label guess %s / %s%s, score %.2f, x=%.0f%% y=%.0f%% w=%.0f%% h=%.0f%%"
                         % (b["box_id"], b.get("label_en"), b.get("label"), " (generic)" if b.get("generic") else "", b.get("score") or 0, x, y, w, h))
        if scan.get("boxes"):
            lines.append("The label guesses are usually wrong or just 'flower': choose boxes by the pictures, and never tell the user "
                         "a label as the flower's name.")
        if files and files.get("overview"):
            lines.append("Overview picture (numbers = box_id): %s" % files["overview"])
        if files and files.get("sheet"):
            lines.append("Contact sheet of the crops: %s" % files["sheet"])
    if scan.get("page_url"):
        lines.append("Result page for the user (private link): %s" % scan["page_url"])
    if scan.get("duplicate"):
        lines.append("This exact file was scanned before; this is that earlier result.")
    return lines


def scan_result(scan, files, user_id, created):
    return {"user_id": user_id, "user_id_created": created, "scan_id": scan["scan_id"], "status": scan.get("status"),
            "duplicate": bool(scan.get("duplicate")), "boxes": len(scan.get("boxes") or []),
            "box_ids": [b["box_id"] for b in scan.get("boxes") or []],
            "notice": scan.get("notice"), "error": scan.get("error"), "expired": bool(scan.get("expired")),
            "page_url": scan.get("page_url"), "scan_file": files.get("scan_file"), "overview_image": files.get("overview"),
            "sheet_image": files.get("sheet"), "pending_scan_ids": pending()}


def cmd_scan(args):
    path, data = read_photo(args.photo)
    user_id, created = ensure_user()
    if created:
        log("Created user ID %s (saved in %s). It is a credential: do not post it anywhere." % (user_id, home() / "user.json"))
    log("Uploading %s (%d KB)..." % (path.name, len(data) // 1024))
    scan = upload(user_id, path, data)
    set_pending(pending() + [scan["scan_id"]])
    if scan.get("status") not in FINAL and not args.no_wait:
        scan = wait_for(user_id, scan["scan_id"], args.wait)
    files = save_scan(scan)
    for line in describe_scan(scan, files):
        log(line)
    code = 0 if scan.get("status") == "done" else 1 if scan.get("status") == "failed" else 3
    return code, scan_result(scan, files, user_id, created)


def cmd_status(args):
    u = load_user()
    if not u:
        raise Fail("No user ID yet (%s does not exist). Scan a photo first: flora.py scan PHOTO" % (home() / "user.json"), "no_user")
    user_id = u["user_id"]
    ids = [args.scan_id] if args.scan_id else pending()
    if not ids:
        _, listing = api("GET", PREFIX + "/scans?limit=5", user_id)
        scans = listing.get("scans") or []
        log("Nothing pending. Most recent scans, newest first:" if scans else "This user ID has no scans yet.")
        for s in scans:
            log("  %s  %s  %d boxes  %s  %s%s" % (s["scan_id"], s.get("status"), len(s.get("boxes") or []), s.get("created_at"),
                                                   s.get("filename") or "", "  (expired)" if s.get("expired") else ""))
        return 0, {"user_id": user_id, "scans": [{"scan_id": s["scan_id"], "status": s.get("status"), "boxes": len(s.get("boxes") or []),
                                                  "created_at": s.get("created_at"), "expired": bool(s.get("expired"))} for s in scans],
                   "pending_scan_ids": []}
    results, worst = [], 0
    for sid in ids:
        try:
            scan = wait_for(user_id, sid, args.wait)
        except Fail as e:
            if e.code == "not_found":
                set_pending([i for i in pending() if i != sid])
            log("ERROR: %s: %s" % (sid, e.message))
            results.append({"scan_id": sid, "status": None, "error": {"code": e.code, "message": e.message}})
            worst = max(worst, 1)
            continue
        files = save_scan(scan)
        for line in describe_scan(scan, files):
            log(line)
        results.append(scan_result(scan, files, user_id, False))
        worst = max(worst, 0 if scan.get("status") == "done" else 1 if scan.get("status") == "failed" else 3)
    if len(results) == 1:
        return worst, results[0]
    return worst, {"user_id": user_id, "scans": results, "pending_scan_ids": pending()}


# --------------------------------------------------------------------------- find


def parse_boxes(text):
    if not text:
        return []
    try:
        return [int(t) for t in text.replace(" ", "").split(",") if t]
    except ValueError:
        raise Fail("--boxes takes box numbers separated by commas, for example --boxes 2,5", "usage", 2)


def find_references(user_id, scan_id, payload, wait_s):
    return post_search("%s/scans/%s/references" % (PREFIX, scan_id), user_id, payload, wait_s)


def post_search(path, user_id, payload, wait_s):
    """POST a search, retrying while the GPU is starting. Returns the result, or raises Fail (code gpu_starting when time ran out)."""
    deadline = time.monotonic() + max(0.0, wait_s)
    while True:
        try:
            _, result = api("POST", path, user_id, payload=payload, timeout=90.0)
            return result
        except Fail as e:
            if e.code not in ("gpu_starting", "busy"):
                raise
            retry = min(float(e.extra.get("retry_after_s") or 20), MAX_RETRY_WAIT_S)
            if time.monotonic() + retry > deadline:
                e.exit_code = 3
                raise
            log("  %s: waiting %d s, then trying again..." % ("the GPU is starting" if e.code == "gpu_starting" else "the server is busy", retry))
            time.sleep(retry)


def cmd_find(args):
    u = load_user()
    if not u:
        raise Fail("No user ID yet. Scan a photo first: flora.py scan PHOTO", "no_user")
    user_id = u["user_id"]
    payload = {}
    boxes = parse_boxes(args.boxes)
    if boxes:
        payload["box_ids"] = boxes
    if args.query_en:
        payload["query_en"] = args.query_en
    if args.query:
        payload["query"] = args.query
    if args.top_k is not None:
        payload["top_k"] = args.top_k
    if not boxes and not args.query_en:
        raise Fail("Give --boxes, --query-en, or both.", "usage", 2)
    result = find_references(user_id, args.scan_id, payload, args.wait)
    d = scan_dir(args.scan_id)
    find_file = d / "finds" / (result["find_id"] + ".json")
    used = result.get("used") or {}
    log("%d reference works (mode %s, boxes %s, text used %r), from %s works:"
        % (len(result.get("references") or []), result.get("mode"), used.get("box_ids"), used.get("text"), (result.get("gallery") or {}).get("works")))
    refs = []
    for r in result.get("references") or []:
        local = None if args.no_images else download(r["image_url"], d / "refs" / (r["work_id"] + ".jpg"))
        r["local_image"] = local
        pairs = ", ".join("box %s similarity %.2f" % (p["box_id"], p["similarity"]) for p in r.get("pairs") or []
                          if p.get("box_id") is not None)
        log("  %d. work %s  score %.3f  %s%s" % (r["rank"], r["work_id"], r["score"], r["image_url"], ("  matched: " + pairs) if pairs else ""))
        if local:
            log("     picture: %s" % local)
        refs.append({"rank": r["rank"], "work_id": r["work_id"], "image_url": r["image_url"], "local_image": local, "score": r["score"]})
    write_json(find_file, result)
    log("Scores only rank the results; they are not percentages. Look at the pictures before describing a work.")
    if result.get("page_url"):
        log("Result page for the user (private link): %s" % result["page_url"])
    return 0, {"user_id": user_id, "scan_id": args.scan_id, "find_id": result["find_id"], "mode": result.get("mode"), "used": used,
               "references": refs, "find_file": str(find_file), "page_url": result.get("page_url"),
               "finds_left_today": result.get("finds_left_today")}


def parse_refs(values, scan_ids, flag, whole_ok):
    """['1:6', '2:all', 'sabc...:all'] -> [{"scan_id", "box_id"}]. The part before the colon is a photo number (position among
    the SCAN_IDs, from 1) or, for a photo that is not in the list, its scan ID."""
    out = []
    for v in values or []:
        photo, _, box = v.partition(":")
        if photo.isdigit():
            if not 1 <= int(photo) <= len(scan_ids):
                raise Fail("%s %s: there is no photo %s; %d scan ID(s) were given." % (flag, v, photo, len(scan_ids)), "usage", 2)
            sid = scan_ids[int(photo) - 1]
        else:
            sid = photo
        if box.isdigit() and int(box) >= 1:
            bid = int(box)
        elif box == "all" and whole_ok:
            bid = None
        else:
            raise Fail("%s takes PHOTO:BOX, for example %s 1:6%s." % (flag, flag, " (or 2:all for a whole photo)" if whole_ok else ""), "usage", 2)
        out.append({"scan_id": sid, "box_id": bid})
    return out


def parse_boxes_pct(values, n_photos):
    """['1:30,40,12,18:白色洋桔梗', ...] -> [{"photo", "box", "name"?}]: boxes the agent drew, in percent of the upright photo."""
    out = []
    for v in values or []:
        parts = v.split(":", 2)
        try:
            photo = int(parts[0])
            box = [float(x) for x in parts[1].split(",")]
        except (ValueError, IndexError):
            photo, box = 0, []
        if len(box) != 4 or not 1 <= photo <= n_photos:
            raise Fail("--box takes PHOTO:x,y,w,h[:name] in percent of the photo as displayed, for example --box 1:30,40,12,18 "
                       "(photo 1 of %d)." % n_photos, "usage", 2)
        item = {"photo": photo, "box": box}
        if len(parts) == 3 and parts[2].strip():
            item["name"] = parts[2].strip()
        out.append(item)
    return out


def spot(item):
    where = "photo %s" % item["photo_index"] if item.get("photo_index") is not None else "your other photo"
    return "%s box %s" % (where, item["box_id"]) if item.get("box_id") is not None else "%s (whole photo)" % where


def not_wanted(result):
    ex = result.get("exclude") or {}
    if isinstance(ex, list):
        ex = {"colors": [], "refs": ex}
    if not ex.get("colors") and not ex.get("refs"):
        return ""
    text = "; not wanted: colour(s) " + ", ".join(result.get("excluded_colors") or ex.get("colors") or ["?"])
    if ex.get("refs"):
        text += " (from " + ", ".join(spot(e) for e in ex["refs"]) + ")"
    return text


def cmd_pair(args):
    u = load_user()
    if not u:
        raise Fail("No user ID yet. Scan a photo first: flora.py scan PHOTO", "no_user")
    user_id = u["user_id"]
    payload = {"scan_ids": list(args.scan_ids)}
    anchors = parse_refs(args.anchor, args.scan_ids, "--anchor", True)
    exclude = parse_refs(args.exclude, args.scan_ids, "--exclude", False)
    if anchors:
        payload["anchors"] = anchors
    ex = {}
    if args.exclude_color:
        ex["colors"] = list(args.exclude_color)
    if exclude:
        ex["refs"] = exclude
    if args.exclude_species:
        ex["species"] = list(args.exclude_species)
    if ex:
        payload["exclude"] = ex
    if args.query_en:
        payload["query_en"] = args.query_en
    if args.query:
        payload["query"] = args.query
    if args.top_k is not None:
        payload["top_k"] = args.top_k
    result = post_search("%s/references" % PREFIX, user_id, payload, args.wait)
    d = home() / "pairings" / result["find_id"]
    pairing_file = d / "pairing.json"
    log("%d plans from %s works, for %d photo(s); anchors: %s%s%s"
        % (len(result["plans"]), (result.get("gallery") or {}).get("works"), len(result["photos"]),
           ", ".join(spot(a) for a in result["anchors"]) or "none (whole stall)",
           not_wanted(result),
           ("; wish: %r" % result["used"]["query_en"]) if (result.get("used") or {}).get("query_en") else ""))
    for ph in result["photos"]:
        local = scan_dir(ph["scan_id"]) / "overview.jpg"
        log("  photo %d = scan %s%s" % (ph["photo_index"], ph["scan_id"], ("  numbered picture: %s" % local) if local.is_file() else ""))
    if not result["plans"]:
        log("Nothing suitable was found. Try other anchors, fewer excluded colours, or add photos with more flowers.")
    plans = []
    for plan in result["plans"]:
        local = None if args.no_images else download(plan["image_url"], d / "refs" / (plan["work_id"] + ".jpg"))
        plan["local_image"] = local
        moved = ""
        if (result.get("used") or {}).get("query_en") and plan.get("style_reranked") and plan.get("base_rank") not in (None, plan["rank"]):
            moved = "  (re-ranked by the wish; base rank %s)" % plan["base_rank"]
        log("Plan %d: work %s  score %.3f  %s%s" % (plan["rank"], plan["work_id"], plan["score"], plan["image_url"], moved))
        if local:
            log("  picture: %s" % local)
        if plan["anchor_matches"]:
            log("  uses: " + "; ".join("%s (similarity %.2f)" % (spot(m), m["similarity"]) for m in plan["anchor_matches"]))
        if plan["unused_anchors"]:
            log("  does not use: " + ", ".join(spot(x) for x in plan["unused_anchors"]))
        buy = []
        for g in plan["buy_groups"]:
            c = g["candidates"]
            buy.append({"photo_index": c[0]["photo_index"], "scan_id": c[0]["scan_id"], "box_id": c[0]["box_id"], "similarity": c[0]["similarity"],
                        "look_alikes": [{"photo_index": x["photo_index"], "box_id": x["box_id"]} for x in c[1:]]})
        if buy:
            log("  also buy (at most %d kind(s)): " % len(buy) + "; ".join(
                "%s (%.2f)%s" % (spot(b), b["similarity"], (" [look-alikes: %s]" % ", ".join(spot(x) for x in b["look_alikes"][:3])) if b["look_alikes"] else "")
                for b in buy))
        if plan.get("indexed_instances") is not None:
            log("  not found: %d of the %d indexed flowers of this work have nothing to buy in these photos; the picture may show "
                "more that were not indexed" % (plan["not_found"], plan["indexed_instances"]))
        elif plan["not_found"]:
            log("  %d flower(s) of this work have nothing similar in the photos" % plan["not_found"])
        warned = bool((plan.get("exclude_match") or {}).get("flagged"))
        if warned:
            log("  warning: it contains something like a flower the user does not want (ranked down)")
        plans.append({"rank": plan["rank"], "work_id": plan["work_id"], "image_url": plan["image_url"], "local_image": local, "score": plan["score"],
                      "uses": [{"photo_index": m["photo_index"], "scan_id": m["scan_id"], "box_id": m["box_id"], "similarity": m["similarity"]}
                               for m in plan["anchor_matches"]],
                      "unused_anchors": [{"photo_index": x["photo_index"], "scan_id": x["scan_id"], "box_id": x["box_id"]} for x in plan["unused_anchors"]],
                      "buy": buy, "not_found": plan["not_found"], "indexed_instances": plan.get("indexed_instances"),
                      "base_rank": plan.get("base_rank"), "like_unwanted": warned})
    write_json(pairing_file, result)
    if result["plans"]:
        log("Each 'kind' is a group of boxes that look alike; one flower often lands in several groups, so the count is an upper bound: "
            "look at the pictures and merge. Similarity and score only rank; they are not percentages. Look at the pictures of the works "
            "before describing them.")
    if result.get("page_url"):
        log("Result page for the user (private link): %s" % result["page_url"])
    return 0, {"user_id": user_id, "find_id": result["find_id"], "scan_ids": result["scan_ids"], "anchors": result["anchors"],
               "exclude": result["exclude"], "excluded_colors": result.get("excluded_colors"), "used": result.get("used"), "plans": plans, "pairing_file": str(pairing_file),
               "page_url": result.get("page_url"), "finds_left_today": result.get("finds_left_today")}


# --------------------------------------------------------------------------- the fast path: flora.py quick


def shrink(path, data):
    """The photo with its long side cut to SHRINK_SIDE by a tool of the operating system (sips on macOS, PowerShell on
    Windows, ImageMagick elsewhere), or the file as it is when it is small, already small enough or no tool works."""
    if len(data) <= SHRINK_OVER_BYTES:
        return data
    out = home() / "tmp" / ("shrink-%s.jpg" % secrets.token_hex(6))
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        if sys.platform == "darwin" and shutil.which("sips"):
            info = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)], capture_output=True, text=True, timeout=30)
            sides = [int(t) for t in info.stdout.split() if t.isdigit()]
            if not sides or max(sides) <= SHRINK_SIDE:
                return data
            subprocess.run(["sips", "-Z", str(SHRINK_SIDE), "-s", "format", "jpeg", "-s", "formatOptions", "88", str(path), "--out", str(out)],
                           capture_output=True, timeout=60, check=True)
        elif os.name == "nt" and shutil.which("powershell"):
            script = (
                "Add-Type -AssemblyName System.Drawing; $i=[System.Drawing.Image]::FromFile($args[0]); "
                "if (($i.PropertyIdList -contains 274)) { $o=$i.GetPropertyItem(274).Value[0]; "
                "$f=@{3='Rotate180FlipNone';6='Rotate90FlipNone';8='Rotate270FlipNone'}[[int]$o]; if ($f) { $i.RotateFlip($f) } }; "
                "$m=[Math]::Max($i.Width,$i.Height); if ($m -le %d) { exit 3 }; $s=%d/$m; "
                "$b=New-Object System.Drawing.Bitmap $i,([int]($i.Width*$s)),([int]($i.Height*$s)); "
                "$b.Save($args[1],[System.Drawing.Imaging.ImageFormat]::Jpeg)" % (SHRINK_SIDE, SHRINK_SIDE))
            r = subprocess.run(["powershell", "-NoProfile", "-Command", script, str(path), str(out)], capture_output=True, timeout=60)
            if r.returncode != 0:
                return data
        else:
            tool = shutil.which("magick") or shutil.which("convert")
            if not tool:
                return data
            subprocess.run([tool, str(path), "-auto-orient", "-resize", "%dx%d>" % (SHRINK_SIDE, SHRINK_SIDE), "-quality", "88", str(out)],
                           capture_output=True, timeout=60, check=True)
        small = out.read_bytes()
        return small if 0 < len(small) < len(data) else data
    except (OSError, ValueError, subprocess.SubprocessError):
        return data
    finally:
        try:
            out.unlink()
        except OSError:
            pass


def quick_cache():
    return read_json(home() / "quick-cache.json", {}) or {}


def cache_key(path):
    st = path.stat()
    return "%s|%d|%d" % (path.resolve(), st.st_size, int(st.st_mtime))


def run_quick(opts):
    """The whole fast path. opts: photos (paths), flower, flower_color, flower_photo, say, style_en, exclude_colors, anchors
    (['1:6', ...]), wait. Returns (exit code, text lines, RESULT dict, list of picture paths)."""
    t0 = time.monotonic()
    paths = list(opts.get("photos") or [])
    if not 1 <= len(paths) <= 8:
        raise Fail("Give 1 to 8 photos.", "usage", 2)
    photos = [read_photo(x) for x in paths]
    user_id, created = ensure_user()
    lines = []
    if created:
        lines.append("Created user ID %s (saved in %s). It is a credential: do not post it anywhere." % (user_id, home() / "user.json"))
    warm = threading.Thread(target=lambda: _quiet(lambda: api("POST", PREFIX + "/warmup", user_id, payload={}, timeout=20.0)), daemon=True)
    warm.start()                                                   # start a sleeping GPU while the photos go up

    cache = quick_cache()
    scans, fresh, errors = [None] * len(photos), [False] * len(photos), [None] * len(photos)

    def one(i):
        path, data = photos[i]
        key = cache_key(path)
        sid = cache.get(key)
        if sid:
            try:
                scan = fetch_scan(user_id, sid)
                if scan.get("status") != "failed" and not scan.get("expired"):
                    scans[i] = scan
                    return
            except Fail:
                pass
        try:
            scans[i] = upload(user_id, path, shrink(path, data))
            fresh[i] = True
            cache[key] = scans[i]["scan_id"]
        except Fail as e:
            errors[i] = e

    workers = [threading.Thread(target=one, args=(i,)) for i in range(len(photos))]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    for i, e in enumerate(errors):
        if e is not None:
            raise Fail("Photo %d (%s): %s" % (i + 1, photos[i][0].name, e.message), e.code, e.exit_code, **e.extra)
    write_json(home() / "quick-cache.json", cache)
    ids = [s["scan_id"] for s in scans]
    numbered = ", ".join("%d = %s" % (i + 1, p.name) for i, (p, _) in enumerate(photos))
    result = {"user_id": user_id, "user_id_created": created, "scan_ids": ids,
              "photos": [{"photo_index": i + 1, "path": str(p), "scan_id": ids[i]} for i, (p, _) in enumerate(photos)]}

    gpu = (scans[0].get("gpu") or {}).get("state")
    if any(fresh) and any(s.get("status") not in FINAL for s in scans) and gpu in ("off", "starting"):
        # first contact while the GPU sleeps: return now so that the agent can tell the user before waiting
        lines.append("Starting: tell the user in one line that it takes about 1.5-3 minutes, then run exactly the same command "
                     "again (it waits for the result).")
        result.update(status="starting_gpu", elapsed_s=round(time.monotonic() - t0, 1))
        return 3, lines, result, []

    deadline = time.monotonic() + float(opts.get("wait") or 300.0)
    told = 0.0
    while True:
        open_ = [i for i, s in enumerate(scans) if s.get("status") not in FINAL]
        if not open_:
            break
        left = deadline - time.monotonic()
        if left <= 0:
            lines.append("Photos: %s. Still being recognised; run the same command again in a minute." % numbered)
            result.update(status="running", elapsed_s=round(time.monotonic() - t0, 1))
            return 3, lines, result, []
        scans[open_[0]] = fetch_scan(user_id, ids[open_[0]], min(25.0, left))
        if time.monotonic() - told > 30 and scans[open_[0]].get("status") not in FINAL:
            told = time.monotonic()
            log("  waiting: photo %d is %s (GPU %s)" % (open_[0] + 1, scans[open_[0]].get("status"), (scans[open_[0]].get("gpu") or {}).get("state")))
    for i, s in enumerate(scans):
        if s.get("status") == "failed":
            raise Fail("Photo %d (%s) could not be recognised: %s. Run again without it." % (i + 1, photos[i][0].name,
                       (s.get("error") or {}).get("message")), "scan_failed")
    recognised = time.monotonic() - t0

    body = {"scan_ids": ids}
    style_missing = bool((opts.get("say") or "").strip()) and opts.get("style_en") is None   # --say without --style-en
    style = (opts.get("style_en") or "").strip()
    if style.lower().strip(" .\"'") in ("none", "no", "n/a", "null", "-", ""):
        opts = dict(opts, style_en=None)                            # 0.7.2: the template always has --style-en; "none" = not given
    for key, name in (("flower", "flower"), ("flower_color", "flower_color"), ("flower_photo", "flower_photo"), ("style_en", "query_en"),
                      ("say", "query")):
        if opts.get(key):
            body[name] = opts[key]
    if opts.get("anchors"):
        body["anchors"] = parse_refs(opts["anchors"], ids, "--anchor", True)
    if opts.get("boxes"):
        if opts.get("anchors"):
            raise Fail("Give either --box or --anchor, not both.", "usage", 2)
        body["boxes"] = parse_boxes_pct(opts["boxes"], len(ids))
    if opts.get("exclude_colors"):
        body["exclude"] = {"colors": list(opts["exclude_colors"])}
    if opts.get("detail"):
        body["detail"] = True
    key = json.dumps({k: v for k, v in body.items() if k != "query"}, sort_keys=True)
    last = read_json(home() / "quick-last.json", {}) or {}
    if opts.get("another") and not opts.get("detail") and last.get("key") == key:
        saved = read_json(home() / "quick" / str(last.get("find_id")) / "quick.json", None)
        if saved and saved.get("results"):                           # the next work of the same result: no new search
            return _picks_output(saved, lines, result, numbered, recognised, t0, int(last.get("shown", 1)))
    told = read_json(home() / "quick-told.json", {}) or {}
    patient = told.get("key") == key and time.time() - float(told.get("at") or 0) < 900
    try:
        out = post_search(PREFIX + "/quick", user_id, body, max(240.0, float(opts.get("wait") or 0)) if patient else 0.0)
    except Fail as e:
        if e.code == "gpu_starting" and not patient:            # tell the user first, then the same command waits
            write_json(home() / "quick-told.json", {"key": key, "at": time.time()})
            lines.append("Starting: tell the user in one line that it takes about 1.5-3 minutes, then run exactly the same command "
                         "again (it waits for the result).")
            result.update(status="starting_gpu", elapsed_s=round(time.monotonic() - t0, 1))
            return 3, lines, result, []
        if e.code == "not_found" and not e.extra.get("scan_id"):
            raise Fail("The server %s does not have the fast path yet (HTTP 404). The photos are uploaded and recognised (scan IDs: %s): "
                       "continue step by step with flora.py pair (section 6 of SKILL.md)." % (server(), " ".join(ids)), "no_quick", **{"scan_ids": ids})
        raise
    out["request"] = {k: v for k, v in body.items() if k != "scan_ids"}   # kept in quick.json: what was asked (self-test reads it)
    if "groups" not in out:
        write_json(home() / "quick-last.json", {"key": key, "find_id": out["find_id"], "shown": 0})
        code, lines, result, pictures = _picks_output(out, lines, result, numbered, recognised, t0, 0)
    else:
        code, lines, result, pictures = _detail_output(out, lines, result, numbered, recognised, t0, opts)
    if style_missing and lines:                                         # 0.7.2: no extra round now, a reminder for next time
        lines[-1] += (" Next time always add --style-en: the occasion or style the user named as one English sentence, or "
                      "--style-en none.")
    result["query_en"] = body.get("query_en")
    return code, lines, result, pictures


def _fetch_all(wanted):
    """Download [(path, url)] in parallel; returns the saved paths (None where it failed), in order."""
    got = [None] * len(wanted)

    def one(i):
        if wanted[i][1]:
            got[i] = download(wanted[i][1], wanted[i][0])
    threads = [threading.Thread(target=one, args=(i,)) for i in range(len(wanted))]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return got


def _picks_output(out, lines, result, numbered, recognised, t0, index):
    """0.6.1/0.7: one work at a time, as little to read as possible: the picture path(s), the two lines for the user, one line
    for the agent. index: which of the result's works (0 = the first; --another shows the next one without searching again).
    The lists and the other works are in quick.json next to the picture and on the page (--detail for the agent)."""
    qdir = home() / "quick" / out["find_id"]
    write_json(qdir / "quick.json", out)
    picks = out.get("results") or []
    done = dict(status="done", find_id=out["find_id"], page_url=out.get("page_url"), elapsed_s=round(time.monotonic() - t0, 1))
    if not picks or index >= len(picks):
        if not picks:
            lines.append(out.get("headline_zh") or "")
        else:
            lines.append("这次找到的 %d 件都给你看过了。想要别的，可以换一束花或多拍几个摊位。" % len(picks))
        if out.get("page_url"):
            lines.append("全部方案：%s" % out["page_url"])
        lines.append("Send the user these lines exactly; nothing else.")
        result.update(done, pictures=[], more=False)
        return 0, lines, result, []
    x = picks[index]
    one = download(x["pair_image_url"], qdir / ("pick-%d.jpg" % x["rank"])) if x.get("pair_image_url") else None
    text = x["line_zh"]
    if one:
        pictures = [one]
    else:                                                           # an older server: the single pictures, market first
        wanted = [(qdir / ("buy-%d-photo%d.jpg" % (x["rank"], b["photo_index"])), b["url"]) for b in x["buy_images"]]
        wanted.append((qdir / ("work-%d.jpg" % x["rank"]), x["image_url"]))
        pictures = [g for g in _fetch_all(wanted) if g]
        text = (text.replace("左图", "前面照片里", 1)          # 0.8 / 0.9: solid, dashed, gray, nothing framed
                .replace("右图", "最后一张图"))
    write_json(home() / "quick-last.json", {"key": (read_json(home() / "quick-last.json", {}) or {}).get("key"),
                                             "find_id": out["find_id"], "shown": index + 1})
    lines.extend(pictures)
    lines.append(text)
    if out.get("page_url"):
        lines.append("要买什么、在哪个摊：%s" % out["page_url"])
    lines.append("Show the user the picture%s above (open it or put it in your reply as an image, not just the path), then these two "
                 "lines exactly; nothing else." % ("" if len(pictures) == 1 else "s, in this order,"))
    result.pop("photos", None)                                      # the paths the agent gave; nothing to read again
    result.update(done, pictures=pictures, work_id=x["work_id"], rank=x["rank"], shown=index + 1, more=index + 1 < len(picks),
                  finds_left_today=out.get("finds_left_today"))
    return 0, lines, result, pictures


def _detail_output(out, lines, result, numbered, recognised, t0, opts):
    """--detail (the user asked why): the candidates A, B, C, every plan and its comparison card, for the agent to explain."""
    qdir = home() / "quick" / out["groups"][0]["find_id"]
    labelled = [g for g in out["groups"] if g.get("label")]
    wanted = [("candidates.jpg", out.get("sheet_url"))] if labelled else []
    if labelled:
        wanted += [("card-%s.jpg" % g["label"], g["plans"][0]["card_url"]) for g in labelled if g["plans"]]
    else:
        wanted += [("card-%d.jpg" % p_["rank"], p_["card_url"]) for p_ in out["groups"][0]["plans"][:3]]

    def fetch(i):
        if wanted[i][1]:
            pictures[i] = download(wanted[i][1], qdir / wanted[i][0])
    others = []                                                     # the cards of the other plans: on disk, opened only if needed
    for g in out["groups"]:
        for p_ in g["plans"]:
            name = "card-%s%d.jpg" % (g.get("label") or "", p_["rank"])
            p_["card_image"] = str(qdir / name)
            if (labelled and p_["rank"] > 1) or (not labelled and p_["rank"] > 3):
                others.append((name, p_["card_url"]))
    wanted += others
    pictures_n = len(wanted) - len(others)
    pictures = [None] * len(wanted)
    getters = [threading.Thread(target=fetch, args=(i,)) for i in range(len(wanted))]
    for g in getters:
        g.start()
    for g in getters:
        g.join()
    write_json(qdir / "quick.json", out)
    got = [x for x in pictures[:pictures_n] if x]
    for g in out["groups"]:                                         # card files of the first plans were saved under other names
        for p_ in g["plans"]:
            first = qdir / ("card-%s.jpg" % g["label"] if g.get("label") else "card-%d.jpg" % p_["rank"])
            if (not g.get("label") or p_["rank"] == 1) and first.is_file():
                p_["card_image"] = str(first)
            elif not Path(p_["card_image"]).is_file():
                p_["card_image"] = None

    lines.append("Photos: %s (recognised in %.0f s)." % (numbered, recognised))
    if labelled:
        what = " ".join(x for x in (opts.get("flower_color"), opts.get("flower")) if x)
        lines.append("Candidates for %r: open the pictures listed under 'pictures' in RESULT; the first shows boxes A, B, C. Pick the one "
                     "that is the user's flower and pass on its part below; its card is the next picture (cards of the other plans: "
                     "card_image in RESULT groups[].plans[]). None is right? Run flora.py status SCAN_ID to see the numbered photo "
                     "(for you only), then again with --anchor PHOTO:BOX." % what)
    else:
        lines.append("Open the card pictures listed under 'pictures' in RESULT, then pass on the plans below.")
    if out.get("note"):
        lines.append(out["note"])
    for g in out["groups"]:
        a = g.get("anchor")
        if g.get("label"):
            lines.append("--- %s = photo %s box %s ---" % (g["label"], a.get("photo_index") or "x", a["box_id"]))
        if g.get("coverage_zh"):
            lines.append(g["coverage_zh"])
        if not g["plans"]:
            lines.append("这几张照片里能配的花不够：没有一件作品能在这些摊上找到至少 2 种花。")
        full = 1 if labelled else 3
        for n, p_ in enumerate(g["plans"]):
            items = p_.get("shopping_zh") or ["这几个摊上没有找到可以一起配的花"]
            if n < full:
                lines.append("方案 %d（参考作品 %s，作品图 %s）给用户的清单：" % (p_["rank"], p_["work_id"], p_["image_url"]))
                if p_.get("consistency_zh"):
                    lines.append("  " + p_["consistency_zh"])
                lines.extend("  " + x for x in items[:6])
                codes = []
                for r in p_.get("card") or []:
                    if r["market"]:
                        codes.append("%d→%s%s" % (r["row"], "/".join("P%s-%s" % (m["photo_index"] or "x", m["box_id"] if m["box_id"] is not None else "all")
                                                                  for m in r["market"]), "" if all(m.get("checked", True) for m in r["market"]) else "?"))
                    elif r.get("lookalike"):
                        codes.append("%d→P%s-%s 不同种" % (r["row"], r["lookalike"]["photo_index"] or "x", r["lookalike"]["box_id"]))
                    else:
                        codes.append("%d→无" % r["row"])
                lines.append("  对照卡（只给你核对，别转给用户）：" + "  ".join(codes))
            else:
                lines.append("方案 %d（参考作品 %s）：%s" % (p_["rank"], p_["work_id"], "；".join(items[:4])))
        lines.append("页面：%s" % g["page_url"])
    lines.append("This is how the answer was found, for explaining it: tell the user in plain words, without cards, box numbers or "
                 "P-codes. Names are the work's: check each box on the card before you name it. The final picks: %s" % (out.get("page_url") or ""))
    lines.append(out.get("headline_zh") or "")
    result.update(status="done", pictures=got, groups=out["groups"], note=out.get("note"),
                  finds_left_today=out.get("finds_left_today"), elapsed_s=round(time.monotonic() - t0, 1))
    return 0, lines, result, got


def _quiet(fn):
    try:
        fn()
    except Exception:
        pass


def cmd_quick(args):
    code, lines, result, _ = run_quick({"photos": args.photos, "flower": args.flower, "flower_color": args.flower_color,
                                        "flower_photo": args.flower_photo, "say": args.say, "style_en": args.style_en,
                                        "exclude_colors": args.exclude_color, "anchors": args.anchor, "wait": args.wait,
                                        "detail": args.detail, "another": args.another, "boxes": args.box})
    for line in lines:
        log(line)
    return code, result


def cmd_whoami(args):
    u = load_user()
    try:
        srv = server()
    except Fail:
        srv = None
    log("user_id: %s" % (u["user_id"] if u else "(none yet; created on the first scan)"))
    log("server:  %s" % (srv or "(not configured)"))
    log("folder:  %s" % home())
    return 0, {"user_id": u["user_id"] if u else None, "server": srv, "home": str(home()), "pending_scan_ids": pending()}


def cmd_mcp_config(args):
    if args.remote:
        user_id, created = ensure_user()
        if created:
            print("Created user ID %s." % user_id, file=sys.stderr)
        entry = {"type": "http", "url": "%s/skill/mcp/%s" % (server(), user_id)}
        print("This URL contains the user ID and is a credential: never post it anywhere public. It has no scan_photo tool.", file=sys.stderr)
    else:
        entry = {"command": sys.executable, "args": [str(Path(__file__).resolve()), "mcp"]}
        env = {k: os.environ[k] for k in ("FLORA_FLOW_SERVER", "FLORA_FLOW_HOME") if os.environ.get(k)}
        if env:
            entry["env"] = env
        print("Add this entry to the mcpServers section of the agent's MCP settings, then restart the agent.", file=sys.stderr)
    print(json.dumps({"mcpServers": {"flora-flow": entry}}, indent=2))
    return 0, None


# --------------------------------------------------------------------------- MCP bridge (stdio)

INSTRUCTIONS = (
    "flora-flow helps a user at a flower market decide what to buy. Always start with quick_pairings, with all the photo paths, "
    "before any question: add only what the user pointed at or what you can see (photo number, colour, an English flower name "
    "only if you recognise it yourself; never ask what a flower is called). Send its one picture and its lines to the user as "
    "they are, nothing else, and open no other picture (another=true for 换一个; detail=true only when the user asks why). Step by step instead: scan_photo once per photo -> (scan_status until each "
    "is done) -> look at the numbered overview pictures and work out which boxes are the flowers the user has in mind (the "
    "anchors) -> find_pairings with all the scan_ids, in a fixed order, and the anchors. A box's label is the detector's guess "
    "among 17 classes and is usually wrong or just 'flower' (generic): never choose by it and never tell it to the user as the "
    "flower's name; look at the pictures. Scores and similarities only rank. The groups in a shopping list are boxes that look "
    "alike: their number is an upper bound on the kinds of flowers. Relay every notice verbatim. Show the user the pictures or "
    "give them page_url; never describe a reference work you have not seen. On gpu_starting, call again with the same arguments "
    "after retry_after_s. The user ID and links containing a scan or find ID are private. Photos are deleted from the server "
    "after 7 days; do not tell the user about it unless they ask."
)

SCAN_PHOTO_TOOL = {
    "name": "scan_photo",
    "title": "Scan a flower-market photo",
    "description": (
        "Usually not needed: use quick_pairings first. Upload one photo of flowers (a market stall, a shop, a bucket of stems, or a close-up of one flower) from this computer and detect the flowers in it. "
        "path is the absolute path of the photo (JPEG, PNG, WebP or HEIC, at most 25 MB); one photo per call. It waits up to wait_s "
        "seconds (default 45). When status is done the result lists boxes[] (box_id, label, label_en, generic, score, box in percent) "
        "and carries the overview picture with each box_id drawn on it plus a contact sheet of the crops: look at them. Scan every "
        "photo of the visit, then call find_pairings. Choose boxes by the pictures, not by label: label is the detector's guess among 17 classes, usually wrong "
        "or just 'flower' (generic=true), so never give it to the user as the flower's name. If status is queued, starting_gpu (a cold GPU takes about 2 minutes) or detecting, call scan_status with "
        "the scan_id and wait_s=50 until it is done; do not upload again. The same file uploaded twice returns the earlier result "
        "(duplicate=true). If notice.code is no_flowers, tell the user its message verbatim. If user_id_created is true, tell the "
        "user that an ID was created and stored in ~/.flora-flow/user.json."
    ),
    "inputSchema": {"type": "object", "properties": {
        "path": {"type": "string", "description": "Absolute path of the photo on this computer."},
        "wait_s": {"type": "number", "minimum": 0, "maximum": 50, "description": "Wait up to this many seconds for the result (default 45)."}},
        "required": ["path"], "additionalProperties": False},
    "annotations": {"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False},
}

# Copy of the server's tool list (app/skill/mcp.py tools(), default config), used only when the server cannot be reached
# while listing. A unit test keeps the two identical.
BUILTIN_TOOLS = json.loads(r'''[
 {
  "name": "scan_status",
  "title": "Flower scan status and boxes",
  "description": "Status and result of a flower-market photo scan. Give scan_id; without it you get this user's most recent scans. status: queued, starting_gpu (the GPU is cold; about 2 minutes), detecting, done, failed. Use wait_s (up to 50) and call again until status is done or failed. When done: boxes[] lists the detected flowers (box_id, label, label_en, generic, score, box = [x, y, w, h] in percent of the photo) and the result carries the overview picture with each box_id drawn on it, plus a contact sheet of the crops. Choose boxes by looking at the pictures, not by label: label is the detector's guess among 17 classes, usually wrong or just 'flower' (generic=true), so never give it to the user as the flower's name. If notice.code is no_flowers, tell the user its message verbatim; you can still search with query_en alone. Give the user page_url to see the result.",
  "inputSchema": {
   "type": "object",
   "properties": {
    "scan_id": {
     "type": "string",
     "description": "The scan_id returned by scan_photo (or the flora.py scan command)."
    },
    "wait_s": {
     "type": "number",
     "minimum": 0,
     "maximum": 50,
     "description": "Wait up to this many seconds for the scan to finish (default 0)."
    },
    "images": {
     "type": "boolean",
     "description": "Attach the pictures to the result (default true). Set false if you cannot view images."
    }
   },
   "additionalProperties": false
  },
  "annotations": {
   "readOnlyHint": true,
   "openWorldHint": false
  }
 },
 {
  "name": "find_pairings",
  "title": "Find arrangements for the flowers the user likes, and what to buy with them",
  "description": "For one visit to a flower market: find reference arrangements that use the flowers the user has set their heart on, and tell which other flowers in the photos go with them. scan_ids: the finished scans of this visit (1-8 photos); keep the same order in every call, because results name a flower as photo_index (position in scan_ids, from 1) + box_id. anchors: the flowers the user likes or already has, 0-5 of them, each {scan_id, box_id}; box_id null means the whole photo is that flower (a close-up), and an anchor's scan need not be in scan_ids (flowers already bought are not for sale). With no anchors the works are ranked by how much of them the stalls can supply. exclude leaves out COLOURS: exclude.colors takes colour names (pink, red, orange, yellow, green, blue, purple, brown, white, gray, black), exclude.refs up to 2 boxes that show the unwanted colour (their main colour is used when colors is not given; these boxes are not offered to buy). A work is left out when that colour covers a sizeable patch of one of its flowers; small touches can remain, so still look. Excluding a kind of flower is not supported yet: exclude.species returns the error exclude_species_unsupported; never swap in a colour on your own. query_en: optional wish in English, translated by you (e.g. '\u66f4\u7d20\u4e00\u70b9' -> 'understated, muted colours'); only then is the GPU needed. It re-orders only plans that match the anchors about equally well, so the same works may come back in a new order. query: the user's own words, recorded only. Returns plans[] best first (works where the stalls supply fewer than 2 kinds are left out, so there may be fewer than asked, or none). The text gives, per plan, a comparison card: each flower of the work (name, colour and part from the gallery annotation, or 'unannotated') against the market box matched to it, or 'not found in the market', and a shopping list by name. One card picture per plan is attached (left the work's flower, right the market box). Names are of the work's flowers: the market box was matched by appearance, so check its picture before naming it to the user. Never give the user the numbered stall photos. Similarity and score only rank; never present them as percentages. Errors naming a scan_id mean that photo is not done, failed or expired: fix it or leave it out. Error gpu_starting: call again with the same arguments after retry_after_s.",
  "inputSchema": {
   "type": "object",
   "properties": {
    "scan_ids": {
     "type": "array",
     "items": {
      "type": "string"
     },
     "minItems": 1,
     "maxItems": 8,
     "description": "The scans of this market visit, in a fixed order (photo 1, photo 2, ...)."
    },
    "anchors": {
     "type": "array",
     "maxItems": 5,
     "description": "The flowers the user likes or already has.",
     "items": {
      "type": "object",
      "properties": {
       "scan_id": {
        "type": "string"
       },
       "box_id": {
        "type": [
         "integer",
         "null"
        ],
        "minimum": 1,
        "description": "null: the whole photo (a close-up)."
       }
      },
      "required": [
       "scan_id",
       "box_id"
      ],
      "additionalProperties": false
     }
    },
    "exclude": {
     "type": "object",
     "description": "What the user does not want: colours (by name, or by boxes showing them).",
     "properties": {
      "colors": {
       "type": "array",
       "items": {
        "type": "string"
       },
       "maxItems": 3,
       "description": "Colour names: pink, red, orange, yellow, green, blue, purple, brown, white, gray, black."
      },
      "refs": {
       "type": "array",
       "maxItems": 2,
       "description": "Boxes showing the unwanted colour; used for the colour when colors is not given.",
       "items": {
        "type": "object",
        "properties": {
         "scan_id": {
          "type": "string"
         },
         "box_id": {
          "type": "integer",
          "minimum": 1
         }
        },
        "required": [
         "scan_id",
         "box_id"
        ],
        "additionalProperties": false
       }
      },
      "species": {
       "type": "array",
       "items": {
        "type": "string"
       },
       "description": "Not supported yet: a kind of flower to leave out. Gives the error exclude_species_unsupported, so that you can tell the user."
      }
     },
     "additionalProperties": false
    },
    "query_en": {
     "type": "string",
     "description": "Optional: the user's wish in English, a short phrase or sentence."
    },
    "query": {
     "type": "string",
     "description": "The user's wish in their own words (recorded only, not used for the search)."
    },
    "top_k": {
     "type": "integer",
     "minimum": 1,
     "maximum": 6,
     "description": "How many plans to return (default 3)."
    },
    "images": {
     "type": "boolean",
     "description": "Attach the pictures to the result (default true). Set false if you cannot view images."
    }
   },
   "required": [
    "scan_ids"
   ],
   "additionalProperties": false
  },
  "annotations": {
   "readOnlyHint": true,
   "openWorldHint": false
  }
 }
]''')


def tool_result(text, structured, is_error=False, pictures=None):
    content = [{"type": "text", "text": text}]
    content.extend(pictures or [])
    return {"content": content, "structuredContent": structured, "isError": is_error}


def tool_fail(e):
    return tool_result("Error %s: %s" % (e.code, e.message), {"error": dict({"code": e.code, "message": e.message}, **e.extra)}, True)


def mcp_forward(message, user_id=None, timeout=75.0):
    """Send one JSON-RPC message to the server's MCP endpoint and return its response object."""
    headers = {"Content-Type": "application/json"}
    if user_id:
        headers["X-Flora-User"] = user_id
    status, data, raw = http("POST", server() + "/skill/mcp", json.dumps(message).encode("utf-8"), headers, timeout)
    if isinstance(data, dict) and ("result" in data or "error" in data):
        return data
    raise Fail("Unexpected answer from the server's MCP endpoint: HTTP %d %s" % (status, raw[:120].decode("utf-8", "replace")), "bad_answer")


def bridge_scan_photo(arguments):
    if not isinstance(arguments, dict) or not isinstance(arguments.get("path"), str) or not arguments["path"].strip():
        raise Fail("path is required: the absolute path of one photo on this computer.", "bad_request")
    wait_s = arguments.get("wait_s", 45)
    if isinstance(wait_s, bool) or not isinstance(wait_s, (int, float)) or not 0 <= wait_s <= 50:
        raise Fail("wait_s must be a number from 0 to 50.", "bad_request")
    try:
        path, data = read_photo(arguments["path"].strip())
    except Fail as e:
        e.code = "bad_request" if e.code == "usage" else e.code
        raise
    user_id, created = ensure_user()
    scan = upload(user_id, path, data)
    set_pending(pending() + [scan["scan_id"]])
    # let the server build the result (text, boxes, pictures) so that scan_photo and scan_status look the same
    answer = mcp_forward({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                          "params": {"name": "scan_status", "arguments": {"scan_id": scan["scan_id"], "wait_s": wait_s}}}, user_id, wait_s + 25.0)
    if "result" not in answer:
        raise Fail("Uploaded as %s, but its status could not be read (%s). Call scan_status with that scan_id."
                   % (scan["scan_id"], (answer.get("error") or {}).get("message")), "bad_answer", scan_id=scan["scan_id"])
    result = answer["result"]
    sc = result.get("structuredContent")
    if isinstance(sc, dict):
        sc["user_id_created"] = created
        if scan.get("duplicate"):
            sc["duplicate"] = True
            result["content"][0]["text"] += "\nThis exact file was scanned before; this is that earlier result."
        if sc.get("status") in FINAL:
            set_pending([i for i in pending() if i != scan["scan_id"]])
    if created:
        result["content"][0]["text"] += "\nA user ID was created and saved in %s. Tell the user; it is a credential." % (home() / "user.json")
    return result


QUICK_TOOL = {
    "name": "quick_pairings",
    "title": "Fast path: one arrangement and where to buy its flowers",
    "description": (
        "Always the first step with photos of a flower market, before any question. Give the paths of all the photos of this "
        "visit (1-8; numbered 1, 2, ... in this order) and only what the user pointed at or what you can see: flower_photo "
        "(which photo), flower_color (e.g. 'pink'), flower (an English name, only if you recognise the flower in the photo "
        "yourself; never ask the user what it is called). A colour or style wish with no flower: the main colour you see as "
        "flower_color; nothing to go by: give none. One call uploads the photos, waits for the recognition and returns the "
        "answer: one picture (left the user's market photo with only the flowers to buy framed and numbered, right the "
        "reference work) and one line. Send the user that picture and the lines as they are, nothing else; open no other "
        "picture and add no list (the list is on the page). The user says 换一个: call again with the same arguments and "
        "another=true. Only when the user asks why: detail=true. If the answer says the recognition service is starting, tell "
        "the user in one line (about 1.5-3 minutes) and call again with the same arguments. An occasion or a style the user "
        "named (送长辈, 中性风, 浪漫) also goes in style_en, as one concrete English sentence (colours, mood, occasion)."
    ),
    "inputSchema": {"type": "object", "properties": {
        "paths": {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 8, "description": "Absolute paths of the photos."},
        "flower": {"type": "string", "description": "English name of the flower the user means, only if you recognise it in the photo yourself."},
        "flower_color": {"type": "string", "description": "Its colour: pink, red, orange, yellow, green, blue, purple, brown, white, gray, black (the nearest; other words are mapped or left out)."},
        "flower_photo": {"type": "integer", "minimum": 1, "description": "The photo it is in, when the user said so."},
        "say": {"type": "string", "description": "The user's own words (recorded only)."},
        "style_en": {"type": "string", "description": "Always give it: the occasion or style the user named (送长辈, 中性风, 浪漫, 莫奈花园) as one concrete English sentence (colours, mood, occasion), e.g. 'soft impressionist pastels, airy and romantic like Monet's garden'; 'none' when the user named none."},
        "exclude_colors": {"type": "array", "items": {"type": "string"}, "maxItems": 3, "description": "Colours the user does not want."},
        "anchors": {"type": "array", "items": {"type": "string"}, "maxItems": 5, "description": "PHOTO:BOX of the flower, e.g. '1:6': no candidates then."},
        "detail": {"type": "boolean", "description": "Only when the user asks why: the candidates, every plan and its comparison card."},
        "another": {"type": "boolean", "description": "The user said 换一个: the next work of the same result, with the same other arguments."}},
        "required": ["paths"], "additionalProperties": False},
    "annotations": {"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False},
}


def bridge_quick(arguments):
    if not isinstance(arguments, dict) or not isinstance(arguments.get("paths"), list) or not all(isinstance(x, str) for x in arguments["paths"]):
        raise Fail("paths is required: the absolute paths of the photos on this computer.", "bad_request")
    extra = set(arguments) - set(QUICK_TOOL["inputSchema"]["properties"])
    if extra:
        raise Fail("Unknown arguments: %s." % sorted(extra), "bad_request")
    opts = dict(arguments, photos=arguments["paths"], wait=240.0)
    try:
        code, lines, result, got = run_quick(opts)
    except Fail as e:
        e.code = "bad_request" if e.code == "usage" else e.code
        raise
    pictures = []
    for picture in got or []:
        try:
            pictures.append({"type": "image", "mimeType": "image/jpeg", "data": base64.b64encode(Path(picture).read_bytes()).decode("ascii")})
        except OSError:
            pass
    return tool_result("\n".join(lines), result, False, pictures)


def bridge_tools():
    try:
        answer = mcp_forward({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}, None, 20.0)
        remote = answer["result"]["tools"]
    except (Fail, KeyError, TypeError):
        remote = BUILTIN_TOOLS
    return [QUICK_TOOL, SCAN_PHOTO_TOOL] + [t for t in remote if t.get("name") not in ("scan_photo", "quick_pairings")]


def bridge_handle(msg):
    """One JSON-RPC message from the host -> the response object, or None for notifications."""
    if not isinstance(msg, dict) or msg.get("jsonrpc") != "2.0":
        return {"jsonrpc": "2.0", "id": msg.get("id") if isinstance(msg, dict) else None, "error": {"code": -32600, "message": "Not a JSON-RPC 2.0 message."}}
    method, msg_id = msg.get("method"), msg.get("id")
    if not isinstance(method, str) or "id" not in msg:
        return None
    params = msg.get("params") if isinstance(msg.get("params"), dict) else {}

    def ok(result):
        return {"jsonrpc": "2.0", "id": msg_id, "result": result}

    if method == "initialize":
        asked = params.get("protocolVersion")
        return ok({"protocolVersion": asked if asked in PROTOCOL_VERSIONS else PROTOCOL_VERSIONS[0],
                   "capabilities": {"tools": {"listChanged": False}},
                   "serverInfo": {"name": "flora-flow", "version": VERSION}, "instructions": INSTRUCTIONS})
    if method == "ping":
        return ok({})
    if method == "tools/list":
        return ok({"tools": bridge_tools()})
    if method == "tools/call":
        name = params.get("name")
        try:
            if name == "scan_photo":
                return ok(bridge_scan_photo(params.get("arguments")))
            if name == "quick_pairings":
                return ok(bridge_quick(params.get("arguments")))
            user_id, created = ensure_user()
            answer = mcp_forward({"jsonrpc": "2.0", "id": msg_id, "method": "tools/call", "params": params}, user_id)
            answer["id"] = msg_id
            return answer
        except Fail as e:
            return ok(tool_fail(e))
        except Exception as e:  # never let the bridge die on one bad call
            return ok(tool_result("Error internal: the local bridge failed (%s)." % type(e).__name__,
                                  {"error": {"code": "internal", "message": str(e)[:200]}}, True))
    return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found: %s" % method[:60]}}


def cmd_mcp(args):
    out = sys.stdout
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except ValueError:
            reply = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error."}}
        else:
            if isinstance(msg, list):
                replies = [r for r in (bridge_handle(m) for m in msg) if r is not None]
                reply = replies or None
            else:
                reply = bridge_handle(msg)
        if reply is not None:
            out.write(json.dumps(reply, ensure_ascii=False) + "\n")
            out.flush()
    return 0, None


# --------------------------------------------------------------------------- main


def log(text):
    print(text, flush=True)


def build_parser():
    p = argparse.ArgumentParser(prog="flora.py", description="flora-flow client")
    p.add_argument("--version", action="version", version="flora-flow " + VERSION)
    sub = p.add_subparsers(dest="command")
    s = sub.add_parser("quick", help="the fast path: photos (+ the flower the user likes) -> one work and where to buy its flowers")
    s.add_argument("photos", nargs="+", metavar="PHOTO", help="1-8 photos of this market visit; numbered 1, 2, ... in this order")
    s.add_argument("--flower", metavar="NAME", help="English name of the flower the user means (rose, sunflower), only if you recognise it yourself")
    s.add_argument("--flower-color", metavar="COLOR", help="its colour: pink, red, orange, yellow, green, blue, purple, brown, white, gray, black")
    s.add_argument("--flower-photo", type=int, metavar="N", help="the photo it is in, when the user said so")
    s.add_argument("--say", metavar="TEXT", help="the user's own words (recorded only)")
    s.add_argument("--style-en", metavar="TEXT", help="always: the occasion or style the user named as one concrete English sentence, or none")
    s.add_argument("--exclude-color", action="append", metavar="COLOR", help="a colour the user does not want; repeat for up to 3")
    s.add_argument("--anchor", action="append", metavar="PHOTO:BOX", help="use this box as the flower the user likes (no candidates)")
    s.add_argument("--box", action="append", metavar="P:x,y,w,h[:name]", help=argparse.SUPPRESS)   # 0.7: not offered yet (server off)
    s.add_argument("--wait", type=float, default=300.0, metavar="SECONDS", help="how long to wait for the recognition (default 300)")
    s.add_argument("--detail", action="store_true", help="only when the user asks why: the candidates, every plan and its comparison card")
    s.add_argument("--another", action="store_true", help="the user said 换一个: the next work of the same result (no new search)")
    s = sub.add_parser("scan", help="upload one photo and detect the flowers in it")
    s.add_argument("--no-wait", action="store_true", help="return right after uploading")
    s.add_argument("--wait", type=float, default=300.0, metavar="SECONDS", help="how long to wait for the result (default 300)")
    s.add_argument("photo", metavar="PHOTO")
    s = sub.add_parser("status", help="check pending scans, or one scan")
    s.add_argument("--wait", type=float, default=0.0, metavar="SECONDS", help="keep polling up to this long (default: check once)")
    s.add_argument("scan_id", nargs="?", metavar="SCAN_ID")
    s = sub.add_parser("pair", help="find arrangements that use the flowers the user likes, and what else to buy from the photos")
    s.add_argument("scan_ids", nargs="+", metavar="SCAN_ID", help="the scans of this market visit, always in the same order (photo 1, 2, ...)")
    s.add_argument("--anchor", action="append", metavar="PHOTO:BOX", help="a flower the user likes: 1:6 = box 6 of photo 1, 2:all = the whole "
                   "photo 2 (a close-up), SCAN_ID:all = a photo that is not in the list; repeat for up to 5")
    s.add_argument("--exclude-color", action="append", metavar="NAME", help="a colour the user does not want: pink, red, orange, yellow, green, "
                   "blue, purple, brown, white, gray or black; repeat for up to 3")
    s.add_argument("--exclude", action="append", metavar="PHOTO:BOX", help="a box showing a colour the user does not want (its main colour is "
                   "used when --exclude-color is not given; the box is not offered to buy); repeat for up to 2")
    s.add_argument("--exclude-species", action="append", metavar="NAME", help="a kind of flower to leave out: not supported yet, the server "
                   "answers exclude_species_unsupported")
    s.add_argument("--query-en", metavar="TEXT", help="the user's wish in English (only then is the GPU needed)")
    s.add_argument("--query", metavar="TEXT", help="the user's wish in their own words (recorded only)")
    s.add_argument("--top-k", type=int, metavar="N", help="how many plans (1-6, default 3)")
    s.add_argument("--wait", type=float, default=240.0, metavar="SECONDS", help="how long to keep retrying while the GPU starts (default 240)")
    s.add_argument("--no-images", action="store_true", help="do not download the pictures of the works")
    s = sub.add_parser("find", help="the older single-photo search: boxes of one scan and/or an English query")
    s.add_argument("scan_id", metavar="SCAN_ID")
    s.add_argument("--boxes", metavar="2,5", help="box numbers from the scan, most important first")
    s.add_argument("--query-en", metavar="TEXT", help="the user's wish in English")
    s.add_argument("--query", metavar="TEXT", help="the user's wish in their own words (recorded only)")
    s.add_argument("--top-k", type=int, metavar="N", help="how many references (1-6, default 2)")
    s.add_argument("--wait", type=float, default=240.0, metavar="SECONDS", help="how long to keep retrying while the GPU starts (default 240)")
    s.add_argument("--no-images", action="store_true", help="do not download the reference pictures")
    sub.add_parser("whoami", help="show the user ID, server and local folder (no network)")
    s = sub.add_parser("mcp-config", help="print the JSON for the agent's MCP settings")
    s.add_argument("--remote", action="store_true", help="the server's own endpoint (no scan_photo; the URL is a credential)")
    sub.add_parser("mcp", help="run the stdio MCP bridge (started by the agent host)")
    return p


COMMANDS = {"quick": cmd_quick, "scan": cmd_scan, "status": cmd_status, "pair": cmd_pair, "find": cmd_find, "whoami": cmd_whoami, "mcp-config": cmd_mcp_config, "mcp": cmd_mcp}


def main(argv=None):
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code else 0
    if not args.command:
        parser.print_help()
        return 2
    quiet = args.command in ("mcp", "mcp-config")
    try:
        code, result = COMMANDS[args.command](args)
        errors = []
    except Fail as e:
        if quiet:
            print("ERROR: %s" % e.message, file=sys.stderr)
            return e.exit_code
        log("ERROR: %s" % e.message)
        code, result = e.exit_code, {}
        errors = [dict({"code": e.code, "message": e.message}, **e.extra)]
    except KeyboardInterrupt:
        return 1
    if quiet:
        return code
    out = {"exit_code": code, "command": args.command}
    out.update(result or {})
    out["errors"] = errors
    log("RESULT " + json.dumps(out, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
