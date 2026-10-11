## Description:

Looks up the keywords driving traffic to a specified Amazon ASIN, including search volume, organic and ad rankings, traffic share, and PPC bid estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and analysts use this skill to investigate an ASIN's traffic-generating keywords and compare organic visibility, advertising positions, and PPC opportunities across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may install or update Node and the qhkit command-line package and change the user environment.

Mitigation: Review these changes first; preinstall and pin a trusted qhkit version when possible.

Risk: The skill configures and uses a Qinghu API token for an external service.

Mitigation: Provide the token only if you trust the service and keep it out of shared outputs.

Risk: Keyword lookups can consume Qinghu credits, including some failed calls.

Mitigation: Check the current estimate and obtain consent before paid calls; review credit usage afterward.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-traffic-keyword)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [Markdown summary with an optional tabular export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes marketplace and time period; larger result sets may be delivered as files with a short preview.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
