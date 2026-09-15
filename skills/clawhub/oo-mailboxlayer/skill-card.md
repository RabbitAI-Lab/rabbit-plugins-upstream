## Description:

Mailboxlayer validates individual email addresses and returns Mailboxlayer quality signals through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to validate email addresses through Mailboxlayer from an agent workflow without handling raw API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running an unverified remote installer directly in a shell.

Mitigation: Review setup commands before installing, prefer a verified or package-manager installation path for the oo CLI, and avoid running installer commands as administrator or root unless clearly required.

Risk: Email addresses checked by the skill are sent through the OOMOL Mailboxlayer connector.

Mitigation: Treat submitted email addresses as data shared with the connector path and only validate addresses that are appropriate for that service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailboxlayer)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return Mailboxlayer validation data and execution metadata as JSON through the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
