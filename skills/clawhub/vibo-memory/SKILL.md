# ViBo — memory + living archive + web-search savings + thread memory for AI agents

Use when the agent needs persistent memory (L1/L2/L3), a living document archive (.vibo: pack documents, search by meaning, answer questions), web-search savings (compress articles up to 96%), or thread memory (compress long conversations, restore details). Requires a valid ViBo license.

One skill. Four products:
1. 🧠 **Memory** — persistent memory with L1/L2/L3 encryption
2. 🌐 **Web Search Savings** — cut web-search context up to 96%
3. 💬 **Thread Memory** — compress long conversations, keep full history
4. 📦 **Living Archive** — pack documents into .vibo (up to 9× smaller), search by meaning, answer questions in milliseconds

## License (important!)

This skill is commercial. Before first use, activate it:

```bash
# Paid key:
python3 activate.py VIBO-XXXX-XXXX-XXXX-XXXX

# Or get a FREE 2-day trial by email (works from any install: ClawHub, n8n, site):
python3 activate.py --email you@example.com
```

Activation is one-time: one key = one machine. Re-activation on another computer is rejected by the server.

After activation, every skill run starts with a license check:

```bash
python3 check_license.py || exit 1   # 🔒 without license the skill doesn't work
```

**Tip:** if you downloaded the trial version, the key is already built in — just unpack and run. No manual activation needed.

