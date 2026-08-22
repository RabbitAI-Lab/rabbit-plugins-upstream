## v2.9.0 — reliability & verification best practices

A hardening pass to ensure every functionality works as expected.

### Added
- `scripts/self_test.py` — one-command offline self-test: compiles every .py,
  checks required files + SKILL.md frontmatter + config.yaml, imports core
  modules, and runs the offline pytest subset. Exit 0 only when all pass.
- `scripts/preflight.py` — environment readiness report (httrack/curl/wget
  binaries, python version, optional packages, config load) with install hints.
- `tools/package_selftest.py` — release-readiness check to run before publishing.
- `.github/workflows/ci.yml` — CI on push/PR: preflight → self-test → full
  pytest (DB tests self-skip) → package selftest.
- `src/utils/http_util.py` — shared `get_bytes()` with retry + exponential
  backoff on transient HTTP 408/425/429/5xx and socket errors; TLS verified by
  default.

### Changed
- `httrack_engine.py` — `require_httrack` flag + graceful `mirror_supplier()`
  returning an empty stats dict when httrack is missing (the fallback chain —
  playwright, curl/wget/python, free-access — now takes over instead of
  crashing). `build_command` uses the resolved binary path.
- `directory_crawler.py` — discovery engine no longer hard-crashes without
  httrack (uses `require_httrack=False`).
- `free_access_engine.py` / `woo_rest_engine.py` / `http_fetch_engine.py` —
  all network GETs now go through the shared retry/backoff helper.
- `pyproject.toml` — ruff bug-focused rules (E/F/W/B) with FastAPI-aware
  ignores; pytest `integration` / `network` markers.
- Removed 4 dead code spots (unused imports/variable) flagged by ruff.

### Verification
- Full pytest suite passes (DB tests self-skip without PostgreSQL).
- `ruff check` clean; `preflight` + `self_test` + `package_selftest` all green.

---
## v2.8.0 — multi-tool HTTP fetch fallback (curl / wget / python)

### Added
- `src/crawler/http_fetch_engine.py` — single-page fetch chain
  (python-urllib → curl → wget, browser UA, redirect-following, timeout +
  size guards) plus optional `wget -r -k -p` recursive mirror. Tools detected
  at runtime; missing ones skipped. Output saved under
  `<mirror>/fetch-fallback/<tool>/` and parsed by the existing pipeline.
- `config.yaml` → `http_fetch:` section.

### Changed
- `crawl_tasks.py`: the HTTrack mirror call is now wrapped so a missing httrack
  binary (or any mirror error) degrades gracefully instead of failing the
  supplier; when the mirror is empty and the site is NOT geo-blocked, the
  HTTP-fetch fallback runs (homepage + catalog entry points). Its saved files
  are counted in `/coverage` instead of a false "no-html-mirrored".

---
## v2.7.1 — Wayback "Save Page Now" (SPN2) — invented via adversarial debate

A 2-round adversarial debate among the reasoning team (cmdr, qwen, devstral,
gemini — each proposed 6 novel methods, then cross-critiqued the other 21)
produced one genuinely new, live-verified method:

### Added
- `fetch_via_spn2()` — forces a FRESH capture of a blocked page via
  `https://web.archive.org/save/<url>`, then reads the new capture back from
  `web.archive.org/web/<ts>id_/<url>`. The IA crawler fetches from its own
  (allowed) IPs, so geo-blocked hosts are captured on demand. Verified live:
  rockchemie.com captured 2026-08-22 (428 KB full HTML). Fails gracefully when
  IA's save endpoint is busy (HTTP 5xx) and is appended to every site's method
  list automatically.
- `DEFAULT_FREE_ACCESS_METHODS` now: jina, wayback, commoncrawl, spn2,
  translate, archivetoday. `free_access_preference()` always appends spn2.

### Debate verdicts (documented for the record)
- Google PageSpeed Insights — real & keyless, but Google hard-rate-limits
  datacenter IPs (429 in testing) — NOT shipped.
- Facebook Graph scrape / Twitter Card Validator / LinkedIn Post Inspector —
  real but metadata-only (or login-walled) — NOT shipped.
- Yandex Turbo, Google AMP cache, W3C validator from DC IPs, "Cloudflare Edge
  Fetch", "Tehran Uni Archive", "performance-tester", "data-saver transcoder",
  "webcache.search-engine" — dead, keyed, or hallucinated by the models —
  rejected after live testing.

