## Description:

Provides agent access to 1Password Events API audit events, item usage events, and sign-in attempts through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security operators, and agents use this skill to read 1Password Events API telemetry for audit review, item usage analysis, and sign-in investigation without handling raw 1Password credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skill asks users or agents to run unverified remote installer scripts.

Mitigation: Review installation steps before use and prefer safer verified oo CLI installation instructions instead of piping remote scripts into a shell.

Risk: The security review reports that sensitive security telemetry is routed through a third-party connector.

Mitigation: Connect 1Password Events API data to OOMOL only after confirming the organization is comfortable with OOMOL processing audit and sign-in telemetry under its documented controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-one-password-events)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [1Password Events API homepage](https://1password.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides read-only OOMOL connector calls for audit events, item usage events, and sign-in attempts.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
