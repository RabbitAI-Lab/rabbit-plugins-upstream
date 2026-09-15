## Description:

Provides agent guidance for using the oo CLI to inspect action schemas and export Microsoft Clarity live insights through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and support agents use this skill to retrieve recent Microsoft Clarity live insights after confirming connector schemas and account connection state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Do not allow an agent to run those installer commands automatically; install the oo CLI through a trusted method with version pinning and signature or checksum verification where available.

Risk: The skill depends on an authenticated OOMOL Microsoft Clarity connection and may fail when credentials, scopes, app readiness, or billing are not in the expected state.

Mitigation: Treat authentication, connection, scope, app readiness, and billing messages as setup issues that require intentional user action before retrying connector commands.

## Reference(s):

- [Microsoft Clarity homepage](https://clarity.microsoft.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-microsoft-clarity)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before running Microsoft Clarity actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
