## Description:

Retrieves a WeChat Channels account's published videos with cursor-based pagination using Qinghu's data tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Content analysts and social media teams use this skill to review a WeChat Channels account's recent videos and compare publishing activity across accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit and Node.js may change the host environment, including PATH settings.

Mitigation: Review host changes before installation; prefer a preinstalled, pinned qhkit version in a controlled environment.

Risk: Configuring a Qinghu API token may expose a credential if handled carelessly.

Mitigation: Provide the token through a controlled secret mechanism and avoid including it in shared commands or logs.

Risk: Paginated queries consume paid Qinghu credits.

Mitigation: Check estimated credits, obtain user consent before paid calls, and report actual credits consumed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-videos)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written findings and, for larger results, a tabular file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports cursor pagination; reports credits spent on paid queries.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
