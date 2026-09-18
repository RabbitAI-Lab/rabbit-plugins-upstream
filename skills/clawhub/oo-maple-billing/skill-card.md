## Description:

Use Measure (getmeasure.com) for reading, creating, and updating data through the OOMOL-connected maple_billing connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Measure billing schemas and retrieve, search, create, or update customers, products, pricing, subscriptions, and checkout sessions through OOMOL's Measure connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that may execute unreviewed code.

Mitigation: Review installer sources or use a verified package source before running installation commands.

Risk: Write actions can create or update Measure billing objects.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before any create or update action.

Risk: The connector can read billing objects after account authorization.

Mitigation: Install only for trusted OOMOL and Measure accounts and verify that requested reads match the user's intent.

## Reference(s):

- [Measure homepage](https://getmeasure.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-maple-billing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing requests; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
