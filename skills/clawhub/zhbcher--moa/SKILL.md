---
name: moa
description: "Mixture-of-Agents: run multiple reference models in parallel, then aggregate with current agent for deeper analysis."
metadata: {"openclaw": {"emoji": "🧠", "requires": {"anyBins": ["node"]}}}
---

# MoA (Mixture of Agents) Skill

## Agent Instructions

When the user sends a message starting with `/moa`, do NOT respond normally. Instead, execute the MoA (Mixture of Agents) pipeline:

### Pipeline

**Step 0: Notify the user (P3)**

Immediately tell the user that MoA is running:
"正在调参考模型并行分析（N 个参考模型）..."

If persistent mode is ON, prefix with:
"[MoA 持续模式 · deep preset] 正在调参考模型并行分析（3 个参考模型）..."

This gives feedback during the waiting time.

**Step 1: Parse the command**

Extract the preset name and the actual question:

- `/moa <question>` → use `default` preset, question is everything after `/moa `
- `/moa deep <question>` → use `deep` preset
- `/moa balanced <question>` → use `balanced` preset
- `/moa code-review <question>` → use `code-review` preset (task_type: coding)
- `/moa arch-review <question>` → use `arch-review` preset (task_type: architecture)
- `/moa writing <question>` → use `writing` preset (task_type: writing)
- `/moa on` → write `on` to `~/.openclaw/moa-mode-state` and reply "MoA 持续模式已开启"
- `/moa off` → write `off` to `~/.openclaw/moa-mode-state` and reply "MoA 持续模式已关闭"
- `/moa doctor` → run the executor in health mode:
  ```bash
  echo '{"mode":"health"}' | node moa-executor.js
  ```
  This checks: each provider's API key presence + endpoint reachability, prompt file syntax, preset YAML integrity. Respond with a health report.

- `/moa status` → read `~/.openclaw/moa-mode-state` (mode), read `~/.openclaw/workspace/skills/moa/presets.default.yaml` (presets), and reply with a layered status report:

```
━━━ MoA Status ━━━

=== CORE ===
Mode:          ON (persistent)  or  OFF
Preset:        deep (default: balanced)
Models:        3 references

=== ACTIVE ===
Quality Gate:  ✓ enabled (diagnostics: on)

=== HEALTH ===
Prompts:       ✓ general, coding, architecture, writing
API Keys:      ✓ SenseNova, NVIDIA, DeepSeek, Agnes
Executor:      ✓ syntax OK
State:         ✓ ~/.openclaw/moa-mode-state readable
```

(Health info is a lightweight check — if any check fails, list the failure.)

Also: if persistent MoA mode is on (check if `~/.openclaw/moa-mode-state` contains `on`), run the MoA pipeline for EVERY user message automatically, not just `/moa` commands.

**Step 2: Read the preset configuration**

Read the file `~/.openclaw/workspace/skills/moa/presets.default.yaml` and find the matching preset.

**Step 3: Build the executor input**

Build a JSON object with the preset config and the user's question as the `conversation` field.

**Step 4: Call reference models via the executor**

API keys are read from environment variables. OpenClaw injects them automatically — configure in `openclaw.json`:
```json5
{
  skills: {
    entries: {
      moa: {
        enabled: true,
        env: {
          SENSENOVA_API_KEY: "<your-key>",
          NVIDIA_API_KEY: "<your-key>",
          DEEPSEEK_API_KEY: "<your-key>",
          AGNES_API_KEY: "<your-key>",
        },
      },
    },
  },
}
```

Then run:
```bash
cd ~/.openclaw/workspace/skills/moa
echo '<JSON_INPUT>' | node moa-executor.js
```

The input JSON supports optional fields:
```json
{
  "preset": {...},
  "conversation": "...",
  "task_type": "coding",
  "presetName": "deep",
  "max_tokens": 1500
}
```

- `task_type`: `coding`, `architecture`, `writing`, `general` (default)
- `presetName`: used for `MOA_MODEL_<PRESET>_<N>` env var model overrides
- `max_tokens`: override per-model output token limit (P2: user-customizable)

**Step 5: Collect reference outputs**

