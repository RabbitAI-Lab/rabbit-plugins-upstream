"""
Bump Doctor: dependency-upgrade risk analyzer (core logic).

Given a package and a version bump, this gathers the upstream evidence a
developer would otherwise collect by hand, release notes / changelog, the
tag-to-tag commit summary, and open "breaking/migration" issues, then
cross-references it against the symbols the caller actually uses, producing a
focused risk report.

Framework-free and stdlib-only on purpose: it does the real work and returns
plain dicts, so it can be driven by the MCP server, a CLI, or tests unchanged,
and it runs anywhere Python does with no pip install.

Run directly for a smoke test:
    python analyzer.py npm express 4.18.2 5.0.0 --used app,Router,res.send
"""

from __future__ import annotations

import argparse
import json
import os
import re
from html import unescape
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from typing import Optional

USER_AGENT = "bump-doctor/0.1 (+https://clawhub/bump-doctor)"
GITHUB_API = "https://api.github.com"
TIMEOUT = 20

# Lines in release notes that tend to signal a real migration cost.
_BREAKING_RE = re.compile(
    r"\b(break(?:ing)?|removed?|drop(?:ped|s)?|renamed?|no longer|"
    r"replaced?|migrat|incompatible|deprecat)\b",
    re.IGNORECASE,
)
_DEPRECATION_RE = re.compile(r"\bdeprecat", re.IGNORECASE)

# Changelog lines that match _BREAKING_RE by accident but are really CI / chore /
# docs / tooling churn, not developer-facing API changes. Filtered out of the
# free heuristic pass so we stop crying wolf on "removed appveyor from ci".
_NOISE_RE = re.compile(
    r"\b(ci|appveyor|gha|github actions?|workflow|pipeline|lint(?:er|ing)?|"
    r"prettier|eslint|coverage|codecov|test(?:s|ing)?|readme|docs?|"
    r"document(?:ation|ed)?|changelog|"
    r"typo|dependabot|renovate|bump|deps?|dev[- ]?dependenc|refactor|chore|"
    r"benchmark|npm audit|pin(?:ning)?)\b",
    re.IGNORECASE,
)


class AnalyzerError(Exception):
    pass


@dataclass
class RiskItem:
    severity: str                       # "breaking" | "deprecation" | "note"
    summary: str
    affects_you: bool                   # touches a symbol you told us you use
    matched_symbols: list[str] = field(default_factory=list)
    source: str = ""                    # changelog / issue url


@dataclass
class RiskReport:
    ecosystem: str
    package: str
    from_version: str
    to_version: str
    repo: Optional[str]
    risk_score: int                     # 0-100
    headline: str = ""
    items: list[RiskItem] = field(default_factory=list)
    migration_steps: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #
def _get_json(url: str, token: Optional[str] = None) -> object:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if token and "github.com" in url:
        headers["Authorization"] = f"Bearer {token}"
        headers["Accept"] = "application/vnd.github+json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            raise AnalyzerError(f"Not found: {url}") from exc
        if exc.code in (403, 429):
            raise AnalyzerError(
                "Rate limited by upstream (pass a github_token to raise the limit)."
            ) from exc
        raise AnalyzerError(f"HTTP {exc.code} fetching {url}") from exc
    except urllib.error.URLError as exc:
        raise AnalyzerError(f"Network error fetching {url}: {exc.reason}") from exc


# --------------------------------------------------------------------------- #
# Registry resolution -> GitHub repo
# --------------------------------------------------------------------------- #
# github.com/<owner>/... paths whose first segment is a GitHub feature route,
# not a real repo owner. Guards the broad PyPI URL scan below from resolving a
# "Funding" sponsors link to a bogus "sponsors/<pkg>" repo.
_NON_REPO_OWNERS = frozenset({
    "sponsors", "marketplace", "apps", "about", "features", "topics",
    "collections", "trending", "settings", "notifications", "orgs", "login",
    "pricing", "readme", "site", "customer-stories",
})


def _repo_from_url(url: str) -> Optional[str]:
    if not url:
        return None
    m = re.search(r"github\.com[:/]+([^/]+)/([^/#?]+?)(?:\.git)?(?:[/#?].*)?$", url)
    if not m:
        return None
    owner, name = m.group(1), m.group(2)
    if owner.lower() in _NON_REPO_OWNERS:
        return None
    return f"{owner}/{name}"


