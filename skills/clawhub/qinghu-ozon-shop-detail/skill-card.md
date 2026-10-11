## Description:

Looks up details for up to 10 Ozon shops by shop ID using the Qinghu data tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and analysts use this skill to compare Ozon shop details and review competitor shops by ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install or upgrade Node/npm tooling, including unpinned latest versions, on the host.

Mitigation: Review before installation and prefer preinstalled, pinned tooling.

Risk: Setting up qhkit can store an API credential on the machine.

Mitigation: Manage credentials outside the skill and avoid exposing tokens in agent output.

Risk: Shop lookups consume credits, and actual charges can vary with result size.

Mitigation: Estimate costs and obtain explicit user consent before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-shop-detail)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown summary; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 10 shop IDs per query; paid calls consume Qinghu credits.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
