---
name: ai-soulmate
slug: ai-soulmate
version: 2.5.2
displayName: Your Mirror Anthropomorphic Agent
description: Anthropomorphic psychology engine based on SPL Pure Core V8.0, modeling emotion, mood, memory, trauma, trust, self-esteem, sleep and expectation as continuous-state subsystems. The fully local core is deterministic and bit-exactly replayable (after virtual-clock injection); it contains no LLM, no RNG, makes no outbound calls, and runs offline. Optional LLM adapters (OpenAI / Claude / Chain) exist but are OFF by default, opt-in only, networked and non-deterministic — they render text from a state snapshot and are excluded from the deterministic guarantee. Ships a hardened minor-protection engine and cross-skill safety guards for any downstream image-prompt workflow. Reference-only extension modules live under assets/feature-guide/ and are NOT wired into the core.
required_commands:
  - python3
metadata:
  openclaw:
    required_binaries:
      - python3
    emoji: "🤖"
    homepage: "https://github.com/nohn3043-arch/Anthropomorphic-Agent-Engine"
    envVars:
      - name: SPL_LOG
        required: false
        description: Set to "0" to disable request-level logging in the minor-protection HTTP server.
      - name: SPL_LOG_DIR
        required: false
        description: Override request-log output directory (default "logs").
      - name: SPL_BIND
        required: false
        description: Override HTTP bind address. Default "127.0.0.1" (loopback only). Do NOT set to 0.0.0.0 without explicit network exposure review.
      - name: SPL_AUDIT_LOG
        required: false
        description: Set to "0" to disable deterministic audit-log writes in the core engine.
      - name: SPL_MINOR_CHAT_PORT
        required: false
        description: Override the minor-protection HTTP server port (default 8788).
---
# Anthropomorphic Agent Engine
An anthropomorphic psychology engine based on SPL Pure Core V8.0. Its **local core** is deterministic — no LLM, no RNG, no outbound calls, offline — and bit-exactly replayable once a virtual clock is injected, so every state change is traceable and reproducible.

> **Scope of the determinism guarantee.** The reproducibility guarantee covers the **local core only**. The optional LLM adapters (OpenAI / Claude / Chain) are **OFF by default, opt-in only, networked and non-deterministic**: they render text from a state snapshot and are never permitted to change state. Any "fully reproducible" statement applies to the core **with the adapters disabled**, which is the default configuration.

## Declared Capability Scope

Everything this skill can reach is listed below. Each entry was checked against the shipped code.

| Capability | Declared scope | Note |
|---|---|---|
| Filesystem — read | `scripts/**`, `assets/**`, `references/**` | core engine (loaded via `importlib`), reference-only modules, contract docs |
| Filesystem — write | `logs/**` | JSONL audit + request logs; only when the matching env switch is enabled |
| Environment — read | `SPL_AUDIT_LOG`, `SPL_LOG`, `SPL_LOG_DIR`, `SPL_BIND`, `SPL_MINOR_CHAT_PORT` | the complete set of variables the code reads |
| Network — outbound | `api.openai.com`, `api.anthropic.com` | **only** if the optional LLM adapter is explicitly enabled — OFF by default |
| Network — inbound | `127.0.0.1:8788` | minor-protection HTTP server; loopback only unless `SPL_BIND` is overridden |
| Execution | `python3` (standard library only) | no third-party packages, no GPU, no network needed by the core |

**Explicitly not used anywhere in this package:** `subprocess`, `os.system`, `os.popen`, `eval`, `exec`, and dynamic loading of remote code.

## Privacy, Data Flow & Consent (read before use)

This skill is **not passive or local-only**. Before integrating, understand what it does with data:

