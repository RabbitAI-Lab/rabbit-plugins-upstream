## Description:

Pendo connector skill for searching and reading Pendo feature and page data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to inspect Pendo features and pages, verify integration status, and run scoped read operations through an OOMOL-managed Pendo connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that execute shell or PowerShell scripts directly.

Mitigation: Install the oo CLI only through a verified package or a downloaded installer with checksum or signature verification, and do not allow an agent to run installer commands automatically.

Risk: The skill depends on an OOMOL-managed Pendo connection and can fail when authentication, connection scope, credentials, app readiness, or billing are not current.

Mitigation: Run setup and reconnection steps only after a matching command failure, and confirm account connection or billing actions deliberately before retrying.

## Reference(s):

- [Pendo homepage](https://www.pendo.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pendo)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata when run through the oo CLI.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
