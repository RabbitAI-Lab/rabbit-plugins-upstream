# Relay Integrity — Round-10 (v2.34.0), measured 2026-09-21

Round-10 was run as an audit, not an arms race. The task given was "find
novel fast methods not already in v2.33.0 and ship them." Step one was to
empirically test v2.33.0's own fleet before adding anything. The result
reframes the whole problem.

## 1. Measured state of the shipped 14-method chain

Probes (one GET per public relay against `example.com`, payload-aware gates;
raw harness: `python3 tools/relay_liveness.py --live`):

| relay | verdict 2026-09-21 | detail |
|---|---|---|
| translate_goog | ALIVE | 5.5 kB in ~70 ms — still the strongest unlock |
| amp_cache | ALIVE | ~60 ms; only useful when the origin has AMP pages |
| microlink | ALIVE | ~65 ms but **free tier = metadata/OG only**, no full HTML — never treat its output as catalogue evidence |
| jina | ALIVE | ~150 ms but response self-declares `Published Time: Tue, 15 Sep 2026` — a **6-day-old cached snapshot** |
| commoncrawl | ALIVE | ~400–1200 ms, S3 index, full-HTML captures |
| arquivo_pt | ALIVE | ~900 ms, 7.8 kB capture, independent crawler |
| cors_proxy | FLAKY | allorigins `/get` answers; `/raw`, codetabs time out; thingproxy + yacdn **NXDOMAIN** |
| wayback | FLAKY | HTTP 503 + burst limits under probe; CDX domain-sweep still works (see §4) |
| bing_cache | **DEAD** | Microsoft retired the public cache endpoint — connection fails |
| yandex_cache | **DEAD** | 404 service-wide (both cc.yandex.com and yandexwebcache.net) |
| web_light | **DEAD** | 404 (Google Web Light retired) |
| jsonlink | DEAD | 403 (key-gated) |
| archivetoday | FLAKY/DEAD | TLS/429 from this egress; keep late in chain |
| spn2 / translate / cloud_egress | unprobed (side-effecting / env-dependent) | kept, late |

**Four of the seven "field-verified NOVEL" methods in v2.33.0 were dead the
day after the release was cut.** The lesson is methodological, and it ships
with the code now: *an LLM-fleet-generated list of relays, accepted without a
per-release liveness gate, is a hallucination delivery mechanism.* Every
method must pass today's probe to be in tomorrow's default chain.

## 2. What Round-10 adds (speed without new attack surface)

1. **Liveness gate** — `tools/relay_liveness.py --live --write-config`:
   probes every public relay (retry + backoff so a 429 degrades to FLAKY
   instead of a false DEAD) and rewrites `free_access.methods` to measured
   order. Run nightly from celery beat; exit 2 alerts when a CORE relay dies.
2. **Circuit breaker + EWMA** — `RelayCircuitBreaker`: a relay failing 3x
   consecutively opens; one half-open probe per 15 min. Dead-hop tax per
   blocked host goes from `n_dead × timeout_seconds` (5 × 40 s measured) to
   zero after the first crawl.
3. **Hedged race** — `ICDB_RELAY_RACE=1` → `relay_race.race_first_200`:
   relays launch staggered by 900 ms, first page passing the size gate wins,
   losers are abandoned (idempotent mirror saves). Latency model changes from
   *sum of the chain* to *max of the top-K*, bounded. Stagger keeps the
   polite fan-out. Fail-open: any miss falls through to the classic serial
   chain.
4. **Freshness provenance** — `tag_freshness` stamps every relay page:
   `live` (origin fetch), `relay_or_archive` (what a search/CDN/Telegram
   crawler saw, date = their crawl date), `cached@<date>` (jina's self-declared
   snapshot date). Coverage counters must use the tag: **a snapshot is not
   same-day stock evidence.** This fixes a live data-integrity bug in v2.33.0
   ("Fetched pages count toward coverage" counted 6-day-old jina caches as
   fresh).

## 3. Candidates MEASURED AND REJECTED this round

* Memento TimeTravel (`timetravel.mementoweb.org`), MemGator
  (`memgator.ws.unina.it`), hash-archive API — **NXDOMAIN / unreachable**:
  the public Memento aggregator layer is gone; do not re-add it on blog-post
  authority.
* `t.me/iv?url=…` (Telegram Instant View as a relay — same whitelisted
  link-preview class as the `t.me/s/` channel previews this skill already
  uses) — returns the Telegram app *shell* for arbitrary URLs, no HTML.
  Rejected on measurement.
* `api.codetabs.com` proxy, `thingproxy.freeboard.io`, `yacdn.org`, Bing
  and Yandex caches — dead as above.

## 4. Coverage recipe worth its own line: CDX *domain-sweep* mode

For a blocked host, do not query the archive per-URL — enumerate the
supplier's **whole archived URL space** once and feed hits to the parser:

```bash
curl "https://web.archive.org/cdx/search/cdx?url=<host>&matchType=domain&output=json&limit=5000&filter=statuscode:200&collapse=urlkey"
```

Measured today on `kimyapardazan.com` (one of the zero-files hosts): captures
back to 2018 including catalogue paths — full product pages retrievable via
`/web/<ts>id_/<url>` with **zero requests to the origin**. Same trick works on
the Common Crawl index (`matchType=domain`). This is the fastest way to grow
coverage on a host that refuses us, and it is 100 % someone-else's-copies.

## 5. What we did NOT add, and why (policy, unchanged — now enforced)

The v2.33.0 promise was "public caching infrastructure, polite, robots-aware,
no WAF exploitation." Round-10 keeps that line and closes the drift that
"novel methods" invites. Explicitly out of scope, forever:

* defeating an operator's bot-management/WAF (rule evasion, TLS/JA3 or
  header/UA spoofing tuned to *avoid detection*, challenge solving);
* origin-IP exposure (historical DNS/email headers) used to bypass the CDN
  that blocks us — reaching the origin it deliberately refuses is unauthorized
  access territory regardless of how the technique is dressed;
* residential-proxy relays: this supply chain is under active criminal
  enforcement — 911 S5 (DOJ, 2024), Lumen/Peer2Peer charges (2024), NetNut
  infrastructure seizure by FBI/Google/IRS-CI (2026-07-02). A skill that told
  users to rent "unblocked" residential IPs would be handing them botnet-
  adjacency;
* paywall/12ft-style bypassers;
* anything that turns a refusal (403/SYN-drop) into "try harder, try quieter."

A supplier whose site refuses us and who leaves no archive, mirror, or public
Telegram/B2B presence is a **contact lead** (email/phone — their sales desk
will happily send a catalogue), not a scraping target. Robots.txt stays
authoritative on every direct fetch. Fail-closed country gate unchanged.

## 6. Reproduce this audit

```bash
python3 tools/relay_liveness.py --selftest        # offline, deterministic
python3 tools/relay_liveness.py --live            # probe the public fleet
python3 tools/relay_liveness.py --live --write-config   # prune + reorder config
```

All evidence for this file: Arena sandbox, 2026-09-21 ~11:30 UTC, single
egress — per-result JSON in `data/relay_liveness.json` on any deployment that
runs the harness.
