## Description:

Fairing (fairing.co). Use this skill for Fairing search and read requests through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live Fairing connector schemas and list paginated Fairing survey responses with optional filters. It supports account setup recovery for authentication, connection, and billing failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes direct execution of remote installer scripts in a shell.

Mitigation: Use an official package when available, or download and inspect the installer first and verify checksum or signature information before execution.

Risk: Fairing response data is accessed through OOMOL as the connector service.

Mitigation: Install and use the skill only when sharing Fairing response data through OOMOL is acceptable for the intended account and data.

## Reference(s):

- [Fairing homepage](https://fairing.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Fairing skill page](https://clawhub.ai/oomol/skills/oo-fairing)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Fairing connector response data returned as JSON through the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
