## Description:

TOTP Authenticator lets an agent generate the current six-digit TOTP code for a configured website account through the OOMOL TOTP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent request a current TOTP code for a configured account while relying on OOMOL server-side credential injection. It is suited for workflows where the user has already installed the oo CLI, signed in, and connected the TOTP provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Do not let an agent run installer commands automatically; install the OOMOL CLI only from a trusted source and version, preferably with independent verification.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-totp)
- [RFC 6238: TOTP](https://www.rfc-editor.org/rfc/rfc6238)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The connector response includes data and meta.executionId when an action is run.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
