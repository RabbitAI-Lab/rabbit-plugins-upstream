---
name: Grizzly
description: "Grizzly by Yielding Bear — one OpenAI-compatible key for 100+ LLMs with smart high/mid/free routing, semantic cache, and agent-ready install. Cut multi-model spend at high token volume without juggling provider accounts. Start at https://yieldingbear.com"
homepage: https://yieldingbear.com
metadata:
  author: Yielding Bear LLC
  version: "2.4.2"
  openclaw:
    requires:
      bins: ["curl", "bash"]
    primaryEnv: YIELDINGBEAR_API_KEY
    emoji: "🐻"
  clawhub:
    title: Grizzly
    slug: grizzly
    tags:
      - llm-gateway
      - openai-compatible
      - smart-routing
      - cost-optimization
      - multi-model
    categories:
      - development
      - operations
---

# Grizzly

**One key. 100+ LLMs. Smart routing that pays for itself at volume.**  
Grizzly is Yielding Bear’s agent-first LLM gateway — OpenAI-compatible `base_url`, automatic **high / mid / free** routing, and spend controls built for Hermes, OpenClaw, and production agents.

→ **https://yieldingbear.com**

## Why Grizzly wins on large token volume

| Feature | ROI at scale |
|--------|----------------|
| **One OpenAI-compatible key** | Stop paying multi-provider ops tax. One `base_url`, one key (`grizzly_live_sk_…`), every major model family. |
| **Grizzly 1.0G Pro auto-select** | Classifies each prompt → **high / mid / free**. Trivial work rides free/cheap tiers; frontier only when the task needs it. |
| **Manual pin + live recs** | Lock a catalog model when you must; still see live recommended high/mid/free chips. |
| **Semantic + prompt cache** | Repeatable agent loops and system prompts hit cache paths instead of full retail decode — biggest lever when token volume is high. |
| **Honest free tier** | True $0 upstream free models only — no fake “free” paid rows padding the catalog. |
| **Spendable balance + Pro** | Credits never expire; **Grizzly Pro** adds included high/mid allowance for always-on agents. |
| **Doctor CLI** | `yb.sh doctor / models / set-routing / smoke` — wire once, verify forever. |

**Punchline:** At high request rates, routing + cache beats “always call Sonnet/GPT-4o.” You keep quality where it matters and dump bulk tokens onto mid/free routes — same agent code, lower blended $/1M.

## Features (marketable)

- **Drop-in gateway** — OpenAI SDK / curl / LangChain-style clients point at Yielding Bear.
- **100+ models** — OpenAI, Anthropic, Google, Meta, DeepSeek, Groq, xAI, Mistral, and more via one catalog.
- **Smart router product** — `yieldingbear/grizzly-1.0g-pro` for Auto mode.
- **Dashboard** — keys, credits packs, Active Model Auto|Manual, usage.
- **Agents-first install** — one command for Hermes / OpenClaw / shell.
- **CLI Pro offer** — **$10 off first 3 months** ($89→$99) via `/offer/cli10x3` (not stacked with referral).

## Install (2 minutes)

```bash
# Site installer
curl -fsSL https://yieldingbear.com/install.sh | bash

# Or ClawHub (canonical slug)
clawhub install grizzly
bash ~/.openclaw/skills/grizzly/scripts/install.sh
# legacy slug still redirects: clawhub install yieldingbear
```

1. **Account** — signup (CLI offer cookie when applicable)  
2. **API key** — paste `grizzly_live_sk_…` (legacy `yb_live_sk_…` still works)  
3. **Plan** — Pro ($10×3) | credits | stay free  
4. **Routing** — Auto-select (recommended) or Manual pin  
5. Smoke test  

```bash
bash ~/.openclaw/skills/grizzly/scripts/yb.sh doctor
bash ~/.openclaw/skills/grizzly/scripts/yb.sh models --free
bash ~/.openclaw/skills/grizzly/scripts/yb.sh set-routing auto
bash ~/.openclaw/skills/grizzly/scripts/yb.sh smoke
```

Non-interactive:

```bash
YIELDINGBEAR_API_KEY=grizzly_live_sk_… \
YIELDINGBEAR_ROUTING_MODE=auto \
  bash scripts/install.sh
```

## Update

```bash
clawhub update grizzly
```

## Links

- Product: https://yieldingbear.com  
- Models: https://yieldingbear.com/models  
- Docs: https://yieldingbear.com/docs  
- Dashboard: https://yieldingbear.com/dashboard  
- ClawHub: https://clawhub.ai/yieldingbear/grizzly  
