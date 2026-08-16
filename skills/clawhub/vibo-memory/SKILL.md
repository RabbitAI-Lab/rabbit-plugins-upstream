# ViBo — memory + living archive + web-search savings + thread memory for AI agents

Use when the agent needs persistent memory (L1/L2/L3), a living document archive (.vibo: pack documents, search by meaning, answer questions), web-search savings (compress articles up to 96%), thread memory (compress long conversations, restore details), or a privacy layer that masks secrets before they reach any LLM (ViBo Proxy). Requires a valid ViBo license. Requires **Python 3.11** (the package ships compiled CPython 3.11 modules). Use ONLY with the user's explicit consent: ViBo persists facts, thread history, web summaries and document archives locally — tell the user what will be stored and how to delete it before first use.

One skill. Five products:
1. 🧠 **Memory** — persistent memory with L1/L2/L3 encryption
2. 🌐 **Web Search Savings** — cut web-search context up to 96%
3. 💬 **Thread Memory** — compress long conversations, keep full history
4. 📦 **Living Archive** — pack documents into .vibo (up to 9× smaller), search by meaning, answer questions in milliseconds
5. 🛡️ **Privacy Layer (ViBo Proxy)** — encrypt secrets and mask them (`🔒[name]`) before prompts reach any LLM

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

**Tip:** the trial key is issued by email — run `python3 activate.py --email you@example.com` and the 2-day trial activates automatically. There is no built-in free key.

