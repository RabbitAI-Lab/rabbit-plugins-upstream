# Model & agent compatibility (v1.5.0)

This document is the contract between the skill and whatever model or agent
runtime happens to be driving it. v1.3 assumed two API shapes and one style of
model behaviour; v1.4.0 assumes nothing and **probes instead**.

---

## 1. What "compatible" means here

Two separate promises:

| Promise | Meaning | How it is verified |
|---|---|---|
| **Runs anywhere** | Any model family, any API dialect, any agent runtime, or fully offline | `forge.py compat` |
| **Reproduces the intended result** | Different models produce the same *kind* of correct artifact, and agreement between them is measurable | `forge.py reproduce` |

The second promise is the hard one. A study guide is not a deterministic
function of a PDF — models phrase flashcards differently. What v1.4.0
guarantees is that the **structure, grounding and quality bar are identical**,
and that the *content* can be forced toward cross-model consensus.

---

## 2. Supported API dialects

| Dialect | Endpoint | Used by |
|---|---|---|
| `openai` | `POST {base}/chat/completions` | OpenAI, Groq, OpenRouter, Mistral, DeepSeek, Together, Fireworks, xAI/Grok, Z.AI/GLM, Cerebras, NVIDIA NIM, Perplexity, llm7, LiteLLM, vLLM, LM Studio, llama.cpp server, any proxy |
| `responses` | `POST {base}/responses` | OpenAI Responses API |
| `gemini` | `POST {base}/models/{m}:generateContent` | Google Gemini, Gemma |
| `anthropic` | `POST {base}/v1/messages` | Claude |
| `cohere` | `POST {base}/v2/chat` | Command R / R+ |
| `ollama` | `POST {base}/api/chat` | Local Ollama models (Llama, Qwen, Mistral, Phi, Gemma…) |
| `hf` | HuggingFace router (OpenAI shape) | HF Inference Providers |
| `mock` | none — in-process | CI, dry runs, tests, air-gapped machines |

Adding a dialect is one function in `scripts/model_adapters.py` returning
`(text, finish_reason, usage)`; nothing else in the skill changes.

---

## 3. The 18 cross-model quirks this skill defends against

Every one of these was observed in the wild; the ones marked ✅ **live** were
reproduced and fixed against real provider responses during v1.5.0 development.

| # | Quirk | Defence |
|---|---|---|
| 1 | `max_tokens` rejected in favour of `max_completion_tokens` (o-series, some gateways) | Error body parsed, field flipped, retried, remembered in the capability cache |
| 2 | `seed` rejected outright — HTTP 422 `extra_forbidden` (Mistral, some vLLM) ✅ **live** | Pydantic-style `loc` parsed, parameter dropped, retried, cached |
| 3 | `temperature` fixed / not settable (reasoning models) | Detected from the 4xx body, omitted on retry |
| 4 | `response_format` / `json_schema` unsupported | Detected and dropped; the tolerant parser carries the load instead |
| 5 | No `system` role (some Gemma/Ollama builds, older gateways) | System text is prepended to the user turn |
| 6 | Anthropic uses `x-api-key` + `anthropic-version`, `system` is top-level, and has no `response_format` | Dedicated adapter; JSON mode is done by **prefilling the assistant turn with `{`** |
| 7 | Cohere v2 nests content in `message.content[]` blocks | Dedicated adapter, normalized |
| 8 | Ollama answers NDJSON even with `stream:false` | Chunk lines merged before parsing |
| 9 | Reasoning models emit `<think>…</think>` (R1, QwQ, extended thinking) | Stripped, including **unterminated** blocks left by truncation |
| 10 | Response wrapped in markdown fences or prose | Fences stripped; widest JSON slice extracted, start-bracket aware |
| 11 | Truncation at the token limit — `finish_reason: length` | Reported, never hidden; brackets auto-closed to salvage the valid prefix |
| 12 | Refusals / safety blocks | Detected and raised distinctly so failover moves on instead of retrying forever |
| 13 | Trailing commas, Python `None/True/False`, smart quotes, `//` comments | Repaired before parsing |
| 14 | BOM and RTL bidi marks around JSON punctuation (very common with Persian) | Stripped |
| 15 | Persian/Arabic digits and `«صفحهٔ ۳»` page references | `coerce_ref` (v1.3) + digit folding |
| 16 | Persian answer labels `الف/ب/ج/د`, `۱–۴` | `coerce_answer` (v1.3) |
| 17 | **Model retired**, replacement named in the 404 body ✅ **live** (Gemini) | Suggestion parsed and followed automatically, then cached |
| 18 | Quota/credit exhaustion (402), rate limits (429) ✅ **live** | 402 skips the provider immediately; 429 honours `Retry-After` with jittered backoff |

Everything learned is written to
`~/.cache/persian-pdf-studyguide-forge/capabilities.json`, so a provider's
quirks cost one retry ever, not one per call.

---

## 4. How reproducibility is achieved

Five mechanisms, in increasing strength:

1. **Deterministic sampling.** `temperature 0`, `top_p 1`, and a fixed seed
   (`FORGE_SEED`, default 7) wherever the dialect accepts one.
2. **Canonical artifacts.** Every JSON file the skill writes is sorted-key,
   stable-indent canonical JSON. Two runs are byte-comparable with `diff`.
3. **Stable ordering.** `stable_sort_items()` orders by source page then
   content key, so thread scheduling and provider order cannot change output.
4. **Semantic deduplication.** `content_key()` normalizes Persian (letters,
   digits, ZWNJ, ezafe hamza, harakat, punctuation) so the same fact phrased
   two ways collapses to one item. `similarity()` adds Jaccard overlap for
   looser matches.
