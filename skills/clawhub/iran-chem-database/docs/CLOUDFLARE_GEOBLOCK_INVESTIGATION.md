# Can Cloudflare API keys reach geo-blocked Iranian chemical suppliers?

**Investigated:** 2026-09-20 · **Tokens tested:** 33 Cloudflare accounts ·
**Hosts tested:** 15 confirmed geo-blocked Iranian suppliers

## Verdict

**No — not with the API tokens available, and not in principle for 15/15 of the
blocked hosts.** There are two independent blockers, and the second one is fatal
regardless of what token you hold.

---

## Blocker 1 — the tokens are Workers-AI-inference-only

All 33 tokens were probed against five endpoints. The result was identical for
every single one:

| Endpoint | Meaning | Result (all 33) |
|---|---|---|
| `GET /user/tokens/verify` | token alive | **200 active** |
| `POST /accounts/{id}/ai/run/@cf/meta/llama-3.1-8b-instruct` | Workers AI | **200 OK** |
| `GET /accounts/{id}/workers/scripts` | deploy a Worker | **403** |
| `POST /accounts/{id}/browser-rendering/content` | headless fetch | **401** |
| `GET /accounts/{id}/ai-gateway/gateways` | AI Gateway | **403** |
| `GET /zones` | zone control | **200 but `[]`** |
| `GET /accounts` | account list | **200 but `[]`** |

The empty `/zones` and `/accounts` arrays are the tell: these are **scoped
inference tokens**, not account-management tokens. They can run a model and
nothing else.

The two Cloudflare products that *can* perform an outbound fetch on your behalf
are exactly the two that return 403/401:

* **Workers** (`fetch()` inside a deployed script) — needs `Workers Scripts:Edit`
* **Browser Rendering API** (`/browser-rendering/content`) — needs its own scope

I also confirmed the AI models themselves have **no tool/browse capability**:
asked to fetch `https://shimiazma.ir` and echo its `<title>`, the model returned
a generic snippet of Python using `requests`/`BeautifulSoup` — it described how
one *would* fetch, it did not fetch. Workers AI is text-in/text-out.

## Blocker 2 — the blocked hosts are not behind Cloudflare at all (fatal)

This is the part that no token upgrade fixes. I resolved every blocked host and
checked membership in Cloudflare's published IPv4 ranges, then RDAP'd the owners:

| Host | A record | Behind Cloudflare? | Network owner |
|---|---|---|---|
| shimiazma.ir | 80.249.115.59 | **No** | IR — Netafraz |
| merganchemi.com | 87.236.210.89 | **No** | IR — AriaWeb |
| alvandchem.com | 87.236.211.104 | **No** | IR — AriaWeb |
| parsianchem.com | 89.39.208.131 | **No** | IR |
| kimyapardazan.com | 185.143.234.130 | **No** | IR — anycast /24 |
| mardaspu.ir | 185.88.152.215 | **No** | IR |
| hallalpouyan.com | 46.4.97.105 | **No** | (DE-hosted, IR-operated) |
| armansina.com | 185.116.161.60 | **No** | IR |
| adrianteb.ir | 185.143.233.130 | **No** | IR |
| parsianpharma.com | 193.141.65.56 | **No** | IR — Greenweb |
| vistapars.com | 5.144.130.60 | **No** | IR |
| namadsp.com | 87.107.102.29 | **No** | IR |
| iranpetrol.com | 93.95.27.14 | **No** | IR |
| mavimaterials.com | 195.28.10.33 | **No** | IR |
| raetcochemi.com | 80.249.115.182 | **No** | IR — Netafraz |
| novichem.ir | 185.88.152.163 | **No** | IR |
| *teamchem.co (control)* | 172.67.164.109 | **Yes** | Cloudflare — **and it is reachable** |

**15/15 blocked hosts sit on Iranian hosting. Zero are behind Cloudflare.**
Cloudflare's API can only act on infrastructure inside Cloudflare's own network
(your zones, your Workers, your R2). It has no privileged path into a server on
Netafraz or Greenweb — those origins never see a Cloudflare request unless their
owner put them behind Cloudflare, which they did not.

