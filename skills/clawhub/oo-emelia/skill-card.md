## Description:

Provides read-only access to Emelia campaign, contact, email provider, and webhook data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to search and read Emelia account data from an agent session, including campaign details, campaign activity, campaign contacts, email providers, and webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Install the oo CLI only from trusted OOMOL sources, prefer signed or package-manager installation paths where available, and avoid running installer commands from an elevated shell.

Risk: The skill can read Emelia campaign, contact, provider, and webhook data through the connected account.

Mitigation: Use an account with appropriate access, confirm the Emelia connection scope, and review returned data before sharing it outside the agent session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-emelia)
- [Emelia homepage](https://emelia.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connector actions return JSON data with execution metadata when run through the oo CLI.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