# project_urls keys (compared case-insensitively) that most reliably point at the
# source repo. Tried before scanning every declared URL.
_PYPI_SOURCE_KEYS = ("source", "source code", "repository", "repo", "code",
                     "github", "git")


def _repo_from_pypi_info(info: dict) -> Optional[str]:
    """Resolve a GitHub repo from a PyPI package's metadata.

    PyPI packages declare URLs under arbitrary, inconsistently-cased project_urls
    keys: numpy uses lowercase ``source``, pandas ``repository``, sqlalchemy
    exposes GitHub only under ``Issue Tracker``. The previous fixed, CASE-SENSITIVE
    key list ("Source", "Repository", ...) missed every one of those and returned
    None. Strategy now: (1) canonical source-ish keys, case-insensitively;
    (2) failing that, scan EVERY declared URL for a github.com repo (an issues or
    blob deep-link still resolves to the correct owner/repo); (3) legacy
    home_page. Returns None when no GitHub repo is declared anywhere, rather than
    guess at one."""
    project_urls = info.get("project_urls") or {}
    lowered = {str(k).lower(): v for k, v in project_urls.items()}

    # 1. Canonical source keys first (most likely the repo itself, not a tracker).
    for key in _PYPI_SOURCE_KEYS:
        found = _repo_from_url(lowered.get(key) or "")
        if found:
            return found

    # 2. Any declared project URL that resolves to a github.com repo. Scan
    #    source/repo/home-ish keys first for a deterministic, sensible pick.
    def _rank(item: tuple) -> tuple:
        k = item[0].lower()
        primary = 0 if any(t in k for t in
                           ("source", "repo", "code", "git", "home")) else 1
        return (primary, k)

    for _key, url in sorted(project_urls.items(), key=_rank):
        found = _repo_from_url(url or "")
        if found:
            return found

    # 3. Legacy home_page as a last resort.
    return _repo_from_url(info.get("home_page") or "")


def resolve_repo(ecosystem: str, package: str) -> Optional[str]:
    ecosystem = ecosystem.lower()
    if ecosystem == "npm":
        data = _get_json(f"https://registry.npmjs.org/{urllib.parse.quote(package, safe='@/')}")
        repo = (data.get("repository") or {})
        url = repo.get("url") if isinstance(repo, dict) else repo
        return _repo_from_url(url or "")
    if ecosystem in ("pypi", "pip"):
        data = _get_json(f"https://pypi.org/pypi/{urllib.parse.quote(package)}/json")
        return _repo_from_pypi_info(data.get("info", {}) or {})
    raise AnalyzerError(f"Unsupported ecosystem: {ecosystem} (use npm or pypi)")


# --------------------------------------------------------------------------- #
# Evidence gathering from GitHub
# --------------------------------------------------------------------------- #
def _version_key(tag: str) -> tuple:
    nums = re.findall(r"\d+", tag)
    return tuple(int(n) for n in nums[:4]) if nums else (0,)


def _tag_version_for_package(tag: str, package: Optional[str]) -> Optional[tuple]:
    """Version key for a release tag, respecting monorepo per-package tags.

    Accepts plain version tags (``v6.0.0`` / ``6.0.0``) and tags qualified with
    THIS package's name (``react-router-dom@6.0.0``). Returns None for a tag that
    belongs to a *different* package in a monorepo (``react-router@6.0.0`` when we
    asked about ``react-router-dom``), so we never report on the wrong package."""
    tag = (tag or "").strip()
    m = re.match(r"^v?(\d+(?:\.\d+)+(?:[-.][0-9A-Za-z.]+)?)$", tag)
    if m:
        return _version_key(m.group(1))
    if package:
        m = re.match(re.escape(package) + r"[@/_-]v?(\d+(?:\.\d+)+)", tag)
        if m:
            return _version_key(m.group(1))
    return None


