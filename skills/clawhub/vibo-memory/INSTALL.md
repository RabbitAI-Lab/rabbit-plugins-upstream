# 📦 ViBo — Installation & Integration Guide

ViBo works with **any AI agent** that can run Python: Hermes, OpenClaw, LangChain/LangGraph, CrewAI, or your own agent.

**One skill, two products:**
1. **🧠 Memory** — persistent memory with L1/L2/L3 encryption
2. **🌐 Web Search Savings** — compress articles up to 96%, cache repeats ($0)

Choose the integration that fits your setup:

| Integration | Best for | Effort |
|---|---|---|
| **[CLI](#1-cli-simplest)** | Any agent, shell access | 2 min |
| **[Python API](#2-python-api)** | Custom agents, scripts | 5 min |
| **[LangChain adapter](#3-langchain-adapter)** | LangChain / LangGraph / CrewAI | 5 min |
| **[Agent instructions](#4-agent-instructions)** | Hermes / OpenClaw / Claude / N | 5 min |

---

## 1. CLI (simplest)

```bash
python3 check_license.py              # 🔒 license check (trial: auto)
python3 vibo_use.py --file memory.web add "Anna" "loves coffee without sugar"
python3 vibo_use.py --file memory.web find "what does Anna like?"
python3 vibo_use.py --file memory.web usage     # see your real savings
```

## 2. Python API

```python
from vibo.core import Graph
from vibo.crypto import Crypto, SecurityLevel
from vibo.storage import WebFile
from vibo.navigator import ViBoNavigator

graph = WebFile("memory.web").read() if Path("memory.web").exists() else Graph()
crypto = Crypto(agent_key="agent-key", user_password="user-pass")

# Save fact
graph.add_node("Anna", "Client, loves coffee", tags=["person"])

# Save secret (never reaches the LLM)
graph.add_node("api-key", crypto.seal(SecurityLevel.L3_SECRET, "sk-..."), level="L3")

# Search
nav = ViBoNavigator(graph, crypto)
context = nav.compose("Anna")

# Save
WebFile("memory.web").write(graph, crypto=crypto)
```

## 3. LangChain adapter

```python
from vibo.langchain_memory import ViBoMemory

memory = ViBoMemory(path="memory.web", agent_key="agent-key", user_password="user-pass")
context = memory.load_memory_variables({"input": "what about Anna?"})
```

## 4. Agent instructions

Add to your agent's system prompt (SKILL.md):

> **Memory:** Before answering, search ViBo memory with `vibo find "<topic>"`.
> Save important facts with `vibo add`. Never leak L3 secrets — use 🔒.
> Run `vibo dream` once a day.
>
> **Web search:** Before searching, check the ViBo cache. After getting
> results, compress each article with `vibo web --compress URL --query "..."`
> before putting it in the context. Save the compressed summary to cache.
>
> **Show savings (IMPORTANT):** after every memory search or web
> compression, tell the user what ViBo saved — right in your reply:
> "💾 ViBo: saved 79,737 tokens (99.4%) — article compressed."
> The user must SEE the savings immediately, no commands needed.

---

## 🌐 Web Search Savings (Product 2)

ViBo compresses web-search results before they reach the LLM:
**measured 96.2% fewer tokens** (12,975 → 489 per article).

```python
from vibo_web import compress_article, WebCache

# After your search returns articles, compress each one:
for article in search_results:
    compressed, stats = compress_article(article["text"], query)
    article["text"] = compressed   # now only the essence
    print(f"saved {stats['saved_pct']}% tokens")

# Cache: repeated questions = 0 tokens
cache = WebCache("web_cache.json")
if not cache.get(query):
    results = search(query)
    cache.put(query, results)
```

### Why it works

| Without ViBo | With ViBo |
|---|---|
| 10 articles × 12,975 tokens = 129,750 tokens | 10 × 489 = 4,890 tokens |
| $0.018/query (DeepSeek) | $0.0007/query |
| repeated questions: paid again | repeated: **$0** (cache) |

---

## 🔄 Migration from old memory (important!)

If you used an older ViBo version with memory in a plain JSON file
(no `VIBO` header), the skill **migrates automatically with a backup**:

1. The first read of an old file creates a copy: `<name>.web.bak-<date>`
   (or `<name>.json.bak-<date>`) right next to the original.
2. Your data is read into the new format. **The original is never deleted.**
3. The next save writes the new `VIBO` format.

**You can always roll back:** copy the `.bak-*` file back over the
current one.

> Example:
> ```
> memory.json          ← старый файл (не трогается)
> memory.json.bak-20260813_040005   ← авто-бэкап (создан при чтении)
> memory.web           ← новый формат (создаётся при сохранении)
> ```

In the Telegram bot, use `/backup` (snapshot) and `/restore`
(rollback) — owner only.

---

## 📊 How to see YOUR savings (important!)

Every ViBo operation (memory search + web compression) records how many
tokens it saved you. To see the total difference — **without ViBo vs with ViBo**:

### 1. See the summary

```bash
python3 vibo_use.py --file memory.web usage
```

```
📊 ViBo: your real savings
=============================================
📈 Operations via ViBo: 17
💾 Tokens saved: 8,412,584
💰 Savings (DeepSeek): $1.18
=============================================
Without ViBo you'd pay for ALL memory and FULL articles.
With ViBo: only relevant facts + compressed articles.
```

### 2. See the raw log

```bash
cat vibo_usage.jsonl    # one line per operation: tokens saved, %
```

### 3. What counts as savings

| Operation | Without ViBo | With ViBo |
|---|---|---|
| Memory search | ALL memory in the prompt | only relevant facts |
| Web compression | FULL article (50K+ tokens) | essence (300-500 tokens) |

### 4. Daily savings report (optional)

Add to your agent's instructions:

> Once a day, run `vibo usage` and report the savings to the user.
> If savings are zero, explain: memory is still small — savings grow
> as facts accumulate.

---

## 💬 Thread Memory (Product 3)

Long conversations cost a fortune in tokens. ViBo keeps the FULL history
in a `.web` file and sends only a compressed summary to the LLM.

```bash
# Записать сообщение в историю
python3 vibo_use.py dialog add "client agreed to new pricing" --role assistant --topic pricing --file thread.web

# Сжать старые сообщения (старше 1 дня) → выжимка
python3 vibo_use.py dialog compress --file thread.web
# → 📦 Сжато 8 сообщений: 188 → 52 токенов (-72%)

# Контекст для LLM: выжимка + свежие сообщения
python3 vibo_use.py dialog context --file thread.web

# Найти детали: «что обсуждали 3 дня назад?»
python3 vibo_use.py dialog ask "что было 3 дня назад" --file thread.web
```

### Когда использовать (правило для агента)

> Когда разговор становится длинным (больше ~50 сообщений) — сожми его:
> 1. Запиши ключевые моменты: `vibo dialog add "..." --topic тема`
> 2. Сожми старые: `vibo dialog compress`
> 3. В контекст LLM — только `vibo dialog context`
> 4. Полная история остаётся в thread.web — ничего не теряется
> 5. «Что было 3 дня назад?» → `vibo dialog ask "..."`

---

## Files

```
vibo_skill.zip
├── SKILL.md                 # agent instructions (what to do)
├── INSTALL.md               # this file
├── activate.py              # one-time activation (buyer)
├── check_license.py         # license check on every run
├── vibo_use.py              # CLI (add/find/usage/dream/stats/web)
├── vibo_web.py              # web search savings (compress + cache)
├── vibo/                    # core (protected: .so, sources hidden)
└── vibo_license.json        # trial key (built in, 2 days)
```