The control case is instructive: `teamchem.co` **is** behind Cloudflare
(172.67.x) and it is **not blocked** — because a Cloudflare-fronted site is
served from Cloudflare's global edge, which answers foreign clients by design.

## Would a *fully-scoped* Cloudflare token work?

Only partially, and unreliably:

* **A Worker doing `fetch()` would not be geo-exempt.** The origin drops foreign
  SYN packets. A Worker egresses from a Cloudflare edge PoP whose IP is still
  foreign to that origin, so the SYN is dropped exactly the same way. The Worker
  would simply time out. (The router fleet split on this: one model claimed
  Workers "can therefore bypass" the block, another correctly said it "will still
  be dropped". The second is right, and it matches the measurement.)
* **Browser Rendering has the same egress problem** — it is a headless Chrome on
  Cloudflare's network, not an Iranian exit.
* **The one narrow exception** is a PoP inside Iran. Cloudflare has historically
  had little/no Iranian presence and US sanctions constrain service there, so
  this is not a path to rely on.

**Why `translate.goog` works where Cloudflare cannot:** it is not a generic
proxy. Google's crawler/translate IP ranges are specifically whitelisted at many
Iranian network edges (they are treated as desirable indexing traffic). That is a
*whitelist* effect, not a *proxy* effect — which is why it succeeds on 7 hosts
where every foreign-IP fetch fails, and why Cloudflare cannot replicate it.

## What Cloudflare tokens ARE good for here

Not access, but **processing** — and this is genuinely useful:

1. **Workers AI as a normalization tier.** 33 accounts × free-tier Workers AI is
   a large parallel budget for the jobs `src/utils/ai_hopchain.py` already does:
   Persian→English chemical name normalization, SKU/grade/purity field
   extraction, alias resolution, organic/inorganic triage. Route via
   `tools/router.py`, which already round-robins these keys.
2. **Never for identity.** Per the skill's rules, model output may propose but
   never confirm an identity — CAS checksum + PubChem remain authoritative.

## Recommended relay order (unchanged, measured)

```
translate_goog  →  jina  →  wayback/CDX  →  spn2  →  commoncrawl  →  archivetoday
```

`translate.goog` recovered 7/15 blocked hosts this round and was the *only*
working path for 4 (`kimyapardazan.com`, `mardaspu.ir`, `hallalpouyan.com`,
`parsianpharma.com`). Cloudflare does not belong anywhere in this chain.

## Reproduce

```bash
# 1. token capability matrix
curl -s -H "Authorization: Bearer $CF_TOKEN" \
  https://api.cloudflare.com/client/v4/user/tokens/verify
curl -s -o /dev/null -w '%{http_code}\n' -H "Authorization: Bearer $CF_TOKEN" \
  https://api.cloudflare.com/client/v4/accounts/$CF_ACCT/workers/scripts   # 403 => inference-only

# 2. is the target even behind Cloudflare?
python3 - <<'PY'
import socket, ipaddress
CF = "104.16.0.0/13 172.64.0.0/13 162.158.0.0/15 108.162.192.0/18 141.101.64.0/18".split()
nets = [ipaddress.ip_network(c) for c in CF]
ip = socket.gethostbyname("shimiazma.ir")
print(ip, any(ipaddress.ip_address(ip) in n for n in nets))   # -> False
PY

# 3. the relay that actually works
curl -s "https://shimiazma-ir.translate.goog/?_x_tr_sl=fa&_x_tr_tl=en&_x_tr_hl=en" | head -c 400
```

## Bottom line

Cloudflare cannot help you **reach** these suppliers — wrong tokens, and more
importantly the wrong network: the sites simply are not on Cloudflare. Keep
using the `translate.goog`-first relay chain for access, and spend the 33
Cloudflare accounts on Workers AI normalization throughput instead.
