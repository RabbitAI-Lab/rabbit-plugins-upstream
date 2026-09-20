## Description:

Courier (courier.com). Use this skill for Courier requests that read, create, update, and delete data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Courier messages, subscription lists, and user profiles from an agent using the oo CLI. It supports read actions as well as write and destructive actions that require confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can lead an agent toward remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, verified process outside autonomous agent execution before using the skill.

Risk: Write and destructive Courier actions can send messages, overwrite lists, unsubscribe users, or delete profiles and lists.

Mitigation: Inspect the live action schema, confirm the exact payload and expected effect with the user, and require explicit approval before any write or destructive action.

Risk: Courier actions depend on OOMOL as the intermediary for account connection and credential handling.

Mitigation: Use the skill only when the user is comfortable authorizing Courier through OOMOL and has reviewed the connected account and scopes.

## Reference(s):

- [ClawHub Courier skill page](https://clawhub.ai/oomol/skills/oo-courier)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Courier homepage](https://www.courier.com/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Courier connector schemas before running actions; commands execute through the oo CLI against a connected Courier account.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
