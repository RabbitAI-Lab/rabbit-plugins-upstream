## Description:

Retrieves historical Ozon keyword-trend snapshots by keyword ID for weekly, monthly, quarterly, or yearly periods.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and analysts use this skill to review historical keyword demand and seasonality before making merchandising decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrades of Node.js and qhkit change the host environment.

Mitigation: Preinstall a pinned, reviewed qhkit version and review any runtime changes before execution.

Risk: API tokens can be exposed when pasted into shell commands.

Mitigation: Provide credentials through a managed secret mechanism rather than including tokens in shell commands.

Risk: Trend queries are paid and charges can rise with result volume.

Mitigation: Check current pricing, obtain user consent before paid calls, and report actual credits charged.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-keyword-trend)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise trend summary with supporting data and optional table file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report period, sample size, and actual Qinghu credit consumption when paid calls are made.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
