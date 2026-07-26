# synomega-skill

An agent **Skill** for [synomega](https://github.com/zbc0315/synomega) — the
retrosynthesis toolkit on PyPI. It teaches Claude Code, OpenClaw and other coding
agents to use the `synomega` Python package: predict single-step disconnections,
plan multi-step routes, and compute a continuous **synthesizability score** for a
molecule given as SMILES.

The skill runs synomega **locally** — `pip install synomega` plus a trained model
and a building-block file. It does not depend on any hosted service.

## Install

**OpenClaw / ClawHub**

```bash
clawhub install synomega
```

**Claude Code (manual)**

```bash
mkdir -p ~/.claude/skills/synomega
curl -fsSL https://raw.githubusercontent.com/zbc0315/synomega-skill/main/SKILL.md \
  -o ~/.claude/skills/synomega/SKILL.md
curl -fsSL https://raw.githubusercontent.com/zbc0315/synomega-skill/main/scripts/synomega_run.py \
  -o ~/.claude/skills/synomega/synomega_run.py
```

## Prerequisites

```bash
pip install "synomega[gnn]"        # the package (neural backend)
```

That's it — **it works out of the box**. The default pretrained model and
building-block stock download automatically on first use (into
`~/.cache/synomega`); run `synomega download` to pre-fetch them. Downloads come
from the nearest mirror (USTC GitLab in China, or GitHub), auto-selected by
latency. To use your own checkpoint/stock instead, set `SYNOMEGA_MODEL` /
`SYNOMEGA_STOCK`.

## Use

Ask your agent things like:

- "Can *paracetamol* be synthesized? How hard?"
- "Propose a synthesis route for `CC(=O)Nc1ccccc1O`."
- "What reactants could give this molecule in one step?"

Or call the bundled helper directly:

```bash
python scripts/synomega_run.py score        "CC(=O)Nc1ccccc1O" --max-steps 5
python scripts/synomega_run.py score        "CC(=O)Nc1ccccc1O" --exclude-target
python scripts/synomega_run.py plan         "CC(=O)Nc1ccccc1O" --max-depth 5
python scripts/synomega_run.py single-step  "CC(=O)Nc1ccccc1O" --top-k 10
```

`plan` and `score` take `--exclude-target` to treat the target as not
purchasable even if it is itself a catalogue molecule (so it is not trivially
"solved" in zero steps). Default off.

## Contents

| File | Purpose |
|---|---|
| `SKILL.md` | the skill definition (frontmatter + instructions) |
| `scripts/synomega_run.py` | loads model + stock from env vars, runs any of the three operations, prints JSON |

## Related

- Toolkit: https://github.com/zbc0315/synomega · https://pypi.org/project/synomega/
- Online demo (browser instance): synomega-web

## License

MIT — see [LICENSE](LICENSE).
