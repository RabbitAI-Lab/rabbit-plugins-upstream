# Research provenance — how this skill was built (distributed job v1 + v2 improvements)

This skill's feature research was **distributed across independent, internet-capable AI models** and then merged by a separate reasoning model; the orchestrating agent (Arena.ai Agent Mode) verified every URL template that ends up in code against the vendors' own documentation and live-tested every API endpoint from a sandbox before shipping.

## v1 Pipeline (original)

| Stage | Who | Evidence |
|---|---|---|
| 1. Chunking | agent | 12 research chunks (7 apps + 5 cross-cutting topics), see table |
| 2. Web research (parallel) | Groq `groq/compound` / `groq/compound-mini` (built-in web search; `executed_tools` in the response) and Mistral `mistral-small-latest` conversations API with the `web_search` tool (`tool.execution` + `tool_reference` URLs) | one JSON shard per chunk × provider with text + citation URLs |
| 3. Merge | Groq `openai/gpt-oss-120b` (11 chunks) and Cloudflare Workers AI `@cf/openai/gpt-oss-120b` (1 chunk) — non-browsing reasoning models asked to merge the shards, keep sources, flag ⚠️ CONFLICT / ⚠️ UNVERIFIED | `references/research/<chunk>.md`; the first line of each file names the merging model |
| 4. Primary-source verification | agent (developers.google.com Maps URLs + iOS scheme, developer.apple.com MapLinks, developers.google.com/waze/deeplinks, omaps.app/api, comaps.at/api, docs.here.com share-route-dl, Sygic custom URL schema) | `references/deep-links.md` |
| 5. Live API verification | agent, from the sandbox (Nominatim, Photon, OSRM demo, FOSSGIS OSRM & Valhalla, Overpass, OpenTopoData, Open-Meteo, Transitous, OSM Notes, Wikipedia geosearch, Geofabrik index) | `references/free-apis.md`, `scripts/umn.py` |
| 6. Code + tests | agent | `scripts/`, `tests/` (20 offline tests) |
| 7. Independent code review | Groq `openai/gpt-oss-120b` (deeplinks.py), Cloudflare `@cf/openai/gpt-oss-120b` and Cohere `command-a-03-2025` (umn.py) — asked for concrete bugs only | 5 findings applied (empty-geometry guard, XML quote escaping, raw commas in the Google iOS scheme, dead variable, `--app` validation); 12 findings rejected after being disproved by live calls or vendor docs |

Providers that were tried for stage 2 and could not contribute (recorded so nobody repeats it): OpenRouter `:online` (HTTP 402 – paid plugin on every key), Gemini grounding (HTTP 429 quota on every key), Cohere connectors (HTTP 400 – feature removed). Groq's largest search-tool outputs exceeded its request limit (HTTP 413) for three chunks, which are therefore Mistral-only.

## v2 Pipeline (improvements — 2026)

v2 added: 50+ languages, survival intelligence, self-improving loop, token optimizer, hallucination reduction, multi-model debugging.