def fetch_release_notes(repo: str, from_v: str, to_v: str,
                        token: Optional[str], package: Optional[str] = None,
                        max_pages: int = 6) -> list[dict]:
    """Release entries strictly above from_v and up to/including to_v.

    Pages back through the releases API (newest-first) so an older target
    version is still found, otherwise a package now on a much newer version
    would return nothing and be falsely reported LOW. Stops early once an entire
    page sits at/below from_version."""
    lo, hi = _version_key(from_v), _version_key(to_v)
    picked: list[dict] = []
    for page in range(1, max_pages + 1):
        releases = _get_json(
            f"{GITHUB_API}/repos/{repo}/releases?per_page=100&page={page}", token)
        if not isinstance(releases, list) or not releases:
            break
        page_keys = []
        for rel in releases:
            tag = rel.get("tag_name") or rel.get("name") or ""
            key = _tag_version_for_package(tag, package)
            if key is None:
                continue  # a different monorepo package's tag, skip it
            page_keys.append(key)
            if lo < key <= hi:
                picked.append({"tag": tag, "body": rel.get("body") or "",
                               "url": rel.get("html_url", "")})
        # Every release on this page is already at/below from_version, older
        # pages only go further back, so stop.
        if page_keys and max(page_keys) <= lo:
            break
    return picked


def fetch_migration_issues(repo: str, token: Optional[str]) -> list[dict]:
    q = urllib.parse.quote(f"repo:{repo} is:issue is:open breaking OR migration OR upgrade")
    data = _get_json(f"{GITHUB_API}/search/issues?q={q}&per_page=10", token)
    items = data.get("items", []) if isinstance(data, dict) else []
    return [{"title": it.get("title", ""), "url": it.get("html_url", "")} for it in items]


# Markdown links whose text or target hints at a migration / upgrade doc, this
# is where projects like express hide the real breaking changes.
_DOC_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
_DOC_HINT_RE = re.compile(r"migrat|upgrad|breaking|changelog|what'?s[-_ ]?new",
                          re.IGNORECASE)


def _get_text(url: str, token: Optional[str] = None) -> str:
    headers = {"User-Agent": USER_AGENT}
    if token and "githubusercontent.com" in url:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        raise AnalyzerError(f"HTTP {exc.code} fetching {url}") from exc
    except urllib.error.URLError as exc:
        raise AnalyzerError(f"Network error fetching {url}: {exc.reason}") from exc


def _html_to_text(raw_html: str) -> str:
    """Crude but dependency-free HTML → text for doc pages hosted off-repo."""
    raw_html = re.sub(r"(?is)<(script|style|nav|header|footer|aside)[^>]*>.*?</\1>",
                      " ", raw_html)
    raw_html = re.sub(r"(?is)<br\s*/?>", "\n", raw_html)
    raw_html = re.sub(r"(?is)</(p|div|li|h[1-6]|tr|pre)>", "\n", raw_html)
    text = unescape(re.sub(r"(?s)<[^>]+>", " ", raw_html))
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n[ \t]*\n[ \t]*(\n[ \t]*)+", "\n\n", text).strip()


def _resolve_doc(repo: str, url: str) -> Optional[tuple[str, bool]]:
    """Return (fetch_url, is_html) for a doc link, or None if not fetchable."""
    blob = re.search(r"github\.com/([^/]+/[^/]+)/blob/([^/]+)/(.+)", url)
    if blob:
        return (f"https://raw.githubusercontent.com/{blob.group(1)}/"
                f"{blob.group(2)}/{blob.group(3)}", False)
    if url.startswith("https://"):
        return (url, True)                     # external doc site (e.g. project docs)
    if url.startswith("http://"):
        return None                            # refuse plaintext HTTP
    if url.endswith(".md") or "/" in url:      # repo-relative path
        return (f"https://raw.githubusercontent.com/{repo}/HEAD/{url.lstrip('./')}", False)
    return None


def fetch_linked_docs(repo: str, bodies: list[str], token: Optional[str],
                      max_docs: int = 2, max_chars: int = 40_000) -> list[str]:
    """Follow migration/upgrade doc links found in release notes; return their text."""
    seen: set[str] = set()
    out: list[str] = []
    for body in bodies:
        for text, url in _DOC_LINK_RE.findall(body):
            if not (_DOC_HINT_RE.search(text) or _DOC_HINT_RE.search(url)):
                continue
            resolved = _resolve_doc(repo, url)
            if not resolved or resolved[0] in seen:
                continue
            fetch_url, is_html = resolved
            seen.add(fetch_url)
            try:
                content = _get_text(fetch_url, token)
            except AnalyzerError:
                continue
            if is_html:
                content = _html_to_text(content)
            out.append(f"# Linked doc: {url}\n{content[:max_chars]}")
            if len(out) >= max_docs:
                return out
    return out


