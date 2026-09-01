## Description:

Synomega Skill helps agents run local organic chemistry workflows for retrosynthesis, forward reaction prediction, route planning, synthesizability scoring, reaction-plausibility screening, and multi-component reaction-network exploration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zbc0315](https://clawhub.ai/user/zbc0315)

### License/Terms of Use:

MIT

## Use Case:

Developers, chemists, and agent users use this skill to evaluate organic molecule makeability, propose candidate synthesis routes, predict reaction outcomes, and explore reaction networks from SMILES inputs. It is intended for benign chemistry workflows subject to the host system's safety policy for hazardous, controlled, or otherwise high-risk compounds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first use may download several hundred MB of models and stock data from remote mirrors.

Mitigation: Pre-fetch assets in controlled environments or configure local, vetted model and stock files before use.

Risk: Retrosynthesis and route-planning outputs can become actionable for hazardous, controlled, explosive, toxic, or otherwise high-risk compounds.

Mitigation: Apply the host safety policy and require additional review before providing operational synthesis assistance for high-risk targets.

Risk: Predicted reactions, route plans, and synthesizability scores are candidates rather than guarantees.

Mitigation: Treat outputs as decision support that requires expert chemistry review before laboratory use or procurement decisions.

## Reference(s):

- [SynOmega documentation](https://zbc0315.github.io/synomega/)
- [SynOmega PyPI package](https://pypi.org/project/synomega/)
- [SynOmega source repository](https://github.com/zbc0315/synomega)
- [SynOmega skill source](https://github.com/zbc0315/synomega-skill)
- [ClawHub skill page](https://clawhub.ai/zbc0315/skills/synomega)
- [ClawHub publisher profile](https://clawhub.ai/user/zbc0315)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-producing helper invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Helper commands print JSON for retrosynthesis predictions, forward predictions, route plans, synthesizability reports, and reaction-network outputs.]

## Skill Version(s):

1.8.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
