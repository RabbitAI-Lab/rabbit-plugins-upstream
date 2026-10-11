## Description:

Retrieves a Douyin account's fan demographics, interests, devices, and geographic distribution from a profile or video link using Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and analysts use this skill to understand the age, gender, interests, device usage, and location of a Douyin account's audience before making outreach or content decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation may add unpinned npm tooling or install Node in the user's directory.

Mitigation: Review the installation steps and prefer a preinstalled, pinned qhkit version.

Risk: Persistent configuration may store a Qinghu API token.

Mitigation: Use an ephemeral QHKIT_TOKEN secret rather than storing the token in persistent configuration.

Risk: Fan-profile lookups consume Qinghu credits, and actual charges can exceed the base estimate.

Mitigation: Check the current estimate and obtain user approval before paid calls or large batches.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-douyin-fans-portrait)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise audience analysis with supporting figures; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the Qinghu credits consumed for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
