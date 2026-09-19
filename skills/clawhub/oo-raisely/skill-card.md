## Description:

Provides agent guidance for operating Raisely through the OOMOL oo CLI connector, including campaign and profile reads plus webhook management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with Raisely campaigns, fundraising profiles, and webhook settings through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include unverified internet installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Prefer official, versioned oo CLI installation steps with verification instead of running the pipe-to-shell installer as written.

Risk: Webhook create, update, and delete actions can change or remove Raisely account configuration.

Mitigation: Confirm the exact payload, target webhook, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Raisely skill page](https://clawhub.ai/oomol/skills/oo-raisely)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Raisely homepage](https://raisely.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions may run directly; write and destructive webhook actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
