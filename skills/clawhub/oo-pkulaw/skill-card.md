## Description:

PKULaw (mcp.pkulaw.com) supports searching and reading laws, regulations, provisions, and judicial case data through the OOMOL pkulaw connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search PKULaw laws, regulations, provisions, and judicial cases through an OOMOL-connected PKULaw account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include mutable remote installer scripts executed directly in a shell.

Mitigation: Install the oo CLI through a verified method such as a pinned release or package with checksum or signature validation before using the skill.

Risk: The skill depends on an OOMOL-connected PKULaw account and may fail when authentication, connection scopes, credentials, app readiness, or billing are not valid.

Mitigation: Run setup or reconnection steps only after a matching command failure, and confirm account readiness before relying on results.

## Reference(s):

- [PKULaw homepage](https://mcp.pkulaw.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pkulaw)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live PKULaw connector schemas before running actions; connector responses are JSON.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
