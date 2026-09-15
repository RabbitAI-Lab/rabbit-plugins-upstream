## Description:

Stack Internal lets an agent search and read Stack Overflow for Teams content through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to retrieve the current Stack Internal user, read questions and answers, list tags, and search team knowledge from a connected Stack Overflow for Teams workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can tell an agent to execute an unverified remote installer if the OOMOL CLI is missing.

Mitigation: Review installation steps before deployment; install the oo CLI only from a trusted source, preferably with version pinning or integrity verification, and confirm any local file or shell configuration changes.

Risk: The skill depends on a connected Stack Internal account and may fail when authentication, connection scopes, credentials, or billing are not ready.

Mitigation: Run setup or connection recovery only after a matching command failure, and have the user resolve sign-in, connection, scope, credential, or billing issues before retrying.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-stack-overflow-for-teams)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Stack Internal Homepage](https://stackoverflow.co/internal/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Stack Internal connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
