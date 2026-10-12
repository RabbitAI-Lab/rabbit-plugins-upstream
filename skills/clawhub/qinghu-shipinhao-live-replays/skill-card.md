## Description:

Retrieves a WeChat Channels account's livestream replay list for broadcast-frequency and replay-content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and analysts use the skill to retrieve a WeChat Channels account's livestream replay history, review replay material, and assess livestream frequency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance may install or upgrade Node and qhkit, including globally, or alter shell startup files.

Mitigation: Prefer an existing version-pinned qhkit installation and review host changes before permitting installation, upgrades, or shell configuration.

Risk: The skill uses a Qinghu token and paid service calls that consume credits; failed calls may also incur charges.

Mitigation: Review token configuration, obtain consent after checking the current estimate, and monitor actual credit usage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-live-replays)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise analysis with replay details; larger results may be delivered as a table file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credits consumed for paid calls.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
