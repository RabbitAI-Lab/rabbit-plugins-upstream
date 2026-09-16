## Description:

Operate TheHive through an OOMOL-connected account to read, create, and update alerts and cases using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and security operations teams use this skill to inspect live TheHive connector schemas and run read or write actions for alerts and cases through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include unverified internet installer scripts executed directly in a shell.

Mitigation: Prefer installing the oo CLI from a versioned, verifiable source, or inspect and verify downloaded installers before execution.

Risk: The skill routes TheHive operations through an OOMOL-connected account.

Mitigation: Confirm that routing TheHive operations through OOMOL is acceptable before use; credentials should remain server-side rather than being handled directly by the agent.

Risk: The create_case and create_alert actions change TheHive state.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub TheHive Skill](https://clawhub.ai/oomol/skills/oo-thehive)
- [TheHive Homepage](https://thehive-project.org)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Installation Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can run directly; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
