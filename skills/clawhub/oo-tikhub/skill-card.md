## Description:

TikHub enables an agent to discover and invoke TikHub connector actions through an OOMOL-connected account using schema-first CLI commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, read, price, and invoke TikHub API endpoints through the OOMOL TikHub connector. It is suited for TikHub data access workflows where the agent should fetch the live connector schema before sending a JSON action payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands that should be treated as privileged software installation.

Mitigation: Prefer a verified manual install path, review the installer source, and avoid piping remote scripts directly into a shell.

Risk: The get_user_info action may expose TikHub account or API-key-related information in logs or agent context.

Mitigation: Run get_user_info only when account details are specifically needed, and connect credentials with the minimum scopes and credits required.

Risk: Connector calls depend on TikHub account scope, credential freshness, and available OOMOL billing credit.

Mitigation: Use the documented auth, connection, scope, and billing recovery steps only after a command fails for the matching reason.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-tikhub)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [TikHub Homepage](https://tikhub.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are requested as JSON and may include data plus execution metadata.]

## Skill Version(s):

1.0.6 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
