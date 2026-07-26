---
name: synomega
description: >-
  Retrosynthesis with the synomega Python package (pip install synomega) —
  single-step reactant prediction, multi-step route planning, and a continuous
  synthesizability score (bb-coverage) for a target molecule given as SMILES. Use
  this for legitimate retrosynthesis and cheminformatics tasks — when the user
  gives a specific molecule (as SMILES or a resolvable name) and asks for
  candidate disconnections/reactants, a full synthesis route down to purchasable
  building blocks, or a makeability score to rank molecules. Safety judgments for
  hazardous, controlled, or otherwise dual-use compounds are deferred to the
  host's safety policy (see "Safety boundary / dual-use" below).
---

# SynOmega

SynOmega is a **Python package** ([PyPI](https://pypi.org/project/synomega/))
that turns a target molecule (SMILES) into synthesis routes and a **continuous
synthesizability score**. Three layers behind one interface: single-step
prediction → AND-OR graph search → synthesizability scoring.

It runs entirely locally. **It works out of the box** — the default pretrained
model and building-block stock are downloaded automatically on first use, so
there is nothing to train or configure.

> ⚠️ **Network + disk notice (first use downloads a few hundred MB).** The first
> prediction (or `synomega.load_default_planner()`) automatically reaches out to
> a **remote mirror** (USTC GitLab and/or GitHub) and downloads the default model
> and stock — **a few hundred MB** — into `~/.cache/synomega`. Nothing else phones
> home, but this first fetch does. Controls: pre-fetch with `synomega download`;
> change the cache dir with `SYNOMEGA_CACHE`; pick a mirror with `SYNOMEGA_MIRROR`
> (`ustc` or `github`). In **air-gapped, bandwidth-limited, privacy-sensitive, or
> reproducibility-critical** environments, pre-fetch (or point at a local
> model/stock) and treat the download as an explicit opt-in rather than a surprise.

## Install

```bash
pip install "synomega[gnn]"    # neural D-MPNN backend (torch) — recommended
```

Requires Python ≥ 3.10.

## First run downloads the model + stock (automatic)

The wheel ships only code. The first prediction downloads the default model and
stock (a few hundred MB) into `~/.cache/synomega`. You can pre-fetch them:

```bash
synomega download
```

Downloads come from the nearest mirror, auto-selected by latency (a USTC GitLab
registry, fast in China; and GitHub). Force one with `SYNOMEGA_MIRROR=ustc` or
`SYNOMEGA_MIRROR=github`; change the cache dir with `SYNOMEGA_CACHE`.

## Fastest path: the bundled helper

`scripts/synomega_run.py` prints JSON for any of the three operations. No
configuration — it downloads the default model/stock on first call:

```bash
python scripts/synomega_run.py score        "CC(=O)Nc1ccccc1O" --max-steps 5
python scripts/synomega_run.py score        "CC(=O)Nc1ccccc1O" --exclude-target
python scripts/synomega_run.py plan         "CC(=O)Nc1ccccc1O" --max-depth 5
python scripts/synomega_run.py single-step  "CC(=O)Nc1ccccc1O" --top-k 10
```

`plan` and `score` accept `--exclude-target` (Python: `exclude_target=True`),
which treats the target as *not* purchasable even if it is itself in the stock —
so a catalogue molecule is not reported as trivially solved in zero steps. Use it
when the user asks "how would you actually make X" about a possibly-buyable
molecule. Default off.

## Reaction-plausibility screening (off by default)

An optional **mapping-free dual-tower reaction-plausibility model** can screen
every single-step prediction — for `single-step`, `plan`, and `score` alike —
scoring how likely each candidate's reactants actually give the target and
**dropping** implausible disconnections (it only removes wrong reactions, never
re-ranks the rest). It is **off by default**: it does not improve top-k accuracy
and adds latency. Enable it to prune obviously-wrong candidates from the list.

Enable/tune with env vars: `SYNOMEGA_PLAUSIBILITY=1` turns it on;
`SYNOMEGA_PLAUSIBILITY_THRESHOLD=0.4` sets the drop threshold. When on, each
`single-step` prediction gains a `plausibility` field (0–1). In the Python API:
`synomega.load_default_planner(plausibility=True)`.

## Simplification-constrained model (off by default)

An alternative single-step model restricted to **simplifying (fragmentation)
disconnections** — those that split the target into two or more precursors —
reaches purchasable material with fewer search expansions at matched solvability
(faster planning). Enable it in the Python API with
`synomega.load_default_planner(simplify=True)` or load it directly with
`TemplateGNN.simplify()`; it downloads on first use like the default model.
Requires `synomega >= 0.5.0`.

## Python API

```python
import synomega

# one ready-to-use planner backed by the default model + stock (downloads once)
planner = synomega.load_default_planner()          # device="cpu" by default

# 1) Single-step — "what reacts to give X?"
for p in planner.model.predict("CC(=O)Nc1ccccc1O", top_k=10):
    print(p.score, p.reactants)

# 2) Multi-step — "how do I make X?"
result = planner.plan("CC(=O)Nc1ccccc1O", max_depth=5)
print(result.solved)
print(result.best_route.describe())

# 3) Synthesizability score — "can X be made / how hard?"
from synomega import SynthesizabilityScorer
r = SynthesizabilityScorer(planner).score("CC(=O)Nc1ccccc1O", max_steps=5)
print(r.bb_coverage, r.min_steps, r.solved)
```

To use your own checkpoint/stock instead of the defaults, set `SYNOMEGA_MODEL`
and `SYNOMEGA_STOCK` (the helper reads them), or build the objects directly with
`TemplateGNN.from_pretrained(...)` / `InMemoryStock.from_keys_file(...)`.

## How to read the output

- **single-step** → ranked `Prediction`s; each has `.reactants` (a tuple of
  SMILES) and `.score` (higher = more likely). Present the top few disconnections.
- **plan** → a route tree. Read it top-down: the target decomposes into the
  reactants that make it, recursively, until every leaf is a purchasable building
  block. `result.best_route.describe()` prints it as numbered steps.
- **score** → the headline is **`bb_coverage`** (0–1): the fraction of the best
  route's leaves that are purchasable. It is *continuous*, so 0.8 (a near-miss)
  is meaningfully better than 0.0 — use it to rank candidates, not just to split
  solved/unsolved. Also report `solved` (a fully-purchasable route exists) and
  `min_steps` (reactions in the shortest solved route).

## Rules for the agent

- Always pass a valid **SMILES**. If the user gives a name, resolve it first (or ask).
- `algorithm` ∈ {`retrostar` (default), `mcts`, `bfs`}. Larger `max_depth` /
  `max_steps` finds more but is slower; start at 5.
- The first call downloads a few hundred MB — expect a one-time delay. Loading the
  model also takes a few seconds; in Python, build `planner` once and reuse it.

## Safety boundary / dual-use

Retrosynthesis is inherently dual-use: the same route-planning that helps
legitimate chemistry can also apply to hazardous, controlled, or otherwise
regulated compounds. This skill does **not** itself decide what is permissible —
that judgment is **deferred to the host's safety policy**, which takes precedence
over any request handled here.

- **Educational vs. operational.** General, educational, or conceptual discussion
  of chemistry (what a reaction class is, why a molecule is hard to make) is
  different from **actionable procurement/route assistance** (concrete steps,
  quantities, sourcing) for a specific hazardous or controlled target. Treat the
  latter with far more caution.
- **High-risk targets need extra review.** For compounds that are toxic,
  explosive, weaponizable, controlled, or otherwise clearly high-risk, do not
  produce an operational synthesis plan on autopilot — defer to the host safety
  policy and any required additional review before proceeding.
- **When unsure, ask or decline.** If a request looks like it seeks a usable route
  to a dangerous or restricted substance, surface the concern rather than
  silently planning it. Normal, benign retrosynthesis and makeability scoring are
  unaffected.

## Links

- Package: https://pypi.org/project/synomega/
- Source:  https://github.com/zbc0315/synomega
- This skill: https://github.com/zbc0315/synomega-skill