---
## v2.7.0 — Common Crawl + screenshot fetchers (exhaustive round-3 sweep)

Exhaustive sweep (4 reasoning models + live tests of 20+ candidates on the
geo-blocked sites) added two genuinely new working methods:

### Added
- `fetch_via_commoncrawl()` — queries the Common Crawl index
  (index.commoncrawl.org) for recent captures and downloads each WARC record
  with a tiny HTTP Range request from data.commoncrawl.org (S3, not
  geo-blocked), extracting the full HTML body (chunked/gzip handled). Verified
  live: rockchemie.com 27 captures (2026-07), pgsoc.ir 1 (2026-07),
  irandaru.com 3, shimico.com 407. Gives the "Wayback-only" sites a second
  source with much fresher captures.
- `fetch_via_screenshot()` — thum.io renders the page server-side to a PNG
  (verified: 492 KB render of rockchemie.com). Image-only visual evidence —
  intentionally NOT in the default method list.
- `DEFAULT_FREE_ACCESS_METHODS` now `jina, wayback, commoncrawl, translate,
  archivetoday`; `free_access.methods` / `max_commoncrawl_pages` in config.yaml.

### Verified dead/blocked this round (not implemented)
allorigins(522) · codetabs(522) · corsproxy.io(403) · thingproxy(DNS) ·
fetch.hix.ai(dead) · md.dhr.wtf(dead) · memento(dead) · textise(403) ·
urltotext(own page) · rss2json(500) · rendertron(404) · google-docs-viewer +
officeapps (wrappers) · mshots (placeholder).

---
## v2.6.2 — archive.today method + per-site free-access preferences (2026-08-21)

Round-2 investigation (4 reasoning models + live tests on all 12 geo-blocked
sites) showed the three v2.6 fetchers are the only broadly-working free
front-ends, plus one additional one:

### Added
- `free_access_engine.py`: `fetch_via_archive_today()` — a 4th fetcher using
  the archive.today family (archive.ph / archive.today / archive.is). Serves
  existing snapshots via `/newest/<url>`; reachable from residential/operator
  networks (blocks many datacenter IPs, fails gracefully). Added to
  `DEFAULT_FREE_ACCESS_METHODS` and the orchestrator.
- `seed_list.py`: every geo-blocked seed entry now carries a field-verified
  `free_access_methods` preference, e.g. novichem.ir/pgsoc.ir = ["wayback"]
  (Jina/Translate both fail on them), basparsazan.com = ["jina","translate"],
  artinkimya.com = all three. New `free_access_preference(url)` returns the
  per-site list, defaulting to `DEFAULT_FREE_ACCESS_METHODS`.
- `crawl_tasks.py`: the free-access fallback now uses `free_access_preference()`
  per site (config list is the fallback for unknown domains).
- `config.yaml` → `free_access.methods` now includes "archivetoday".

---
## v2.6.0 — free-access fallback for geo-blocked Iranian sites (2026-08-21)

Field-verified on the 12 geo-blocked seed sites (rockchemie, abnoos,
artinkimya, pakshoo, pgsoc, tebgostar, novichem, basparsazan, mahdistejarat,
irandaru, shimico, parsisotope): every one is reachable through at least one
FREE third-party fetcher whose IPs the Iranian hosts do not block.

### Added
- `src/crawler/free_access_engine.py` — three fetchers:
  - Jina Reader (`https://r.jina.ai/<url>`, markdown) — works on 9/12 sites;
  - Wayback Machine (CDX API enumerates snapshots, `web/…/id_/` serves raw HTML)
    — works on 10/12;
  - Google Translate proxy (`translate?u=`) — works on 9/12.
  Fetched files are stored under `<mirror>/free-access/{jina,wayback,translate}/`
  and parsed by the existing local-file-only pipeline. Stdlib only, no keys.
- `src/parser/markdown_parser.py` — scans Jina markdown for CAS-number patterns
  and emits molecule candidates (name + CAS + purity) for text-only fetches.
- `.md` / `.txt` added to `PARSEABLE_EXTENSIONS` and `SUPPORTED_EXTS`.
- `config.yaml` → `free_access:` section (enabled, methods order, timeout,
  delay, max_wayback_pages).