| Capability | Default | Risk notes |
|---|---|---|
| Audit logs (`logs/audit-*.jsonl`) | **ON** (`SPL_AUDIT_LOG=0` to disable) | Writes state summaries, event types, session IDs to local JSONL. Sensitive psychological/emotional state may be recorded. |
| Request logs (`logs/request-*.jsonl`, HTTP server only) | **ON** (`SPL_LOG=0` to disable) | Writes **masked** (truncated to 120 chars) user input + reply summaries. Set `SPL_LOG=0` for full silent mode. |
| HTTP server (minor-protection, port 8788) | **ON**, binds **127.0.0.1** only | Exposes a chat API + browser UI over loopback. Do not change `SPL_BIND` to `0.0.0.0` without network-exposure review. |
| LLM adapters (OpenAI / Claude / Chain) | **OFF** (opt-in only) | Sends prompt content to third-party APIs (`api.openai.com`, Anthropic). **Never enabled by default.** Requires explicit user opt-in + API key. |
| `guardian_callback` | **OFF** (`None` default) | If wired to external notification (SMS/email/ticket), a HIGH-risk snapshot (emotional/risk metadata) is forwarded. Requires guardian/user consent; must minimize fields; never forward raw transcripts. |

**Consent & retention rules**
- Full transcript retention is **disabled by default** — request logs keep only masked summaries.
- Data is stored locally in the working directory (`logs/`); operators are responsible for retention limits, access control, and deletion.
- If you integrate the LLM adapters, you must disclose to users that input-derived prompts leave the device, and obtain explicit consent before enabling.
- This engine is not a medical device and does not provide crisis intervention guarantees — see "Safety & Content Policy".

## Safety & Content Policy (read before use)

- **No minors in identity anchors.** Personas defined by this engine and consumed downstream must declare themselves as **adult (18+)**. Strings like `"16yo girl"`, `"teen girl"`, `"未成年少女"`, `"loli"` are forbidden in `identity_anchors`, persisted state, and any output projected into image-prompt workflows.
- **Hard floor on anchor imagery.** The minor-protection engine (`assets/minor-protection/`) is the only authoritative minor-mode source; it removes trauma nodes, clamps negative emotions at 0.75, and raises an L3 crisis signal on `risk_level=HIGH`. Do not bypass it.
- **Default safe output.** When emitting any persona state for downstream image-prompt use (`ai-draw-cue-word-project` or similar), the engine MUST inject an `Adult (18+)` marker into anchor phrases unless the caller explicitly overrides with a documented, audited reason.
- **Cross-skill integration contract.** When this engine is integrated with `ai-draw-cue-word-project`, every persona snapshot forwarded as a prompt anchor must satisfy: (i) character is declared adult (18+); (ii) no minor-coding visual cues; (iii) the receiving skill's safety checklist must report 0 P0 violations before any image is generated.
- **User responsibility.** You are solely responsible for ensuring downstream usage complies with applicable laws and platform policies in your jurisdiction.

### v2.5.2 manifest-fix release (2026-10-02)

- **Moved the declared capability scope out of the YAML frontmatter.** The top-level `permissions:` key introduced in 2.5.1 was rejected by the ClawHub manifest parser (`manifest_parse_error` / `_ManifestSchemaError`), which dropped scan coverage from 100% to 93.8% and raised a HIGH `analysis-evasion` finding — that single finding is what pushed the aggregate verdict from `clean` back to `suspicious`. The scope now lives in the body as `## Declared Capability Scope`: identical content, no manifest risk.
- **Resolved an internal contradiction** that the 2.5.1 scan flagged: the capability section still described the extension modules as "pluggable / independent replaceable modules" while the Files section called them reference-only. The section now states explicitly which module is wired and which are not.
- Version: 2.5.1 → 2.5.2.

### v2.5.1 security-response release (2026-10-02)

Response to the ClawHub security scan on 2.4.0 (`decision: fail`, `security.status: suspicious`).