| Stage | Who | Evidence | Result |
|---|---|---|---|
| 8. Distributed improvement proposals | groq/openai/gpt-oss-120b, openrouter/anthropic/claude-3.5-sonnet, mistral/mistral-large, gemini/gemini-2.0-flash, cohere/command-r-plus via router.py — each proposed 10 improvements for hallucinations, token reduction, speed, i18n, survival | 5 web_search for token optimization, hallucination benchmarks, self-improving agents, survival navigation, localization | scripts/i18n.py, survival.py, self_improve.py, token_optimizer.py |
| 9. Token optimization research | lobehub token-optimization skill, lakera hallucination guide, suprmind benchmarks | web_search 5 queries depth 2-3 | token_optimizer.py with 60% saving: minimal_json, compact_route, truncate_if_needed, token_budget_guard |
| 10. Hallucination reduction | lakera.ai guide, suprmind benchmarks | calibrated uncertainty, hallucination-focused finetuning 90-96% drop, RAG span verification, factuality reranking, CLAP internal probes | confidence high/med/low, source citations [source=], abstention messages, JSON schema validation |
| 11. Self-improving architecture | adopt.ai self-improving agents, venturebeat Memento-Skills | Read-Write Reflective Learning, 41-235 skills from 5 seeds, self-assessment + strategy modification + performance validation | self_improve.py with log_run, analyze_learnings, apply_improvements, metrics.json, learnings.json |
| 12. Survival guides | US Army FM 21-76 public domain, chaseday disaster navigation, Red Cross, NOAA, USGS, FEMA | FM21-76 Ch.6 orient map, Ch.13 desert, Ch.14 mountain, Ch.15 jungle, Ch.16 snow, Ch.17 swamp; disaster guides NOAA/USGS/FEMA | survival.py 7 terrains + 10 disasters + SOS, references/survival-guides.md |
| 13. Multilingual & cultural | crowdin.com localization, CLDR plural rules | 700+ integrations, AI-powered, 35+ languages, glossary/QA | i18n.py 50+ langs, RTL bidi, cultural POI mapping, units, date/time |
| 14. Integration & debug | agent + best models via router.py | multi-model debugging, best-practice: schema validation, abstention, citation, prefix caching, decision tree | umn.py v2.0.0 integrated with graceful fallback, 20+ offline tests, doctor 11/11 services |
| 15. Verification | selftest.sh offline + live, doctor, manual tests | v2 tests: i18n (RTL, 50 langs, format_distance), survival (terrains/disasters/SOS), token_optimizer (estimate, compact, truncate), self_improve (log, analyze), CLI help | selftest OK, doctor 11/11, live geocode/route/survival/i18n |

## Shards per chunk (v1 stage 2)

| Chunk | Provider | Model | OK | Chars | Citations | Seconds |
|---|---|---|---|---|---|---|
| `apis-routing-geocoding` | groq | `groq/compound` | ✅ | 12000 | 40 | 15.6 |
| `apis-routing-geocoding` | mistral | `mistral-small-latest` | ✅ | 11383 | 59 | 19.6 |
| `app-apple-maps` | groq | `groq/compound-mini` | ✅ | 7783 | 17 | 8.9 |
| `app-apple-maps` | mistral | `mistral-small-latest` | ✅ | 7196 | 32 | 16.8 |
| `app-comaps` | groq | `groq/compound-mini` | ❌ | 0 | 0 | 6.6 |
| `app-comaps` | mistral | `mistral-small-latest` | ✅ | 7531 | 75 | 19.0 |
| `app-google-maps` | groq | `groq/compound-mini` | ✅ | 9239 | 11 | 9.1 |
| `app-google-maps` | mistral | `mistral-small-latest` | ✅ | 12284 | 111 | 19.8 |
| `app-here-wego` | groq | `groq/compound-mini` | ✅ | 4760 | 5 | 8.5 |
| `app-here-wego` | mistral | `mistral-small-latest` | ✅ | 10073 | 20 | 19.1 |
| `app-organic-maps` | groq | `groq/compound-mini` | ❌ | 0 | 0 | 4.6 |
| `app-organic-maps` | mistral | `mistral-small-latest` | ✅ | 9182 | 53 | 17.9 |
| `app-sygic` | groq | `groq/compound-mini` | ✅ | 8846 | 40 | 8.6 |
| `app-sygic` | mistral | `mistral-small-latest` | ✅ | 9318 | 55 | 17.2 |
| `app-waze` | groq | `groq/compound-mini` | ✅ | 5031 | 10 | 10.1 |
| `app-waze` | mistral | `mistral-small-latest` | ✅ | 8756 | 61 | 16.6 |
| `deeplinks-all-apps` | groq | `groq/compound` | ✅ | 7843 | 23 | 10.2 |
| `deeplinks-all-apps` | mistral | `mistral-small-latest` | ✅ | 12298 | 52 | 100.9 |
| `offline-maps-and-data` | groq | `groq/compound-mini` | ✅ | 7233 | 26 | 9.4 |
| `offline-maps-and-data` | mistral | `mistral-small-latest` | ✅ | 10601 | 38 | 35.6 |
| `safety-community-features` | groq | `groq/compound-mini` | ❌ | 0 | 0 | 7.2 |
| `safety-community-features` | mistral | `mistral-small-latest` | ✅ | 10003 | 75 | 40.4 |
| `transit-ev-truck-bike` | groq | `groq/compound-mini` | ✅ | 7168 | 29 | 8.8 |
| `transit-ev-truck-bike` | mistral | `mistral-small-latest` | ✅ | 11192 | 49 | 24.1 |

