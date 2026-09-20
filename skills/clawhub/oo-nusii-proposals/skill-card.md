## Description:

Nusii Proposals (nusii.com). Use this skill for ANY Nusii Proposals request — reading, creating, updating, and deleting data. Whenever a task involves Nusii Proposals, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with a connected Nusii Proposals account through the OOMOL oo CLI. It supports reading account, client, proposal, template, theme, and user data, and can create, update, send, or archive proposals after user confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path runs a remote installer script for the oo CLI.

Mitigation: Review the installer and install the oo CLI through a trusted, verifiable method before using the skill.

Risk: Write and destructive actions can create, send, update, or archive Nusii proposal records.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running write or destructive actions.

Risk: Actions operate against the connected Nusii account.

Mitigation: Use the skill only with the intended connected account and inspect the live action schema before constructing each payload.

## Reference(s):

- [Nusii Proposals ClawHub listing](https://clawhub.ai/oomol/skills/oo-nusii-proposals)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Nusii Proposals homepage](https://nusii.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
