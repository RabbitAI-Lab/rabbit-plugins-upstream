## Description:

Turbot Pipes helps agents query Turbot Pipes through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and operators use this skill to inspect the Turbot Pipes connector schema and run SQL queries against a connected Turbot Pipes account through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands could execute unreviewed code during first-time setup.

Mitigation: Install the oo CLI through a trusted, independently verified method before enabling the skill.

Risk: Free-form SQL queries may be broad, costly, or expose sensitive Turbot Pipes data.

Mitigation: Review SQL queries and their intended scope before execution, especially against connected production accounts.

## Reference(s):

- [Turbot Pipes homepage](https://turbot.com/pipes)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-turbot-pipes)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown instructions with bash command examples and JSON connector responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