**📄 License Agreement:** By downloading, installing, or using this skill, you agree to the **ViBo End User License Agreement** (see **EULA.md** in this package, also available at https://wwwvibo.com). It applies to all copies of the skill, however obtained — including copies forwarded or shared by others.

## 🧠 Product 1: Memory

ViBo is memory for AI agents: saves facts between sessions, finds them by meaning, and saves tokens. The agent gets only relevant facts, not the whole memory.

Three security tiers:
- **L1 (Public)** — visible to everyone: names, cities, tags
- **L2 (Private)** — visible only to the agent: notes, roadmap (encrypted with agent key)
- **L3 (Secret)** — visible only to the user: API keys, passwords. L3 NEVER gets into the LLM context — only a 🔒 placeholder.

### CLI

```bash
vibo --file memory.web seed               # demo memory
vibo --file memory.web find "query"       # search memory
vibo --file memory.web stats              # statistics
vibo --file memory.web usage              # REAL savings: tokens & money saved
```

### Adaptive mode (honest)

ViBo never costs more than no-ViBo:
- Big memory (10K+ facts) → **50-150× fewer tokens**
- Small memory (100 facts) → skill **stays silent** (no losses, no overhead)

## 🌐 Product 2: Web Search Savings

Web search results are huge (5-15K tokens per article). Dumping them all into the LLM context is expensive. ViBo compresses them first.

**Measured: 96.2% fewer tokens per article** (12,975 → 489 tokens).

```bash
python3 vibo_search.py <URL> "<topic>"   # compressed essence only
```

How it works:
1. **Compress** — removes HTML, navigation, ads, duplicates; keeps only paragraphs relevant to the query
2. **Rank** — picks the best 2-3 articles instead of all 10
3. **Cache** — repeated questions are answered from memory: 0 tokens

Agent rules for web search:
1. Before searching, check the cache for the same question.
2. After getting results, compress each article.
3. Save the compressed summary to cache.
4. Never send raw HTML or full pages to the LLM.

## 💬 Product 3: Thread Memory

Long conversations (100K+ tokens) cost a fortune when sent whole to the LLM. ViBo keeps the FULL history in a `.web` file, sends only a COMPRESSED summary to the model, and can restore details on demand.

```bash
vibo dialog add "client asked about pricing" --role user --topic pricing
vibo dialog compress                # old messages → summary (-70% tokens)
vibo dialog ask "what did we agree 3 days ago?"   # restore details
vibo dialog context                 # compressed context for the LLM
```

**Measured: 72% fewer tokens** on the conversation, full history kept in the file — nothing is lost, details are one query away.

## 🧠 Super Memory

Memory never gets lost — and savings grow with it.

ViBo uses a two-level memory ("desk + archive"):
1. **Active memory** (memory.web) — what is needed right now. Search goes only through it → fast and cheap.
2. **Archive** (memory_archive.web) — everything old that was ever saved. Not involved in search, but available on request.

**Key point:** savings are counted from ALL memory (active + archive). Without ViBo the agent would load everything. With ViBo — only the relevant part. The bigger the archive — the BIGGER the savings.

```bash
# Memory maintenance (automatic weekly):
python3 vibo_memory_tools.py stats      # memory health
python3 vibo_memory_tools.py archive 30 # old entries → archive
python3 vibo_memory_tools.py cleanup    # duplicates and garbage → remove
```

**Philosophy:** memory is like a desk. On the desk — what's relevant; in the drawer — everything else. The desk is always fast, the drawer is always full. Nothing is lost — and savings grow with every saved fact.

## Agent rules (general)

1. Always check the license before using (check_license.py).
2. Write important facts about the user: preferences, projects, decisions.
3. No duplicates: before saving, search for similar facts.
4. L3 only with user permission: encrypt API keys with L3, never output them.
5. Web search: compress + cache before sending results to the LLM.

### SHOW SAVINGS IN EVERY ANSWER (important!)

After every memory search or web compression, tell the user what ViBo saved, right in your reply:

```
💾 ViBo: saved 12,486 tokens ($0.0017) on this search — 96.2% fewer than without ViBo.
```

Examples:
- After memory search: "💾 ViBo: 1,038 tokens saved (67%) — only relevant facts."
- After web compression: "💾 ViBo: 79,737 tokens saved (99.4%) — article compressed."
- If nothing was saved (small memory): "🤷 ViBo: memory is small yet — savings grow as facts accumulate."

The user must SEE the savings immediately, without running any commands.

### Thread Memory for long conversations (important!)

When a conversation gets long (more than ~50 messages or big context), compress it instead of sending everything to the LLM:

```bash
vibo dialog add "user asked X, we agreed Y" --role assistant --topic "topic"
vibo dialog compress              # old messages → summary (-70%)
vibo dialog context               # compressed context for the LLM
```

Keep the FULL history in thread.web — never delete it. When the user asks "what did we discuss 3 days ago?" — restore details from the file. Always tell the user the savings: "💾 ViBo: conversation compressed -72% (12,340 tokens)."

## Skill structure

```
vibo_skill.zip
├── SKILL.md                 # this file
├── INSTALL.md               # integration guides
├── activate.py              # one-time activation (buyer)
├── check_license.py         # check on every run
├── vibo_use.py              # CLI (add/find/usage/stats)
├── vibo_web.py              # web search savings (compress + cache)
└── vibo/                    # protected core
```

## See your real savings

Every ViBo operation (memory search + web compression) records how many tokens it saved. Run:

```bash
vibo --file memory.web usage
```

You'll see your real, measured savings — the difference between "without ViBo" (all memory + full articles) and "with ViBo":

```
📊 ViBo: your real savings
=============================================
📈 Operations via ViBo: 17
💾 Tokens saved: 8,412,584
💰 Savings (DeepSeek): $1.18
=============================================
```

Without ViBo you'd pay for ALL memory and FULL articles. With ViBo: only relevant facts + compressed articles. Raw log: `vibo_usage.jsonl` — one line per operation (query, tokens saved, %).

The more facts you accumulate and the more web pages you compress, the bigger the savings grow.

## Installation & integration

See **INSTALL.md** — guides for Hermes, OpenClaw, LangChain, CLI, Python API, and agent instructions.

## Buy

Buy a license: **https://wwwvibo.com** — $5/month (Stars or USDT). After payment you get a key VIBO-XXXX-XXXX-XXXX-XXXX for one machine.


## 📦 Product 4: Living Archive

Documents are dead weight in regular archives. ViBo makes them ALIVE: pack documents into a single .vibo file (own format), search them by meaning, and get answers in milliseconds.

```bash
vibo archive pack ./documents -o archive.vibo   # 98 files (9 MB) → 808 KB
vibo archive search archive.vibo "company requisites?"   # exact fragment
vibo archive list archive.vibo                  # documents inside
vibo archive unpack archive.vibo -o restored    # restore with paths
```

- **Measured:** 9 MB of documents → 808 KB archive; up to 99.7% token savings.
- **Integrity:** pack → unpack returns ALL files (216/216 tested), paths and extensions preserved.
- **Formats:** .md, .txt, .docx, .pdf (text), .xlsx, .pptx, images (OCR). Junk (configs, binaries) is filtered automatically.
