## Description:

Retrosynthesis, reaction prediction, and synthesizability for organic molecules using the local SynOmega Python package.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zbc0315](https://clawhub.ai/user/zbc0315)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and chemistry-focused agents use this skill to evaluate organic molecules, predict reaction outcomes, plan retrosynthetic routes, score synthesizability, and explore multi-component reaction networks from SMILES inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first use downloads large model and stock assets and stores them in a local cache.

Mitigation: Prefetch assets explicitly, set SYNOMEGA_CACHE to an approved location, or point SYNOMEGA_MODEL and SYNOMEGA_STOCK at approved local assets in private, air-gapped, or reproducibility-sensitive environments.

Risk: Retrosynthesis and reaction prediction can be dual-use for hazardous, controlled, or operational synthesis requests.

Mitigation: Apply the host safety policy before producing route plans, procurement-relevant details, or other operational assistance for high-risk compounds.

## Reference(s):

- [SynOmega package](https://pypi.org/project/synomega/)
- [SynOmega documentation](https://zbc0315.github.io/synomega/)
- [SynOmega toolkit source](https://github.com/zbc0315/synomega)
- [ClawHub skill page](https://clawhub.ai/zbc0315/skills/synomega)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON outputs from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are candidate chemistry predictions and route-planning results; they require host safety-policy review for hazardous, controlled, or operational synthesis requests.]

## Skill Version(s):

1.6.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