The executor returns JSON with:
```json
{
  "references": [
    {
      "provider": "...",
      "model": "...",
      "output": "...",
      "latency_ms": 4230,
      "reference_rank": 82,
      "quality_class": "good",
      "quality_gate": {"passed": true, "reason": "ok", "diagnostics": {"length": 1682, "refusal": false, "api_error": false, "truncated": false}},
      "usage": {...},
      "cost": {...}
    },
    ...
  ],
  "quality_stats": {"passed": 2, "rejected": 1, "rejections": {"too_short": 1}},
  "elapsed_ms": 1234,
  "usage": {...},
  "cost_usd": 0.001
}
```

**Step 6: Inject reference outputs and respond as aggregator**

Include the reference model outputs in your response context. Include latency, reference rank, and quality class:

```
[MoA — N references · X.Xs · ~$X.XXX | Quality: +N/-N]
[Ref 1 / provider/model · X.Xs · rank: XX (good)]: <output>
[Ref 2 / provider/model · X.Xs · rank: XX (ok)]: <output>
...
[Quality rejected: N responses filtered (too_short: N, refusal: N, api_error: N)]
[User's original question]: <question>
```

Reference rank is an internal sort key (0-100). Quality class is the semantically meaningful label:
- `good` — substantial, fast, untruncated
- `ok` — usable but not exceptional
- `bad` — filtered out before reaching aggregator

Then respond as the aggregator: synthesize the reference perspectives, use your own judgement, and produce the final answer with normal tool access.

When a `task_type` is specified, the advisory prompt used for reference models is tailored:
- `coding`: Code reviewer mode — focus on bugs, give patches
- `architecture`: Architecture reviewer — scalability, boundaries, coupling
- `writing`: Editor mode — clarity, flow, readability
- `general` (default): Standard MoA analysis

**Step 7: If persistent mode, show state and remember**

If `/moa on` was set:
- Next user message (even without `/moa`) should repeat steps 2-6 automatically
- At the start of the MoA output, include the mode and preset info in the header line:
  - If no specific preset was requested: `[MoA — Persistent · 3 refs · …]`
  - If a preset was specified via `/moa deep <q>` with mode ON: `[MoA — Persistent · deep preset · 3 refs · …]`
- Also include a footer: `[MoA mode is ON. Run /moa off to disable. Run /moa status for details.]`
- Check `~/.openclaw/moa-mode-state` at the start of each message

### Configuration

Six presets available:

| Preset | References | Timeout | Best for |
|--------|-----------|---------|----------|
| `default` | sensenova/dsv3-flash ×1 | 60s total | Quick single reference |
| `balanced` | sensenova/dsv3-flash + nvidia/step-3.7-flash | 90s total | Daily work, 2 diverse perspectives |
| `deep` | dsv3-flash + step-3.7-flash + step-3.5-flash | 120s total | Hard problems, 3 references |
| `code-review` | dsv3-flash + step-3.7-flash, `task_type: coding` | 90s total | Code bug finding with patch output |
| `arch-review` | nemotron-3-ultra + dsv3-flash, `task_type: architecture` | 120s total | Architecture/design review |
| `writing` | dsv3-flash + step-3.7-flash, `task_type: writing` | 90s total | Editing and prose improvement |


Key config fields:
- `reference_max_tokens`: max advisor output length
- `reference_temperature`: advisor creativity (0-1)
- `timeout_seconds`: per-model timeout
- `total_timeout_seconds`: global timeout for all references combined (P1)
- `task_type`: `general` | `coding` | `architecture` | `writing` — selects tailored advisory prompt
- `keep_top_k`: max references to keep after quality gate + scoring (default: all)

### Supported providers

API keys are injected via OpenClaw's `skills.entries.moa.env` config. Supported providers:

| Provider | Models | Env var |
|----------|--------|---------|
| SenseNova | `deepseek-v4-flash`, `sensenova-6.7-flash-lite` | `SENSENOVA_API_KEY` |
| NVIDIA | `stepfun-ai/step-3.7-flash`, `stepfun-ai/step-3.5-flash` | `NVIDIA_API_KEY` |
| DeepSeek | `deepseek-v4-pro`, `deepseek-v4-flash` | `DEEPSEEK_API_KEY` |
| Agnes | `agnes-2.0-flash` | `AGNES_API_KEY` |
| OpenAI | gpt models | `OPENAI_API_KEY` |
| Anthropic | claude models | `ANTHROPIC_API_KEY` |
| Google | gemini models | `GEMINI_API_KEY` |
| xAI | grok models | `XAI_API_KEY` |
| OpenRouter | multi-provider | `OPENROUTER_API_KEY` |
| Together | open-source models | `TOGETHER_API_KEY` |
| Moonshot | kimi models | `MOONSHOT_API_KEY` |

