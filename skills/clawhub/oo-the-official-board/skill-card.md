## Description:

The Official Board connector helps agents search and retrieve company organizational charts, executive biographies, colleagues, recent org chart news, and watchlist changes through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent look up The Official Board company and executive information through an already configured OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes unverified remote installer commands executed directly in a shell.

Mitigation: Do not let an agent run the installer automatically; use a verified, pinned installer or official package-manager flow and approve setup manually.

Risk: The skill depends on an authenticated OOMOL account and a connected The Official Board credential.

Mitigation: Run login and connection setup only after an auth or connection failure, and have the user approve any account or credential setup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-the-official-board)
- [The Official Board homepage](https://www.theofficialboard.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON action responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, a signed-in OOMOL account, and a connected The Official Board credential.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