5. **Cross-model consensus.** `enrich --consensus N [--min-votes 2]` sends the
   identical prompt to N *different* model families and keeps what they agree
   on, ranked by vote count. `--min-votes 2` drops anything only one model
   said — the strongest available guard against single-model hallucination.

**Verified:** two full offline runs (`FORGE_MOCK=1`) produce byte-identical
`corrections/final.json`, `enrichment/all.json`, `sessions.json` and
`studyguide.html`.

### Measuring it

```bash
python3 scripts/forge.py reproduce --include-pack --out repro.json
```

Reports per-model contract validity, a `reproducibility_rate`, and the merged
consensus pack. A verdict of `REPRODUCIBLE` means at least two independent
model families satisfied the identical contract.

Measured during development against live free-tier models:

| Model | Family | Contract valid | Notes |
|---|---|---|---|
| `openai/gpt-oss-120b` (Groq) | GPT | ✅ | |
| `open-mistral-nemo` (Mistral) | Mistral | ✅ | `seed` quirk auto-learned |
| `gemini-3.6-flash` (Google) | Gemini | ✅ | auto-followed retirement of `gemini-2.5-flash` |
| `glm-4.7-flash` (Z.AI) | GLM | ✅ | truncation reported, prefix salvaged |
| `deterministic-mock` | offline | ✅ | byte-identical across runs |

`reproducibility_rate: 1.0` · verdict `REPRODUCIBLE`.

---

## 5. Provider resolution order

No configuration is required. Providers are resolved as:

1. `--providers providers.json` if given (v1.3 `kind` and v1.4 `dialect`
   shapes both accepted);
2. **environment auto-discovery** — whatever keys the host agent already has;
3. local runtimes: `OLLAMA_HOST`, `LOCAL_OPENAI_BASE_URL`;
4. `FORGE_MOCK=1` → the deterministic offline provider.

```bash
# any ONE of these is enough
export ANTHROPIC_API_KEY=...      # or OPENAI_API_KEY, GEMINI_API_KEY, GROQ_API_KEY,
                                  # OPENROUTER_API_KEY, MISTRAL_API_KEY, COHERE_API_KEY,
                                  # DEEPSEEK_API_KEY, XAI_API_KEY, TOGETHER_API_KEY, HF_TOKEN…
export OLLAMA_HOST=http://localhost:11434   # or nothing but a local model
export FORGE_MOCK=1                          # or nothing at all
```

Pin a model with `<PROVIDER>_MODEL`, redirect a base with
`<PROVIDER>_BASE_URL`. Check what was found:

```bash
python3 scripts/forge.py doctor
python3 scripts/model_adapters.py --list
```

---

## 6. Failure taxonomy and policy

| Class | Examples | Policy |
|---|---|---|
| Transient | timeout, network reset, 408/429/5xx, empty 200 | Retry in place, jittered exponential backoff, honour `Retry-After` |
| Parameter | 400/422 naming a rejected knob | Drop the knob, cache the fact, retry immediately |
| Model | 404 retired / unknown model | Follow the provider's suggested replacement, else next `alt_models` entry |
| Auth | 401/403 | Skip the provider entirely — retrying cannot help |
| Quota | 402, credit exhaustion | Skip the provider entirely |
| Refusal | safety block, refusal text | Distinct error; fail over to a different family rather than re-prompting |
| Contract | valid HTTP, invalid/ill-shaped JSON | Tolerant parse → coercion → focused re-ask → next provider |
| Terminal | every provider exhausted | Honest local OCR fallback (correction stage) or a clear error; **never** fabricated content |

Consistent with `API_CALLS_NEVER_STOP`: a started request is always allowed to
finish, and failure means failover, not abandonment.

---

## 7. Agent runtime compatibility

One entrypoint, one contract: `python3 scripts/forge.py <command>` →
one JSON document on stdout, logs on stderr, stable exit codes.

| Runtime | How | Glue needed |
|---|---|---|
| OpenClaw / ClawHub | `SKILL.md` + `AGENT_DISCOVERY.md` | none |
| Claude Code / Claude Desktop | `integrations/mcp_server.py` over stdio | none |
| Cursor · Windsurf · Zed · Continue · VS Code agents | same MCP server | none |
| OpenAI Agents SDK / Codex CLI | `adapters.openai_tool_spec()` | one line |
| Anthropic tool use | `adapters.anthropic_tool_spec()` | one line |
| Gemini CLI / Google GenAI | `adapters.gemini_function_declaration()` | one line |
| LangChain / LangGraph | `adapters.as_langchain_tool()` | one line |
| CrewAI | `adapters.as_crewai_tool()` | one line |
| AutoGen | `adapters.as_autogen_function()` | one line |
| LlamaIndex | `adapters.as_llamaindex_tool()` | one line |
| n8n / Zapier / shell | `adapters.n8n_execute_command()` | one line |
| GitHub Actions / cron | `adapters.github_actions_step()` | one line |

See [`integrations/README.md`](../integrations/README.md) for copy-paste
examples of each.

---

## 8. Compatibility guarantees

* **SemVer.** MAJOR breaks the CLI contract; MINOR adds commands or optional
  flags; PATCH is behaviour-compatible.
* **v1.3/v1.4 code keeps working.** Every v1.3 script, flag and invocation is still
  valid. `--providers` merely became optional, `call_provider()` kept its
  signature, and `ProviderInfo` still supports `p["name"]` / `p.get("kind")`.
* **stdout purity is permanent.** Anything added to stdout will remain a single
  JSON document.
* **Exit codes are frozen** at the values in `agent-manifest.json`.
