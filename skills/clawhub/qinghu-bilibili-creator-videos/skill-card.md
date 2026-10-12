## Description:

Retrieves a Bilibili creator's published videos from their profile URL, including views, likes, coins, favorites, shares, and comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and analysts use this skill to review a Bilibili creator's video catalog and engagement metrics from a profile URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install qhkit and Node tooling or change the local environment.

Mitigation: Review installation steps and preinstall a pinned qhkit version where possible.

Risk: An API token must be stored or supplied to access the Qinghu service.

Mitigation: Use QHKIT_TOKEN for temporary credentials when possible and avoid sharing the token.

Risk: Video lookups can consume paid Qinghu credits, especially for large requests.

Mitigation: Check the current estimate and obtain user approval before paid calls or additional batches.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-bilibili-creator-videos)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary with a local table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports video engagement metrics and source links; larger responses may be supplied as a local JSON file.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