# Conventional in-repo migration-guide locations, tried when release notes don't
# link one (e.g. pydantic keeps its guide at docs/migration.md but never links it
# from the release body). Migration-specific files only, NOT full CHANGELOGs,
# which would flood the report with every version's churn.
_CONVENTION_DOC_PATHS = (
    "docs/migration.md", "docs/migrating.md", "docs/migration_guide.md",
    "docs/upgrading.md", "docs/migration/index.md",
    "MIGRATION.md", "MIGRATING.md", "UPGRADING.md",
)


def fetch_convention_docs(repo: str, token: Optional[str],
                          max_docs: int = 2, max_chars: int = 40_000) -> list[str]:
    """Try well-known in-repo migration-guide paths; return the text of any found."""
    out: list[str] = []
    for path in _CONVENTION_DOC_PATHS:
        raw = f"https://raw.githubusercontent.com/{repo}/HEAD/{path}"
        try:
            out.append(f"# Repo doc: {path}\n{_get_text(raw, token)[:max_chars]}")
        except AnalyzerError:
            continue
        if len(out) >= max_docs:
            break
    return out


# --------------------------------------------------------------------------- #
# Analysis
# --------------------------------------------------------------------------- #
def _extract_risk_lines(text: str) -> list[str]:
    lines = []
    for raw in text.splitlines():
        line = raw.strip().lstrip("#*-> ").strip()
        if len(line) < 6:
            continue
        if _BREAKING_RE.search(line) and not _NOISE_RE.search(line):
            lines.append(line)
    return lines


def _match_symbols(line: str, used: list[str]) -> list[str]:
    hits = []
    for sym in used:
        if not sym:
            continue
        if re.search(r"\b" + re.escape(sym) + r"\b", line, re.IGNORECASE):
            hits.append(sym)
    return hits