### Model name overrides (P3)

Model names in presets can be overridden without editing presets.yaml. Two mechanisms available, with this priority order (highest wins):

```
1. MOA_MODEL_<PRESET>_<N>      ← 最高优先级，精确到某个预设的某个模型
2. MOA_MODEL_MAP JSON           ← 中间优先级，全局按 provider/model 映射
3. presets.default.yaml 默认值   ← 最低优先级，兜底
```

**Option A: Per-preset, per-index override** (highest priority)
```bash
# MOA_MODEL_<PRESETNAME>_<INDEX>
# 只覆盖 deep 预设的第 0 个模型
# presetName 会转为全大写，非字母数字变下划线
export MOA_MODEL_DEEP_0='nvidia/step-3.7-ultra'
export MOA_MODEL_DEEP_1='nvidia/stepfun-ai/step-3.5-flash'
```

**Option B: Global model map JSON** (medium priority)
```bash
# 按 "provider/model" 或裸 "model" 名匹配
export MOA_MODEL_MAP='{"sensenova/deepseek-v4-flash":"sensenova/new-flash-model"}'
```

**Migration from v1.0.0:** 如果之前通过 `source /tmp/set-moa-keys.sh` 加载，迁移到 openclaw.json 即可——key 内容不变，只是注入方式从磁盘文件改为 OpenClaw 运行时注入。不需要改 presets YAML。

### max_tokens override (P2)

You can pass `max_tokens` in the executor input to override the preset's default reference output length:
```bash
echo '{"preset":{...},"conversation":"...","max_tokens":1500}' | node moa-executor.js
```

Or use the recommended preset defaults:
| Preset | Default max_tokens |
|--------|-------------------|
| default | 512 |
| balanced | 800 |
| deep | 1024 |
| code-review | 1024 |
| arch-review | 1200 |
| writing | 800 |

### Cost

- NVIDIA models are free ($0)
- SenseNova/DeepSeek models ~$0.001-0.01 per MoA call

## Examples

```
/moa 设计一个高并发的消息队列架构
/moa deep 分析这段代码的性能瓶颈
/moa code-review 检查这个函数的性能问题
/moa arch-review 评估这个微服务架构
/moa writing 帮我润色这段产品文案
/moa on
/moa off
/moa status
/moa doctor          Run health diagnostics (API key presence, endpoint reachability, prompt syntax)
```

### Internal pipeline details

1. **Quality Gate (P1 Enhanced)** — Every reference response is checked before reaching the aggregator:
   - Empty/short responses (< 50 chars) → filtered
   - Refusals (EN + CN: 24 patterns) → filtered
   - API errors / rate limits → filtered
   - Low-quality signals: hedging density (>15%), repetition detection → rank penalized
   - If ALL references are rejected, falls back to preserving raw results

2. **Error Isolation (P3)** — Individual model failures are logged and isolated. The pipeline continues with remaining successful models instead of crashing. Failed references are reported separately.

2. **Unified decision (`shouldKeepReference`)** — A single function centralizes all filter/gate decisions:
   - Quality gate (hard reject: empty/refusal/API-error responses)
   - Quality classification (`good`/`ok`/`bad`)
   - Reference rank heuristics (length, latency, token usage, truncation)
   - All decisions go through one entry point, no scattered `if` conditions

3. **Reference Metadata** — Each reference includes:
   - `latency_ms`: wall clock time for the API call
   - `reference_rank`: internal sort key (0-100, avoids "score" cross-provider illusion)
   - `quality_class`: `good` | `ok` | `bad` (semantically meaningful label)
   - `quality_gate`: pass/fail result with reason and diagnostics:
     - Reason: `ok` / `too_short` / `refusal` / `api_error` / `error` / `fallback_all_rejected`
     - Diagnostics: `{length, refusal, api_error, truncated}` (debug info for why)
   - `usage` and `cost`: token and cost breakdown
   - `provider` and `model`: identification

### Quality stats in output

The executor now returns `quality_stats` showing how many references passed/rejected:
```json
{
  "references": [...],
  "quality_stats": {
    "passed": 2,
    "rejected": 1,
    "rejections": {"too_short": 1}
  }
}
```

## Related

- [Mixture-of-Agents Enhances Large Language Model Capabilities](https://arxiv.org/abs/2406.04692)