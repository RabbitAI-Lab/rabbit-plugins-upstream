## Description:

Use this skill for Baremetrics requests involving reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Baremetrics through the oo CLI after connecting a Baremetrics account in OOMOL. It supports reading sources, customers, plans, subscriptions, and charges, plus confirmed write actions for customers, plans, subscriptions, and cancellations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask the agent to run remote installer scripts directly in a shell.

Mitigation: Prefer the official install guide or inspect and verify installer scripts before execution.

Risk: The skill can create, update, or cancel Baremetrics records through an OOMOL-connected account.

Mitigation: Review every write or cancellation payload and require explicit approval before running state-changing actions.

Risk: Baremetrics operations depend on OOMOL as an intermediary for account connection and credential handling.

Mitigation: Install only when the user accepts OOMOL-mediated Baremetrics access and server-side credential injection.

## Reference(s):

- [ClawHub Baremetrics skill page](https://clawhub.ai/oomol/skills/oo-baremetrics)
- [Baremetrics homepage](https://baremetrics.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
