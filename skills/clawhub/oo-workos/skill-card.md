## Description:

Helps agents operate WorkOS through the OOMOL-connected oo CLI for reading, creating, updating, and deleting WorkOS users, organizations, and memberships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent manage WorkOS AuthKit users, organizations, and organization memberships through an OOMOL-connected account. It supports read actions directly and requires confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes a remote installer that runs directly in a shell.

Mitigation: Do not let an agent run the installer automatically; manually review, pin, and verify the oo CLI installation before use.

Risk: Write and destructive WorkOS actions can change users, organizations, or memberships.

Mitigation: Inspect the live action schema and review the exact payload and expected effect before approving any write or destructive command.

Risk: The skill depends on OOMOL's connector and server-side credential handling.

Mitigation: Install only when the publisher and connector are trusted, and review WorkOS connection scopes or credential status before running sensitive actions.

## Reference(s):

- [ClawHub WorkOS Skill Page](https://clawhub.ai/oomol/skills/oo-workos)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [WorkOS Homepage](https://workos.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands and JSON payloads; state-changing WorkOS actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
