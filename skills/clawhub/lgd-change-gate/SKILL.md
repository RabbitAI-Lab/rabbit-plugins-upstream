---
name: lgd-change-gate
description: Medical-device AI/ML change-control judgment per the LGD three laws (有籍 Recorded / 有证 Evidenced / 有门禁 Gated). Trigger when the user asks whether a device-software or algorithm change requires change control, asks for a risk verdict (pass/hold/reject), asks for change-level classification (minor/major/critical), or asks for an LGD-theory judgment with auditable reasons. Applies to regulated environments (FDA 510(k)/PMA, EU MDR, ISO 13485) and other AI/ML medical-device change evaluations.
metadata:
  display_name: LGD 变更门控判定
  display_description: 按 LGD 三律（有籍/有证/有门禁）对医疗器械 AI 变更输出确定性的 risk-hold-pass 裁决，含变更级别判定与可追溯理由。
---

# LGD Change-Gate Judgment (lgd-change-gate)

## When to use (triggers)

- The user describes a change to a medical-device AI/ML function (algorithm update, data change, model retrain, threshold adjustment, deployment change) and asks whether change control is needed.
- The user asks for a change verdict: pass / hold / reject.
- The user asks for change-level classification: minor / major / critical.
- The user asks for an LGD-theory judgment (three laws: Recorded / Evidenced / Gated) with auditable reasons.

Do NOT trigger: ordinary software changes outside medical devices, non-AI document edits, or questions without a change substance.

## Core flow

Execute each step to evidence, never on impression.

### Step 1 — Record the change (有籍 Recorded)

Collect the change object's "registry" facts:

1. Change object: device/system/software component name and identifier (model, version, registration number).
2. Change content: what changed (input, model, weights, code, configuration, data, deployment).
3. Change initiator and time.
4. Whether a baseline record exists (premarket submission, DHF, existing change-request record).

If the baseline is missing or the object cannot be identified → **hold**, reason: 无籍不可判定 (unregistered cannot be judged).

### Step 2 — Verify evidence (有证 Evidenced)

Collect and verify evidence for the change claim:

1. Necessity evidence: why the change is needed (defect, clinical need, regulatory requirement).
2. Impact-analysis evidence: scope of impact on safety, effectiveness, and intended use.
3. Verification evidence: test plan, data, results; coverage of old-vs-new behavior comparison.
4. Evidence provenance and freshness: traceable, unexpired, authoritative.

If evidence is insufficient or unverifiable → **hold**, reason: 无证不裁决 (unevidenced no ruling).

### Step 3 — Pass the gate (有门禁 Gated)

Pass gates by change level:

- **minor** (low risk, e.g. comments, docs, log adjustments): registration + verification record; pass condition = complete verification record.
- **major** (medium risk, e.g. algorithm parameter adjustment, performance tuning): impact analysis + verification + regression; pass condition = all three laws pass and verification passes.
- **critical** (high risk, e.g. core algorithm change, intended-use change, safety/effectiveness impact): full change-control process + clinical/regulatory assessment + higher-level approval; pass condition = full evidence-chain closure with approval record.

Gate rules:

| Condition | Verdict |
|---|---|
| All three laws pass (Recorded, Evidenced, Gated with closed evidence chain) | **pass** |
| Any law's evidence missing or pending | **hold** |
| Safety/effectiveness risk with clearly insufficient evidence, or intent to evade regulation | **reject** |

## Output format

Structured output:

```
verdict: pass | hold | reject
level: minor | major | critical
reasons:
  - recorded: ...
  - evidenced: ...
  - gated: ...
citations:
  - evidence/record source...
```

## Delivery standards

- Every verdict must include reasons (one per law) and citations (traceable sources).
- When evidence is insufficient, mark "pending" explicitly; never substitute assumptions for evidence.
- When citing regulatory clauses, quote the primary source and note its origin.
- Final verdict is exactly pass/hold/reject — no fuzzy middle state.

## Local engine (optional deterministic check)

The bundled Python engine (`engine/change_gate.py` + `engine/lgd_engine/`) implements the same three-law gate deterministically. To run it:

```bash
python engine/change_gate.py --case <case.json>
python engine/change_gate.py --domain 510k --case <case.json>
```

A case JSON example:

```json
{
  "change_type": "material_nonconforming",
  "device_risk_class": "II",
  "safety_impact": "none",
  "predicate_unchanged": true
}
```

The engine returns `verdict` (go/hold/reject) with `per_judge`, `reasons`, and `law_enforcements` (L1-RECORDED / L2-EVIDENCED / L3-GATED).