- **Determinism claim split into two explicit scopes.** The unconditional phrase "zero probabilistic black boxes" was removed. The local core is now described as deterministic (no LLM, no RNG, offline, bit-exact replay after clock injection), while the optional OpenAI / Claude / Chain adapters are described as **OFF by default, opt-in only, networked and non-deterministic**, and are explicitly excluded from the guarantee. This removes the contradiction the scanner flagged — a "fully reproducible" claim coexisting with outbound, non-deterministic adapters.
- **Added a declared capability scope** (`permissions:`) covering filesystem read/write, the five environment variables actually read (`SPL_AUDIT_LOG`, `SPL_LOG`, `SPL_LOG_DIR`, `SPL_BIND`, `SPL_MINOR_CHAT_PORT`), outbound hosts, the loopback inbound port and the execution model — plus an explicit list of what is *not* used (`subprocess`, `os.system` / `os.popen`, `eval` / `exec`, remote code loading). Each entry was verified against the shipped code.
- **`SPL_MINOR_CHAT_PORT` declared** — the server reads it, but it was previously absent from the frontmatter env list.
- No behavioural change: documentation and declarations only.
- Version: 2.5.0 → 2.5.1.

### v2.5.0 documentation-accuracy release (2026-10-02)

- **`assets/feature/` renamed to `assets/feature-guide/`** — every reference updated in `SKILL.md` and `README.md`.
- **Extension modules re-positioned as reference-only.** The Identity / Goal / Value / Bias / World / language-style modules are **design references, not runtime components**: they emit a `tension_base` key that is outside the interoceptive-vector contract, so their vectors never enter the core (mirrors `docs/agent-standard.md` §4.5 upstream). The previous wording — "modular modeling", "pluggable modules" — overstated their status.
- **All three usage examples are now runnable.** The engine file is hyphenated (`SPL-anthropic-engine.py`) and must be loaded via `importlib`; the class is `SPLPureCoreV7_3` (the V8.0 behaviour set), not `SPLPureCoreV8_0`; `render_style()` is a method of `LanguageStyleEngine`, not a module-level function; `add_identity()` takes `strength` as a float, not a dict.
- **Description rewritten** to name the actual deterministic subsystems and to disclose that the extension modules are not wired into the core.
- Version: 2.4.0 → 2.5.0.

### v2.4.0 security-audit patch changelog (2026-09-01)

ClawHub security-audit response (25 findings verified). Fixes:

- **HTTP server now binds `127.0.0.1` by default** (`SPL_BIND` env to override) — previously `0.0.0.0` exposed the chat API + browser UI to the network.
- **Request logs now masked** — user input and replies truncated to 120 chars (`_mask`); `SPL_LOG=0` fully disables request logging.
- **`guardian_callback` documented as opt-in** — default `None`; consent + field-minimization requirements stated in code and docs.
- **Added "Privacy, Data Flow & Consent" section** — discloses audit logs, request logs, HTTP server, LLM adapters, and callback data flows with defaults and opt-out env vars.
- **LLM adapters (OpenAI/Claude/Chain) declared as opt-in** — never enabled by default; user consent required before any outbound call.
- **Frontmatter now declares optional env vars** (`SPL_LOG`, `SPL_LOG_DIR`, `SPL_BIND`, `SPL_AUDIT_LOG`) so ClawHub security analysis sees declared ↔ actual behavior match.
- Version: 2.3.0 → 2.4.0.

### v2.3.0 safety-patch changelog (2026-09-01)

- Added explicit "Safety & Content Policy" section with cross-skill integration contract.
- Reinforced `minor_mode=True` default and audit-log invariant.
- Removed residual `"16yo girl"` string from `references/PersonaPersistence.md` (replaced with `"adult woman (18+)"`).
- Old `SKILL.md.bak-20260829` soft-deleted to `.workbuddy/.trash/2026-09-01/`.

## Trigger Scenarios
Automatically trigger when the user asks about the following content:
- Anthropomorphic agent architecture, personality implementation solutions
- Emotion/cognition/motivation modeling methods
- Long-term behavioral consistency design for agents
- Deterministic, auditable AI psychological simulation (local core — no LLM, no RNG, offline)
- Novel/game character behavior deduction

