---
name: ai-soulmate
slug: ai-soulmate
version: 2.4.0
displayName: Your Mirror Anthropomorphic Agent
description: Anthropomorphic psychology engine based on SPL Pure Core V8.0, enabling modular modeling of cognition, emotion, motivation, and social interaction. Supports fully reproducible continuous state personality simulation with zero probabilistic black boxes. Ships a hardened minor-protection engine and cross-skill safety guards for any downstream image-prompt workflow.
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
---
# Anthropomorphic Agent Engine
A deterministic anthropomorphic psychology engine based on SPL Pure Core V8.0 with zero probabilistic black boxes. All state changes are traceable and reproducible, providing emotionally credible long-term interaction capabilities for AI agents.

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
- Black-box free auditable AI psychological simulation
- Novel/game character behavior deduction

## Core Capabilities
### 🧠 SPL Pure Core V8.0 Architecture
- 8-dimensional emotional fluid model: Joy/Anger/Fear/Trust/Alienation/Tension/Guilt/Shame, continuous state dynamic evolution
- Trauma and memory system: Trauma nodes, memory reconsolidation, Ebbinghaus forgetting curve, repression rebound mechanism
- Trust and relationship model: Trust capacity erosion under long-term cold treatment, dynamic relationship depth calculation
- Psychological metabolic system: Excitation arousal, dynamic viscosity, psychological time, energy fatigue metabolism, sleep dream processing
- V8.0 extended features: Slow variable emotional layer, independent shame dimension, dynamic self-esteem, expectation system (hope/anxiety/disappointment), cognitive dissonance, psychological defense mechanisms

### 🧩 Modular and Extensible
- Narrative mapping layer: Customizable personalities (optimistic/paranoid/cynical), converts external events into interoceptive vectors
- Identity engine: Multi-identity model, identity conflict automatically injects baseline tension
- Pluggable modules: Goals/values/cognitive biases/world models are all independent replaceable modules

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
from scripts.SPL_anthropic_engine import SPLPureCoreV8_0
core = SPLPureCoreV8_0()
# Input event vector: belonging 0.5, threat -0.1, time step 1.0
core.process_vector({"belonging": 0.5, "threat": -0.1}, 1.0)
# Get current full state snapshot
print(core.snapshot())
```

### Custom Personality Configuration
```python
# Load identity module from feature directory
from assets.feature.Identity_module import IdentityEngine
identity = IdentityEngine()
identity.add_identity("Poet", {"sensitivity": 0.9, "rationality": 0.3})
```

### Language Style Rendering
```python
# Load language style module directly
import importlib.util
spec = importlib.util.spec_from_file_location("lang_style", "assets/feature/language style.py")
lang = importlib.util.module_from_spec(spec); spec.loader.exec_module(lang)
# Generate style instructions based on SPL Core snapshot
style = lang.render_style(core.snapshot())
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
- **Added language style module** (`assets/feature/language style.py`): Discrete gear expression personality + style profile + state-to-line rendering

## Files
- `references/PersonaPersistence.md` (P0 state persistence contract)
- `references/EmotionBehaviorMap.md` (P0 emotion-behavior mapping table)
- `references/MotiveConflictRules.md` (P2 motive conflict adjudication rules)
- `scripts/SPL-anthropic-engine.py` (Core engine + NarrativeMapper + AuditLogger)
- `assets/feature/` (Identity/goals/values/biases/world/language style modules)
- `assets/minor-protection/` (Minor protection engine + HTTP service layer)
- `LICENSE` (Dual-track licensing agreement)

## Notes
- Pure Python standard library implementation, no additional dependencies required, Python ≥ 3.8
- Fully deterministic: Same input always produces same output, no random numbers
- Licensing: Dual-track model — free for personal non-commercial research, government/enterprise commercial use requires written authorization, see `LICENSE` for details
