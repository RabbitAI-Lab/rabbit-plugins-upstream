# README

**klyc-pmm** — AI agent memory system with client-side encryption, blind cloud storage, and one-click talisman recovery.

## Why

AI agents wake up fresh every session. KLYC-PMM gives them memory that survives restarts, workspace resets, and migrations — encrypted, searchable, and recoverable from a single URL.

## Install

```bash
skillhub install klyc-pmm
```

Or manual:

```bash
git clone <repo> && cd klyc-pmm && ./pmm_watch.sh init
```

## 3 Commands You'll Use Daily

```bash
./pmm_watch.sh push "title" "what was decided"     # save a conclusion
./pmm_watch.sh search "keyword"                    # find past decisions
./pmm_watch.sh search-yaochi "keyword"             # search cloud memory
```

## Recovery (when everything is lost)

```bash
./pmm_recover.sh https://kunlunyaochi.com/klyc-pmm/YOUR_TOKEN
```

No dependency. Any AI agent with `curl` can do this.

## Docs

- [SKILL.md](./SKILL.md) — full usage guide
- [SECURITY.md](./SECURITY.md) — threat model & encryption design
- [CHANGELOG.md](./CHANGELOG.md) — version history
- [CONTRIBUTING.md](./CONTRIBUTING.md) — how to contribute

## License

MIT-0 — do whatever you want, no attribution required.
