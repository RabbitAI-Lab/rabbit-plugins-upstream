## Description:

Collects comments from a Bilibili video URL through Qinghu's paid data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use the skill to collect comments on a Bilibili video and summarize audience feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit can change local Node tooling.

Mitigation: Review installation steps and prefer a preinstalled, pinned qhkit version.

Risk: Persistently configuring a qhkit API token can expose credentials.

Mitigation: Prefer an ephemeral QHKIT_TOKEN rather than storing a token locally.

Risk: Comment collection incurs variable charges through a paid service.

Mitigation: Check the current estimate and obtain user approval before paid calls, especially for large collections.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-bilibili-comments)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise summary with a short comment preview; table file for 10 or more records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the credits charged for paid calls; large results require reading the complete local data file.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