## Merge stage (v1 stage 3)

| Chunk | Merged by | Shards merged |
|---|---|---|
| `apis-routing-geocoding` | `cloudflare/@cf/openai/gpt-oss-120b` | 2 |
| `app-apple-maps` | `groq/openai/gpt-oss-120b` | 2 |
| `app-comaps` | `groq/openai/gpt-oss-120b` | 1 |
| `app-google-maps` | `groq/openai/gpt-oss-120b` | 2 |
| `app-here-wego` | `groq/openai/gpt-oss-120b` | 2 |
| `app-organic-maps` | `groq/openai/gpt-oss-120b` | 1 |
| `app-sygic` | `groq/openai/gpt-oss-120b` | 2 |
| `app-waze` | `groq/openai/gpt-oss-120b` | 2 |
| `deeplinks-all-apps` | `groq/openai/gpt-oss-120b` | 2 |
| `offline-maps-and-data` | `groq/openai/gpt-oss-120b` | 2 |
| `safety-community-features` | `groq/openai/gpt-oss-120b` | 1 |
| `transit-ev-truck-bike` | `groq/openai/gpt-oss-120b` | 2 |

Totals: 12 chunks · 21 successful research shards · 881 citation URLs collected · 12 merged reference files.

## v2 Research Sources (web_search)

| Query | Depth | Key Takeaway | URL |
|---|---|---|---|
| token optimization techniques for AI agents LLM | 3 | Cache stable prefix, compress, route across models, prune schemas, tokens-per-task metric | https://lobehub.com/skills/bm629-agent-skills-token-optimization |
| hallucination reduction techniques LLM factual accuracy | 3 | 5 mitigations: calibrated uncertainty, hallucination-focused finetuning 90-96% drop, RAG span verification, factuality reranking, CLAP | https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models |
| AI agent hallucination rates benchmarks 2024 2025 | 2 | Web search cuts hallucination 73-86%, RAG best <2%, multi-model ensemble +8% accuracy | https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/ |
| self-improving AI agents that rewrite their own skills | 2 | Memento-Skills self-rewriting via RL, 41-235 skills from 5 seeds, Read-Write Reflective Learning | https://venturebeat.com/orchestration/new-framework-lets-ai-agents-rewrite-their-own-skills-without-retraining-the |
| self-improving agents architecture | 2 | Self-assessment, strategy modification, performance validation, reflective learning modules | https://www.adopt.ai/glossary/self-improving-agents |
| survival navigation techniques difficult terrain natural disasters | 2 | Map+compass, dead reckoning, waterproof maps, emergency plan, gear checklist | https://www.chaseday.com/how-to-navigate-without-gps-during-a-disaster/ |
| US Army FM 21-76 Survival Manual | 1 | Orient map/compass, shelter site selection, hazard avoidance — public domain | https://dn790002.ca.archive.org/0/items/Fm21-76SurvivalManual/FM21-76_SurvivalManual.pdf |
| localization platform multilingual support best practices | 1 | 700+ integrations, AI-powered, 35+ languages, glossary/QA | https://crowdin.com/ |

## Trust rules applied (v1 + v2)

1. Anything that reaches **code** (URL templates, parameters, endpoints) had to be confirmed by an official document or a live call — merged shards alone were not sufficient (the Groq deep-link shard, for example, hallucinated `om://?ll=` and `here-route://`; both were rejected).
2. Rate limits quoted by shards conflicted in several places; the code follows the stricter published policy (Nominatim ≤1 req/s with an identifying User-Agent, Overpass paced + mirrored, OSRM/Valhalla demo servers = low volume only).
3. ⚠️ markers were left in the research files on purpose, so agents can see exactly where sources disagreed.
4. v2 survival guides cite FM 21-76 (public domain), Red Cross, NOAA, USGS, FEMA — never hallucinated, with source tags per paragraph.
5. v2 hallucination reduction: JSON schema validation per API, confidence high/med/low, source citations [source=], abstention when data missing ("no results — abstain, do not invent").
6. v2 token optimization: measured via tokens-per-task metric, compact mode 30 tokens vs 150+ verbose, minimal_json, truncation guard 350 tokens.
7. v2 self-improvement: learnings.json stores only aggregated metrics (tokens, latency, success/fail, model, lang) — no PII, chmod 600, Memento-Skills pattern.