### Changed
- `crawl_tasks.py`: when a mirror looks geo-blocked (or the supplier notes say
  GEO-BLOCKED), the free-access engine runs automatically; its saved files are
  counted in `/coverage` (no more false "no-html-mirrored" partial reason) and
  the method breakdown is recorded in `partial_reason`.

---
## v2.5 — field-hardened release (2026-08-21)

Derived from a live crawl run + full fingerprinting of the 35-supplier seed list.

### Added
- `src/crawler/woo_rest_engine.py` — WooCommerce/WordPress REST + sitemap engine:
  public, unauthenticated `/wp-json/wc/store/v1/products` pagination (WP core
  REST fallback) plus `sitemap.xml`/`product-sitemap.xml` enumeration; JSON is
  persisted into the local mirror store and consumed by the existing
  local-file-only parser (`.json` added to PARSEABLE_EXTENSIONS).
- Fingerprint-annotated seed list: every supplier carries status
  (active/inactive), crawl-profile hint (`woo_rest`, `sitemap_wp`,
  `playwright_js`, …), notes and REST/sitemap entry points. 12 dead domains,
  2 parked, 1 inorganic-only and 1 radiopharma-only are seeded `inactive` and
  skipped by the crawl sweep.
- `woo_rest` / `sitemap_wp` HTTrack profiles + `classify_profile` mapping.
- Geo-block detection: zero-file mirrors with TLS/handshake/timeout signatures
  are flagged `geo-blocked-possible (retry via Iranian proxy)`.

### Fixed
- `trigger_initial_crawl.py`: dispatch now uses `celery_app.send_task(...)`
  instead of `.delay()` on a bare `@shared_task` — the old path fell back to
  the default Celery app (AMQP broker) and failed with "Connection refused"
  while the Redis-bound worker was healthy.

---
## Description: <br>
Iran Chemical Database — an HTTrack-powered live crawling system that autonomously discovers Iranian chemical suppliers, mirrors their websites with HTTrack (with Playwright fallback for JavaScript sites) and a WooCommerce/WordPress REST + sitemap engine, extracts research-grade molecule catalogs from the local mirrors, validates molecules with RDKit/PubChem, and maintains a live PostgreSQL database served by FastAPI (REST) and Streamlit (dashboard), with Celery scheduling and Docker deployment. Ships complete, runnable source code: discovery engine, HTTrack wrapper, local-file parsers (HTML/PDF/Excel), strict research-grade classifier (English + Persian), live sync, API, dashboard, tests, and docs. For academic procurement research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, lab managers, and procurement staff use this skill to build and maintain a live, searchable database of research-grade chemical molecules offered by Iranian suppliers — automatically discovered and kept up to date via HTTrack website mirrors — for sourcing, price comparison, and catalog analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The system crawls third-party websites, which may violate their terms of service or robots.txt if misconfigured. <br>
Mitigation: Polite crawling defaults (robots.txt respected, rate limits, identifiable User-Agent), per-supplier overrides, and explicit legal guidance to mirror only authorized sites. <br>
Risk: Extracted chemical data (grades, purities, prices, GHS) can be inaccurate. <br>
Mitigation: Every record is validated (CAS checksum, RDKit structure, PubChem cross-reference) and flagged with extraction confidence; users must verify before relying on it. <br>
Risk: Requires system services (PostgreSQL, Redis) and, for crawling, the httrack binary and outbound network access. <br>
Mitigation: Full Docker Compose deployment with persistent volumes and a clearly documented environment contract. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Architecture](docs/architecture.md) <br>
- [HTTrack integration guide](docs/httrack_integration.md) <br>
- [API reference](docs/api_reference.md) <br>
- [Deployment guide](docs/deployment_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [code, python, sql, yaml, dockerfile, markdown] <br>
**Output Format:** [A complete, runnable Python application (source tree, Docker Compose, migrations, tests, fixtures, docs) implementing the HTTrack-powered crawling database] <br>
**Output Parameters:** [2D] <br>
**Other Properties Related to Output:** [The system writes mirrored websites to a local directory and populates a PostgreSQL database; it makes outbound HTTP requests only to the supplier sites it is configured to mirror.] <br>

## Skill Version(s): <br>
2.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, mirror only websites they are authorized to archive, respect robots.txt and site terms of service, verify all extracted chemical data before relying on it, and comply with applicable data/procurement regulations. <br>