**📄 License Agreement:** By downloading, installing, or using this skill, you agree to the **ViBo End User License Agreement** (see **EULA.md** in this package, also available at https://wwwvibo.com). It applies to all copies of the skill, however obtained — including copies forwarded or shared by others.

## 🤖 First-run setup (automatic — no menus for the client)

Do NOT ask the client to choose modules from a menu. On the first run after activation, the agent enables everything by default and tells the user in one line:

> ✅ ViBo is on: memory, web-search savings, thread memory, living archive. Everything is stored locally on this machine. Tell me "turn off X" anytime to disable a module.

**Enable automatically, without questions:**
- 🧠 **Memory** — search before answering (`vibo find`), save important facts (`vibo add`)
- 🌐 **Web Search Savings** — compress articles before sending them to the LLM
- 💬 **Thread Memory** — compress long conversations, keep full history
- 📦 **Living Archive** — pack/search/unpack documents on request

**Privacy Layer (ViBo Proxy) — at most ONE question:**
- The proxy needs Docker + an upstream LLM API key, so the agent checks `docker --version` first:
  - Docker present → ask ONE yes/no question: *"Enable secret protection (ViBo Proxy)? (yes/no)"*
  - Docker absent → skip the question and mention: *"Secret protection can be added later with one command (see vibo-proxy/INSTALL.md)."*
- If the user later says "turn off memory", "turn off the proxy", etc. — disable that module and tell them how to re-enable it.

## 🔒 Privacy, consent, retention & deletion (read first)

Everything ViBo stores stays **on your machine** — no cloud sync, no telemetry, no external data sharing.

**Where data is stored (all local) and how to delete it:**

| What | Local file | Delete |
|---|---|---|
| Memory facts (L1/L2/L3) | `memory.web` | `vibo forget "label"` · `vibo wipe --yes` |
| Memory archive | `memory_archive.web` | `vibo wipe --yes` (or remove the file) |
| Memory sidecar | `memory.web.vec` | removed automatically by `vibo wipe` |
| Thread history | `thread.web` | remove the file |
| Web-search cache | `/tmp/vibo_web_cache.json` | remove the file |
| L3 password / agent key | `~/.vibo/user.key`, `~/.vibo/agent.key` | remove the files |
| License + client id | `vibo_license.dat`, `vibo_client.id` (next to the skill) | see EULA.md |

**Consent, retention, deletion rules:**
- **Ask for explicit user consent** before persisting user facts, conversation history, web summaries, or document archives. Do not store on autopilot.
- Facts persist **until deleted** (no automatic expiry for L1/L2; memory is auto-archived to `memory_archive.web` on the weekly maintenance).
- **Secrets:** use the L3 flow only (`vibo add ... --level L3`) — encrypted (AES-256-GCM) with the user's password, never output, never sent to the LLM.
- To remove: `vibo forget "label"` deletes one fact; `vibo wipe --yes` deletes all memory (active + archive + sidecar).
- If you handle confidential, regulated, private or sensitive data — review this section before installing, and keep the memory/web cache local to an environment the user controls.

## 🧠 Product 1: Memory

ViBo is memory for AI agents: saves facts between sessions, finds them by meaning, and saves tokens. The agent gets only relevant facts, not the whole memory.

Three security tiers:
- **L1 (Public)** — visible to everyone: names, cities, tags
- **L2 (Private)** — visible only to the agent: notes, roadmap (encrypted with agent key)
- **L3 (Secret)** — visible only to the user: API keys, passwords. L3 NEVER gets into the LLM context — only a 🔒 placeholder.

### CLI

```bash
vibo add "Anna" "loves coffee"            # add a fact
vibo add "API key" "sk-..." --level L3     # secret (see L3 setup below)
vibo find "query"                          # search memory
vibo stats                                 # statistics
vibo usage                                 # REAL savings: tokens & money saved
vibo forget "Anna"                         # delete one fact
vibo wipe --yes                            # delete ALL memory (irreversible)
```

**Secrets (L3):** store with `--level L3` — the value is encrypted (AES-256-GCM) with your password, never appears in `find` output (shown as 🔒), and never reaches the LLM. `--level L2` encrypts with a persistent agent key.

```bash
vibo setup "my-secret-password"    # one-time: set your L3 password (also: vibo setup --password "...")
vibo add "API key" "sk-..." --level L3
vibo reveal "API key"              # show a secret (asks for the password)
```

### Adaptive mode (honest)

ViBo never costs more than no-ViBo:
- Big memory (10K+ facts) → **50-150× fewer tokens**
- Small memory (100 facts) → skill **stays silent** (no losses, no overhead)

## 🌐 Product 2: Web Search Savings

Web search results are huge (5-15K tokens per article). Dumping them all into the LLM context is expensive. ViBo compresses them first.

**Measured: 96.2% fewer tokens per article** (12,975 → 489 tokens).

⚠️ **Privacy:** compressing a URL fetches its content (a normal request to that site) and stores the compressed summary in the local cache (`/tmp/vibo_web_cache.json`). Do not compress authenticated, confidential, or internal pages unless the user has consented — the summary is persisted locally.

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
2. **Get explicit user consent** before persisting facts, thread history, web summaries, or documents — and tell the user how to delete (`vibo forget "label"` / `vibo wipe --yes`).
3. Write important facts about the user: preferences, projects, decisions.
4. No duplicates: before saving, search for similar facts.
5. L3 only with user permission: encrypt API keys with L3, never output them.
6. Web search: compress + cache before sending results to the LLM.

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
├── vibo-proxy/              # Privacy Layer (Product 5): ViBoProxy.md, proxy_server.py, Dockerfile, setup.sh, INSTALL.md
└── vibo/                    # protected core
```

## See your real savings

Every ViBo operation (memory search + web compression) records how many tokens it saved. Run:

```bash
vibo usage
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

**© 2026 ViBo by Viacheslav Bochkarev.** ViBo — memory, living archive, web-search savings, thread memory and privacy layer for AI agents. https://wwwvibo.com · hello@wwwvibo.com


## 📦 Product 4: Living Archive

Documents are dead weight in regular archives. ViBo makes them ALIVE: pack documents into a single .vibo file (own format), search them by meaning, and get answers in milliseconds.

⚠️ **Privacy:** `archive pack` duplicates the selected documents into a `.vibo` file, and `archive unpack` writes copies back to disk — creating additional plaintext copies in a location you choose. Be aware when packing confidential or regulated documents, and keep the `.vibo` file where the user controls access.

```bash
vibo archive pack ./documents -o archive.vibo   # 98 files (9 MB) → 808 KB
vibo archive search archive.vibo "company requisites?"   # exact fragment
vibo archive list archive.vibo                  # documents inside
vibo archive unpack archive.vibo -o restored    # restore with paths
```

- **Measured:** 9 MB of documents → 808 KB archive; up to 99.7% token savings.
- **Integrity:** pack → unpack returns ALL files (216/216 tested), paths and extensions preserved.
- **Formats:** .md, .txt, .docx, .pdf (text), .xlsx, .pptx, images (OCR). Junk (configs, binaries) is filtered automatically.

## 🛡️ Product 5: Privacy Layer (ViBo Proxy)

A built-in privacy layer: an OpenAI-compatible proxy between your agent and ANY LLM (DeepSeek, OpenAI, ...). Secrets (API keys, passwords, tokens) are encrypted at rest (**AES-256-GCM**) and replaced with `🔒[name]` placeholders BEFORE the prompt reaches the provider — the LLM never sees the real values.

⚠️ **Privacy:** only registered secrets + known key/password patterns are masked. The REST of the prompt is forwarded to the upstream LLM as-is (the LLM must read it to answer). The encryption key lives on the proxy server by default — self-hosted means under YOUR control (zero-knowledge = client-side key variant).

### How it works

1. Register a secret **once**: `POST /secrets {name, value}` → stored encrypted, ciphertext only.
2. Point the agent's `base_url` at the proxy: `http://localhost:8017/v1` (self-hosted) or `https://wwwvibo.com/v1` (hosted).
3. The proxy masks known secrets (`🔒[name]`) before forwarding, plus a regex fallback for unknown patterns (`sk-…`, `ghp_…`, `password=…`).
4. Every response carries the audit: `vibo.secrets_blocked` (how many secrets were blocked) + `vibo.tokens_saved` (tokens not sent to the LLM). Names of blocked secrets are encrypted too.

```bash
# Self-hosted (one command, Docker):
UPSTREAM_API_KEY=sk-... bash setup.sh     # builds + runs on http://localhost:8017

# Register a secret:
curl -X POST http://localhost:8017/secrets \
  -H "Content-Type: application/json" \
  -d '{"name":"api_key","value":"sk-..."}'

# Chat through the proxy — secret comes back as 🔒[api_key]:
curl -X POST http://localhost:8017/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"my key is sk-... — what is it?"}]}'
```

**Measured (live test, real DeepSeek):** a real secret sent in a prompt came back from the model as `🔒[test_api_key]` — the secret never left the machine. `secrets_blocked: 2`, `tokens_saved: 4`. Streaming (SSE) works. `POST /secrets` without the admin token → 403.

### Agent rules for the Privacy Layer

1. Tell the user the audit line after every proxied call: **"🔒 ViBo: N secret(s) blocked, M tokens not sent to the LLM."**
2. Register secrets once, never put real values in prompts or logs.
3. Protect the proxy management: set `PRIVACY_ADMIN_TOKEN` (without it, localhost/LAN access is assumed trusted).
4. If the user handles regulated/sensitive data — self-host the proxy (default) and keep it under their control.
