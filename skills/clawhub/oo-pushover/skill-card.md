## Description:

Pushover (pushover.net). Use this skill for ANY Pushover request: reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to send Pushover notifications and administer Pushover users, groups, teams, licenses, receipts, Open Client sessions, and application metadata from an agent using the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-handling actions can return, validate, or store application and team API tokens or Open Client login material.

Mitigation: Use explicit approval before credential-related actions, avoid exposing tokens in chat or logs, and rotate any token that is disclosed.

Risk: Write and destructive actions can change Pushover delivery groups, team membership, receipts, licenses, devices, messages, or notification delivery state.

Mitigation: Inspect the live action schema, confirm the exact target and payload with the user, and require explicit approval before execution.

Risk: The setup section includes one-line remote installer commands that execute downloaded scripts.

Mitigation: Prefer a verified installation path or independently inspect and verify the installer source before running remote install commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pushover)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Pushover Homepage](https://pushover.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses, execution identifiers, base64 image content, Pushover metadata, and credential-derived values depending on the selected action.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
