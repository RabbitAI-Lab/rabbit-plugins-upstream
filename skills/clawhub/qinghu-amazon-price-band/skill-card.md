## Description:

Analyzes Amazon category price bands, sales share, sales efficiency, and ratings to help identify viable entry prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and market analysts use the skill to compare category price ranges and choose a potential entry price using Qinghu data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid Qinghu queries can consume credits, especially for larger results or upstream category lookups.

Mitigation: Estimate cost, disclose the expected credits, and obtain user consent before paid calls.

Risk: Setup instructions can install or upgrade Node and qhkit and change the local shell environment.

Mitigation: Prefer a pre-provisioned qhkit installation; review and approve environment changes before running setup commands.

Risk: Configuring qhkit requires an API token that could be exposed if pasted into chat or shell configuration.

Mitigation: Supply credentials through the platform's secret handling and avoid placing tokens in chat or shell startup files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-price-band)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Markdown summary with optional tabular export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies marketplace, period, and sample size when available; reports credits spent on paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
