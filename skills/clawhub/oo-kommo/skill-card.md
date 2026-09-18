## Description:

Kommo (kommo.com). Use this skill for ANY Kommo request - searching and reading data. Whenever a task involves Kommo, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent search and read Kommo CRM account, company, contact, lead, pipeline, task, and user records through the OOMOL oo CLI. The skill directs the agent to inspect the live connector schema before building each action payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path asks users to execute remote installer scripts directly, which the security evidence flags for review.

Mitigation: Review setup commands before installation and prefer a trusted, versioned, verifiable oo CLI installation source.

Risk: The skill can read Kommo CRM records through OOMOL-mediated access.

Mitigation: Connect Kommo only when the user is comfortable granting the connected OOMOL account access to the CRM records the skill can read.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kommo)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Kommo homepage](https://www.kommo.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
