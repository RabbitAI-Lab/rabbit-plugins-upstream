## Description:

ServerAvatar helps agents search and read ServerAvatar organization, server, application, and database data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external agents use this skill to inspect ServerAvatar organizations and list managed servers, applications, and databases from an OOMOL-connected account. It is suited to read-oriented infrastructure discovery and account support workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct internet installer commands for the oo CLI.

Mitigation: Review the installer and install the oo CLI from a verified source before allowing setup commands to run.

Risk: The skill can query data from the connected ServerAvatar account, including organizations, servers, applications, and databases.

Mitigation: Confirm the intended ServerAvatar account connection and scopes before use, and limit queries to the relevant organization.

## Reference(s):

- [ServerAvatar ClawHub skill page](https://clawhub.ai/oomol/skills/oo-serveravatar)
- [OOMOL ClawHub publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ServerAvatar homepage](https://serveravatar.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and JSON connector results when actions are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live oo connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.3 (source: evidence.json release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
