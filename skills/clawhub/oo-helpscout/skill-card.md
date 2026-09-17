## Description:

Operate Help Scout through the OOMOL oo CLI to read, create, and update conversations, customers, inbox metadata, replies, notes, tags, fields, workflow state, and related account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support operators use this skill to operate Help Scout accounts through OOMOL-connected credentials, including reading support data and creating or updating conversations, customers, replies, notes, tags, custom fields, snoozes, and workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute unverified code.

Mitigation: Before installing, verify that the OOMOL installer is trusted; prefer pinned or signed installers with checksum verification.

Risk: Help Scout write actions can change customer conversations, assignments, replies, notes, tags, fields, snoozes, or workflow state.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub Help Scout Skill](https://clawhub.ai/oomol/skills/oo-helpscout)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Help Scout](https://www.helpscout.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