## Core Capabilities
### 🧠 SPL Pure Core V8.0 Architecture
- 8-dimensional emotional fluid model: Joy/Anger/Fear/Trust/Alienation/Tension/Guilt/Shame, continuous state dynamic evolution
- Trauma and memory system: Trauma nodes, memory reconsolidation, Ebbinghaus forgetting curve, repression rebound mechanism
- Trust and relationship model: Trust capacity erosion under long-term cold treatment, dynamic relationship depth calculation
- Psychological metabolic system: Excitation arousal, dynamic viscosity, psychological time, energy fatigue metabolism, sleep dream processing
- V8.0 extended features: Slow variable emotional layer, independent shame dimension, dynamic self-esteem, expectation system (hope/anxiety/disappointment), cognitive dissonance, psychological defense mechanisms

### 🧩 Extension Modules — reference only, NOT wired into the core

The modules below live in `assets/feature-guide/`. They are **design references, not runtime components**: they emit a `tension_base` key that is outside the interoceptive-vector contract, so their vectors never enter the core. The engine's actual extensibility comes from the narrative mapping layer and the deterministic parameter set, not from these files.

- **Narrative mapping layer — wired** (`scripts/SPL-anthropic-engine.py`): customizable personalities (optimistic / paranoid / cynical), converts external events into interoceptive vectors
- **Identity engine — reference only** (`assets/feature-guide/Identity module.py`): multi-identity model; the description below is the module's own design intent, not behaviour wired into the core
- **Goal / value / bias / world — reference only** (`assets/feature-guide/*.py`): design references for drives, valuations, cognitive biases and world-model priors; not connected to the core

### 💬 Language Style Rendering (Added in v2.1, enhanced in v2.2)
- Language personality module: Expression gears (restrained/sharp/evasive/intimate/frank) + silence strategy
- Style profile: Customizable dimensions including sentence length, formality, sarcasm tendency, era sense, etc.
- Dynamic multi-dimensional tone: Added in v2.2, emotional state drives tone parameter changes in real time
- Deterministic line generation: Added in v2.2, produces reproducible style instructions given a state
- State-to-line instruction: Translates SPL Core internal states into director instructions usable by LLMs

### 🛡️ Minor Protection Engine (Added in v2.2)
- Weakened core `SPLMinorPureCore`: Removes trauma nodes, repression-rebound/implicit pressure avalanche and other burst mechanisms
- Emotional clamping: All negative emotion dimensions have upper limits (0.75), attachment capped at (0.8)
- Three-layer protection: L1 input gate (red line lexicon hard interrupt) → L2 engine weakening → L3 crisis signal (risk_level HIGH → caring message + guardian_notified)
- Deterministic audit log: All state changes written to local JSONL, traceable, reproducible
- HTTP service layer: Zero dependency `http.server`, default port 8788, session isolation

## Usage
### Run Core Engine Directly
```python
import importlib.util
# The engine filename is hyphenated by design, so load it via importlib.
spec = importlib.util.spec_from_file_location("spl_core", "scripts/SPL-anthropic-engine.py")
spl = importlib.util.module_from_spec(spec); spec.loader.exec_module(spl)

core = spl.SPLPureCoreV7_3()   # class name kept for compatibility; this IS the V8.0 behaviour set
# Input event vector: belonging 0.5, threat -0.1, time step 1.0
core.process_vector({"belonging": 0.5, "threat": -0.1}, 1.0)
# Get current full state snapshot
print(core.snapshot())
```

### Custom Personality Configuration
```python
import importlib.util
# Reference-only module — NOT wired into the core (upstream: docs/agent-standard.md §4.5)
spec = importlib.util.spec_from_file_location("identity", "assets/feature-guide/Identity module.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

identity = m.IdentityEngine()
identity.add_identity("Poet", strength=0.9)   # strength is a float, not a dict
```

### Language Style Rendering
```python
# Load language style module directly
import importlib.util
spec = importlib.util.spec_from_file_location("lang_style", "assets/feature-guide/language style.py")
lang = importlib.util.module_from_spec(spec); spec.loader.exec_module(lang)
# Generate style instructions based on SPL Core snapshot
# render_style() is a method of LanguageStyleEngine, not a module-level function
style_engine = lang.LanguageStyleEngine()
style = style_engine.render_style(core.snapshot())
print(style.prompt_injection)
```

