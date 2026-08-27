## Description:

Synomega Skill helps agents use the local synomega Python package for retrosynthesis, forward reaction prediction, route planning, synthesizability scoring, reaction-plausibility screening, and multi-component reaction-network exploration for organic molecules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zbc0315](https://clawhub.ai/user/zbc0315)

### License/Terms of Use:

MIT

## Use Case:

Developers, chemists, and agent users use this skill to ask synthesis-planning and reaction-prediction questions from valid SMILES inputs, including how to make a target molecule, whether it is likely synthesizable, what reactants could produce it, or how a reactant mixture may evolve. The skill delegates safety decisions for hazardous, controlled, or dual-use chemistry to the host policy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs a local Python chemistry package and may download pretrained model and stock data on first use.

Mitigation: In bandwidth-limited, air-gapped, privacy-sensitive, or reproducibility-critical environments, prefetch assets, pin a trusted mirror, or configure local SYNOMEGA_MODEL and SYNOMEGA_STOCK paths before use.

Risk: Retrosynthesis and route-planning capabilities can be dual-use for hazardous, controlled, or otherwise restricted compounds.

Mitigation: Apply the host safety policy before providing operational synthesis assistance, and avoid automatically producing actionable routes for high-risk targets.

Risk: Reaction predictions and synthesis routes are model-generated candidates rather than guaranteed laboratory outcomes.

Mitigation: Treat predicted products, scores, and routes as decision-support outputs that require expert review and validation.

## Reference(s):

- [SynOmega documentation](https://zbc0315.github.io/synomega/)
- [SynOmega package on PyPI](https://pypi.org/project/synomega/)
- [SynOmega toolkit source](https://github.com/zbc0315/synomega)
- [SynOmega skill source](https://github.com/zbc0315/synomega-skill)
- [ClawHub skill page](https://clawhub.ai/zbc0315/skills/synomega)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-producing helper outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are candidate chemistry predictions and route-planning guidance; generated plans should be reviewed before operational use.]

## Skill Version(s):

1.8.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
