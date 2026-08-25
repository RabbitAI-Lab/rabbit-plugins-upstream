---
name: httrack
description: "Offline website mirroring and web archiving with HTTrack. Mirror a website (HTML, assets, links) to local disk for offline browsing, backup, or research — with recipes for depth-limited crawls, single-page snapshots, and incremental mirror updates."
version: 1.0.0
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

# 🕸️ httrack

**Mirror any website to local disk with HTTrack.**

HTTrack is a mature open-source website copier. This skill turns it into an
agent-friendly task: give it a URL and it returns a complete offline copy of
the site — HTML, images, stylesheets, and links — that can be browsed with no
network connection.

## What to use it for

- Archiving a page/site for offline reading or as evidence
- Saving documentation, references, or course material before it changes
- Building a local corpus for later search/analysis
- Snapshotting a site at a point in time

## Requirements

- `httrack` binary. Debian/Ubuntu: `sudo apt install httrack`
- Outbound network access to the site(s) you mirror

## Quick start

```bash
# full mirror of a site, 2 links deep, 2 parallel connections
httrack "https://example.com" -O ./mirror -r2 -c2

# single page only
httrack "https://example.com/page.html" -O ./snapshot -r0

# use the safe wrapper included with this skill
./mirror.sh "https://example.com" ./mirror 2
```

## Common flags

| Flag | Meaning |
|---|---|
| `-O DIR` | output directory |
| `-rN` | recursion depth (0 = single page) |
| `-cN` | number of parallel connections |
| `--robots=1` | obey robots.txt |
| `-%v` | verbose progress |
| `-i` | continue an interrupted mirror |
| `-Y` | update an existing mirror (incremental) |
| `-A "*.pdf,*.zip"` | only fetch certain file types |
| `-F "user-agent"` | set a custom user agent |

## Safety & legality

- Only mirror sites you are authorized to archive.
- Respect robots.txt and the site's terms of service.
- Mirrored content may be copyrighted — do not redistribute it.
- Keep connection count and depth low to avoid hammering servers.
- Review downloaded files: a mirror can contain scripts, cookies, or pages
  that were not intended for you.

## Files

- `SKILL.md` — this guide
- `mirror.sh` — safe wrapper with sane defaults
- `README.md` — permissions, security & privacy, verification hash