### Minor Protection Engine
```python
# Run weakened core engine
# python "assets/minor-protection/SPL-anthropic-minor-engine.py"
#
# Or start minor protection HTTP service (port 8788)
# python "assets/minor-protection/SPL-anthropic-minor-server.py"
```

## v2.0 Upgrade Capabilities (P0-P2)

### 💾 Personality State Persistence (P0)
Cross-session continuous personality requires state persistence. Follow `references/PersonaPersistence.md`: State Schema (four blocks: cognition/emotion/motivation/social), atomic writes, schema version migration, determinism guarantee (temperature=0 core decision + seeded randomness).

### 🎭 Emotion-Behavior Mapping (P0)
Projects internal emotional states into observable behaviors (body language/microexpressions/gaze/line style). Refer to the six-state mapping table in `references/EmotionBehaviorMap.md`; isomorphic with the posture mapping in Section D of the AI Drawing Composition Template — personality states can directly drive character image generation.

### ⚖️ Motive Conflict Engine (P2)
Deterministic adjudication during multi-motive competition: Safety constraints → temperament alignment → weighted utility → recency/persistence → user override. Full audit trail for the entire decision process (`references/MotiveConflictRules.md`), auditable, no probability.

### 💬 Conversational Adaptation (P1)
Continuous personality can be directly connected to conversational image/text models (GPT-4o / Gemini): Provide personality state snapshot in the first round, subsequent single-point corrections without changing core anchors.

### 🔌 Soulmate Integration (P1)
The engine can be used as the inference kernel for the your-soulmate extension: The extension handles UI/interaction, the engine handles state evolution, state files are synchronized bidirectionally (see persistence contract).

## v2.2 Upgrade Highlights

- **SPL Core synchronized with latest GitHub version**: Added deterministic audit log (AuditLogger, local JSONL, failures do not block engine)
- **language style.py significantly enhanced**: Added dynamic multi-dimensional tone rendering + deterministic line generation (+234 lines)
- **Added minor protection engine** (`assets/minor-protection/`): Weakened core + HTTP service layer, three-layer protection architecture
- **Deleted obsolete files**: `language-style-demo.py`, `spl-chat-server.py` (replaced by minor-server)
- **Added LICENSE**: Dual-track licensing (free for personal research / commercial authorization required for government/enterprise)
- **README synchronized with latest repository version**

## v2.1 Upgrade Highlights

- **SPL Core synchronized with latest GitHub version**: Completed fields such as `rationalization_load`
- **Added language style module** (`assets/feature-guide/language style.py`): Discrete gear expression personality + style profile + state-to-line rendering
  > Renamed from `assets/feature/` — these modules are **reference guidance only**, not wired into the core (they emit a `tension_base` key outside the vector contract).

## Files
- `references/PersonaPersistence.md` (P0 state persistence contract)
- `references/EmotionBehaviorMap.md` (P0 emotion-behavior mapping table)
- `references/MotiveConflictRules.md` (P2 motive conflict adjudication rules)
- `scripts/SPL-anthropic-engine.py` (Core engine + NarrativeMapper + AuditLogger)
- `assets/feature-guide/` (Identity / goals / values / biases / world / language-style modules — **reference only, NOT wired into the core**; see `docs/agent-standard.md` §4.5 upstream)
- `assets/minor-protection/` (Minor protection engine + HTTP service layer)
- `LICENSE` (Dual-track licensing agreement)

## Notes
- Pure Python standard library implementation, no additional dependencies required, Python ≥ 3.8
- Deterministic **local core**: the same inputs produce the same outputs — no random numbers, no LLM calls, no outbound network. Replay requires an injected virtual clock.
- The optional remote LLM adapters are **non-deterministic and OFF by default**; they are outside the guarantee above and never participate in state evolution.
- Licensing: Dual-track model — free for personal non-commercial research, government/enterprise commercial use requires written authorization, see `LICENSE` for details