def analyze(ecosystem: str, package: str, from_version: str, to_version: str,
            used_symbols: Optional[list[str]] = None,
            github_token: Optional[str] = None) -> dict:
    used_symbols = [s.strip() for s in (used_symbols or []) if s.strip()]
    github_token = github_token or os.environ.get("GITHUB_TOKEN")

    # Drop the package's own name as a "used symbol", matching it floods the
    # report on every note that mentions the package (found via subagent test:
    # 14 of 24 express flags were bare "express" mentions).
    _pkg_names = {package.lower(), package.split("/")[-1].lower()}
    used_symbols = [s for s in used_symbols if s.lower() not in _pkg_names]

    try:
        repo = resolve_repo(ecosystem, package)
        resolve_error = None
    except AnalyzerError as exc:
        repo, resolve_error = None, str(exc)

    report = RiskReport(ecosystem=ecosystem, package=package,
                        from_version=from_version, to_version=to_version, repo=repo,
                        risk_score=0)

    if not repo:
        if resolve_error:
            report.notes.append(resolve_error)
        report.notes.append(
            "Could not resolve an upstream GitHub repo for this package; "
            "risk analysis is limited to registry metadata.")
        report.headline = "UNKNOWN: no changelog source found for this package."
        return report.to_dict()

    try:
        releases = fetch_release_notes(repo, from_version, to_version, github_token,
                                       package=package)
    except AnalyzerError as exc:
        releases = []
        report.notes.append(f"Could not fetch release notes: {exc}")
    if not releases:
        report.notes.append(
            "No GitHub releases found in that version range (project may tag "
            "differently or keep a CHANGELOG file instead).")

    seen: set[str] = set()

    def _ingest(text: str, source: str, symbols_only: bool) -> None:
        """Pull risk lines from a chunk of text into the report.

        symbols_only=True is used for long prose docs (migration guides): when
        the caller gave us symbols, only lines touching those symbols are kept,
        so a guide doesn't flood the report with boilerplate. Release notes are
        ingested in full (symbols_only=False)."""
        count = 0
        for line in _extract_risk_lines(text):
            if line in seen:
                continue
            matched = _match_symbols(line, used_symbols)
            if symbols_only and used_symbols and not matched:
                continue
            seen.add(line)
            severity = "deprecation" if _DEPRECATION_RE.search(line) else "breaking"
            report.items.append(RiskItem(
                severity=severity, summary=line[:280], affects_you=bool(matched),
                matched_symbols=matched, source=source))
            count += 1
            if symbols_only and count >= 25:
                break

    for rel in releases:
        _ingest(rel["body"], rel["url"] or f"release {rel['tag']}", symbols_only=False)

    # Follow migration/upgrade guides linked from the release notes, this is
    # where projects like pydantic and express hide the real breaking changes.
    docs_found = 0
    try:
        linked = fetch_linked_docs(repo, [r["body"] for r in releases], github_token)
        for doc in linked:
            doc_url = doc.splitlines()[0].replace("# Linked doc: ", "").strip()
            _ingest(doc, doc_url, symbols_only=True)
        docs_found += len(linked)
        # Fall back to conventional in-repo guide paths if no guide was linked.
        if not linked:
            conv = fetch_convention_docs(repo, github_token)
            for doc in conv:
                label = doc.splitlines()[0].replace("# Repo doc: ", "").strip()
                _ingest(doc, f"{repo}:{label}", symbols_only=True)
            docs_found += len(conv)
    except AnalyzerError as exc:
        report.notes.append(f"Could not fetch migration docs: {exc}")

    # NOTE: we deliberately do NOT scrape open GitHub issues for "migration
    # steps", a subagent test showed that produced irrelevant noise (e.g.
    # "Split the examples from this repo"). Precise, actionable migration steps
    # are the job of the paid LLM tier, which reasons over the guide text.

    # Deterministic risk score.
    breaking = [i for i in report.items if i.severity == "breaking"]
    yours = [i for i in report.items if i.affects_you]
    score = min(100, len(breaking) * 8 + len(report.items) * 2 + len(yours) * 20)
    report.risk_score = score

    if yours or breaking:
        report.notes.append(
            "Free-tier heuristic: symbol matches are keyword-based. They flag "
            "breaking-change notes that MENTION a symbol you use, they do NOT "
            "confirm your specific usage breaks. Expect over-flagging: a note may "
            "cite your symbol only as the safe replacement, or break a call "
            "signature you don't use. Treat each match as a candidate to verify.")

    if yours:
        report.headline = (
            f"REVIEW: {len(yours)} breaking-change note(s) mention symbols you use "
            f"({', '.join(sorted({s for i in yours for s in i.matched_symbols}))}). "
            f"Verify each against your actual usage; this heuristic can over-flag.")
    elif breaking:
        report.headline = (f"REVIEW: {len(breaking)} breaking change(s) in range, none "
                           f"matched to your listed usage; skim to confirm.")
    elif not (releases or docs_found):
        report.risk_score = 0
        report.headline = (
            "INCONCLUSIVE: no release notes or migration guide found for this "
            "version range (monorepo, a non-GitHub-Releases changelog, or unusual "
            "tags). Risk could NOT be assessed, do not treat this as safe.")
        report.notes.append(
            "Verify manually: this package's changelog wasn't retrievable via the "
            "GitHub Releases API or common migration-guide paths.")
    elif _version_key(to_version)[0] > _version_key(from_version)[0]:
        # Semver: a major bump is breaking by definition. Finding none means our
        # sources were too thin (e.g. a stub release body linking to docs we
        # couldn't reach), that's INCONCLUSIVE, never a green light.
        report.risk_score = max(report.risk_score, 25)
        report.headline = (
            "INCONCLUSIVE: MAJOR version bump but no breaking changes found in the "
            "available release notes; the real changelog is likely elsewhere. "
            "Verify manually, do NOT treat this as safe.")
        report.notes.append(
            "Major version bumps almost always include breaking changes (semver); "
            "finding none here usually means the changelog wasn't fully retrievable.")
    else:
        report.headline = "LOW: release notes in range show no breaking-change signals."

    # Surface the items that affect the caller first.
    report.items.sort(key=lambda i: (not i.affects_you, i.severity != "breaking"))
    return report.to_dict()


# --------------------------------------------------------------------------- #
# CLI smoke test
# --------------------------------------------------------------------------- #
def _main() -> None:
    p = argparse.ArgumentParser(description="Bump Doctor risk analyzer")
    p.add_argument("ecosystem", help="npm | pypi")
    p.add_argument("package")
    p.add_argument("from_version")
    p.add_argument("to_version")
    p.add_argument("--used", default="", help="comma-separated symbols your code uses")
    args = p.parse_args()
    used = [s for s in args.used.split(",") if s]
    try:
        report = analyze(args.ecosystem, args.package, args.from_version, args.to_version, used)
    except AnalyzerError as exc:
        report = {"error": "analysis_failed", "message": str(exc)}
    except Exception as exc:  # never surface a raw traceback to a calling agent
        report = {"error": "unexpected", "message": f"{type(exc).__name__}: {exc}"}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    _main()
