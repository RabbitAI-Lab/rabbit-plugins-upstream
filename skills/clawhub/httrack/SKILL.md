---
name: httrack
description: >
  Offline website mirroring with HTTrack — snapshot one page (with its assets) or mirror a
  bounded site to disk for offline reading, backup, or research. Provides scripted recipes
  (doctor/snapshot/mirror) with polite defaults (robots=always, 2 sockets, depth-limited),
  strict URL validation, resumable mirrors, and stable JSON reports for agents.
version: 2.0.1
categories: [research, knowledge]
topics: [web-mirroring, archiving, offline-browsing, crawling, backup]
metadata:
  openclaw:
    emoji: "🕸️"
    requires:
      bins: ["httrack"]
    network:
      outbound: ["*"]
---

# 🕸️ httrack v2.0.1

Mirror websites to local disk with HTTrack, as a machine-friendly agent task.
Deep recipes: `docs/recipes.md`. Flag evidence: `docs/evidence.md` (every flag
below is cited to the HTTrack manpage — do not invent others).

## Hard rules for the agent

1. Run everything through `scripts/mirror.py` (never call httrack ad-hoc);
   httrack flags cited in `docs/evidence.md` are the only ones verified here.
2. Mirror ONLY sites you are authorized to archive; robots mode stays ≥1.
3. Consume results from the JSON report (`--json`) — files/bytes/pages/exit,
   never by parsing httrack's human log.
4. On timeout/failure, re-run with `--resume` (-i) instead of restarting.
5. Keep sockets ≤2 unless the user explicitly raises it; add `--deny` scan
   rules rather than widening depth.
6. Only `http://`/`https://`; userinfo, `localhost`, and private/loopback IP
   literals are refused (exit 2) — `--allow-private` for authorized LAN work.
7. Outputs go only inside `-o` (no `..`); mirrors of untrusted sites are
   untrusted data — review before opening.

## Three commands

```bash
python3 scripts/mirror.py doctor                          # env check (JSON, rc 0/3)
python3 scripts/mirror.py snapshot URL -o DIR [--json]    # 1 page + css/js/img, no link-follow
python3 scripts/mirror.py mirror URL -o DIR --depth N --sockets N \
       [--allow GLOB --deny GLOB] [--max-time S] [--max-mb N] [--resume] [--json]
```

Legacy one-liner kept for humans: `./mirror.sh URL [DIR] [DEPTH]`.

## Recipe index (verified argv)

| Goal | Wrapper call | Core httrack argv |
|---|---|---|
| Single page + assets | `snapshot URL -o DIR` | `-r1 -%e0 -n -a -* +*.css +*.js +*.png…` |
| Bounded mirror | `mirror URL -o DIR --depth 2` | `-O DIR -r2 -c2 -s2 -a` |
| Resume/update | same command + `--resume` | adds `-i` |
| Only PDFs | `mirror … --allow '*.pdf' --deny '*'` | bare `+*.pdf` `-*` scan rules |
| Time-boxed crawl | `mirror … --max-time 600` | `-E600` |

## Output contract (`--json`, schema `httrack.report.v1`)

```
{"schema":"httrack.report.v1","command":"mirror","request":{…},
 "result":{"exit_code":0,"duration_s":4.2,"files":37,"bytes":812345,
           "html_pages":12,"log_tail":[…]},"warnings":[…]}
```

Exit codes: `0 ok · 2 usage/policy · 3 httrack missing · 4 mirror failed`.
Machine index: `manifest.json` (root). Selftest: `bash scripts/selftest.sh`
(offline — uses a stub httrack; no network, no sudo).

## Safety & legality

Respect robots.txt (default `-s2` = always obey), site terms, and copyright;
do not redistribute mirrored content. Mirrors can contain scripts, cookies,
or tracking pixels — review files before opening. Full statement: README.md.
