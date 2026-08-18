# SkillOpt Paper Summary

## Paper Info
- **Title:** SkillOpt: Executive Strategy for Self-Evolving Agent Skills
- **Authors:** Yifan Yang, Ziyang Gong, Weiquan Huang, et al. (Microsoft Research)
- **Published:** May 2026 (arXiv:2605.23904)
- **GitHub:** https://github.com/microsoft/skillopt (15.5K+ stars)
- **Pages:** 27 pages, 4 figures, 6 tables

## Core Thesis

Agent skills today are:
1. Hand-crafted (inconsistent quality)
2. Generated one-shot by LLMs (no iterative improvement)
3. Evolved through loosely controlled self-revision (unreliable)

**None of these behave like a deep-learning optimizer for the skill.**

SkillOpt argues: **the skill should be trained as the external state of a frozen agent**, with the same discipline that makes weight-space optimization reproducible.

## Methodology

### The Pipeline

```
Rollout → Reflect → Aggregate → Select → Update → Gate → (Slow Update) → Epoch Boundary
```

1. **Rollout:** Target model executes tasks using the current skill document
2. **Reflect:** Separate optimizer model analyzes trajectories, produces edit patches
3. **Aggregate:** Merge multiple edit patches into candidates
4. **Select:** Rank edits, apply learning rate (max edits per step)
5. **Update:** Apply selected edits to skill document
6. **Gate:** Validate on held-out set. Accept ONLY if score improves.
7. **Slow Update:** Epoch-boundary longitudinal update (consolidate learnings)
8. **Meta Skill:** Cross-epoch optimizer memory

### Deep Learning Analogy

| Deep Learning | SkillOpt |
|---|---|
| Model weights | Skill document (Markdown) |
| Forward pass | Rollout (target executes tasks) |
| Loss / gradient | Reflect (optimizer produces edit patches) |
| Gradient clipping | Edit selection (learning_rate = max edits) |
| SGD step | Patch application to skill |
| Validation set | Gated evaluation on selection split |
| LR schedule | lr_scheduler: cosine, linear, constant |
| Epochs | Multi-epoch with slow update & meta skill memory |

### Key Mechanisms

**Textual Learning Rate:**
- Max number of edit patches per step (default: 4)
- Prevents overfitting / over-editing
- Schedules: cosine, linear, constant, autonomous

**Validation Gate:**
- Candidate edit accepted ONLY when it strictly improves held-out validation score
- Prevents regressions
- Can be configured: hard gate (strict), soft gate (weighted), mixed

**Rejected-Edit Buffer:**
- Rejected edits are stored, not discarded
- Alternative formulations tried in next pass
- Prevents losing useful insights

**Slow Update:**
- Epoch-boundary longitudinal update
- Uses 20+ evaluation samples
- Consolidates learnings across epochs

**Meta Skill:**
- Cross-epoch optimizer memory
- Remembers what types of edits work
- Improves optimizer's own strategy over time

## Results

### Performance

| Benchmark | Improvement |
|---|---|
| SpreadsheetBench | 41% → 80% accuracy |
| DocVQA | 33% → 72% accuracy |
| Average across 6 benchmarks | +23.5 points (GPT-5.5, direct chat) |

### Key Findings

1. **Best or tied on ALL 52 evaluated (model, benchmark, harness) cells**
2. On GPT-5.5:
   - +23.5 points in direct chat
   - +24.8 inside Codex agentic loop
   - +19.1 inside Claude Code
3. **Transfer:** Optimized skills retain value when moved:
   - Across model scales
   - Between Codex and Claude Code
   - To nearby benchmarks without further optimization

### Comparison

SkillOpt beats:
- Human-crafted skills
- One-shot LLM-generated skills
- Trace2Skill
- TextGrad
- GEPA
- EvoSkill

## Implementation Details

### Architecture
- Python package: `pip install skillopt`
- Backends: OpenAI, Azure, Claude, Qwen, MiniMax, Copilot
- Execution harnesses: Direct chat, Codex CLI, Claude Code CLI
- WebUI dashboard for monitoring

### Configuration
- YAML-based config with inheritance
- Separate optimizer and target model roles
- Benchmarks as pluggable adapters
- ~100 lines of code to add new benchmark

### SkillOpt-Sleep (v0.2.0)
Nightly offline self-evolution:
```
harvest sessions → mine recurring tasks → replay → consolidate → gate → stage proposal → adopt
```
- Reviews past coding agent sessions
- Replays recurring tasks
- Consolidates validated skills
- Staged for human review before adoption

## Limitations

1. Requires scored rollouts (benchmark tasks with clear pass/fail)
2. Optimizer model costs (separate API calls for reflection)
3. Designed for task-specific skills, not general conversation
4. Requires multiple epochs for best results (not instant)

## Our Adaptation for OpenClaw

### What We Keep
- ✅ Treat SKILL.md as trainable state
- ✅ Bounded edits (add/delete/replace, not full rewrite)
- ✅ Validation gate (only accept improvements)
- ✅ Learning rate (max edits per pass)
- ✅ Rejected-edit buffer
- ✅ Meta skill extraction (cross-skill patterns)

### What We Adapt
- 🔄 No benchmarks → use quality rubric (10 dimensions) instead of scored rollouts
- 🔄 No separate optimizer model → use the agent itself as optimizer
- 🔄 No execution harness → analyze skill structure + execution logs
- 🔄 No epochs → iterative optimization passes with AAR feedback
- 🔄 Focus on structural quality, not task accuracy

### What We Add
- ➕ Integration with OpenClaw skill system (SKILL.md format)
- ➕ Integration with AAR (continuous improvement loop)
- ➕ Integration with Skill Workshop (publishing optimized skills)
- ➕ Batch optimization across workspace
- ➕ Human-readable reports and diffs
