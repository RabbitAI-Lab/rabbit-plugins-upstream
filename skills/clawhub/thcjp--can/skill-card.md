## Description:

CAN（Clock Address Naming）协议 helps agents create a verifiable content-addressing index for data flows by recording timestamps, content hashes, and human-readable labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation teams, and agent users use this skill to label, verify, find, and audit agent data outputs with a three-field WHEN/WHERE/WHAT content-addressing pattern.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill mixes local-only content-addressing claims with optional use of third-party xc.cx endpoints.

Mitigation: Use local hashing and logs when possible, and send labels or workflow metadata to xc.cx only when that service is trusted for the task.

Risk: The skill declares broad read, write, and exec authority.

Mitigation: Review generated commands before execution and run the skill only for explicit CAN/content-addressing tasks.

Risk: Sensitive labels, hashes, workflow metadata, or API keys could be exposed if provided unnecessarily.

Mitigation: Avoid sensitive labels, redact workflow metadata, and do not provide API keys unless a specific trusted integration requires them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/can)
- [CAN evaluate endpoint](https://xc.cx/can/evaluate)
- [CAN log endpoint](https://xc.cx/can/log)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns task status, parsed summaries, concrete output data, and error details when a task fails.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
