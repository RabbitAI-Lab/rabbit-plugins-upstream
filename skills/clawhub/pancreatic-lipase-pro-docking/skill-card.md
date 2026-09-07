## Description:

Docks small molecules against human pancreatic lipase (PDB 1LPB, lipase+colipase+Ca2+) across five validated sites with AutoDock Vina, pH 7.4 ligand preparation, multi-seed consensus, native re-dock validation, and calibration drift detection.

This skill is for research and development only.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to dock, screen, validate, and rank candidate compounds against human pancreatic lipase for authorized anti-obesity or lipase-inhibitor virtual screening workflows. It supports local execution and an optional Kaggle CPU route when the local docking toolchain is unavailable or large batches need cloud execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional setup and cloud paths can run unpinned downloaded tooling.

Mitigation: Use a fresh project-local environment or container, prefer the documented micromamba environment, avoid optional user-level bootstrap paths, and review setup scripts before execution.

Risk: Kaggle and PubChem paths can expose ligand names, SMILES, or screening libraries outside the local environment.

Mitigation: Keep confidential structures offline, supply SMILES directly instead of resolving names through PubChem, and avoid Kaggle for proprietary ligand sets.

Risk: Docking scores can be misleading if validation or calibration gates fail.

Mitigation: Run the preflight, native re-dock, drift check, and result validator before relying on or publishing any scores.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/pancreatic-lipase-pro-docking)
- [README](artifact/README.md)
- [CLI and data reference](artifact/references/reference.md)
- [Kaggle execution guide](artifact/references/kaggle.md)
- [Workflow recipes](artifact/references/workflows.md)
- [Debugging guide](artifact/references/debugging.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration instructions, and references to generated CSV and JSON docking outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Docking scores must come from generated CSV outputs and pass validation gates before reporting; the skill also produces reports and version metadata when its tools are run.]

## Skill Version(s):

101.0.7 (source: server release evidence; artifact frontmatter reports 101.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
