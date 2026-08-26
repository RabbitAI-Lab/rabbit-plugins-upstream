## Description:

Ozon helps an agent search and read data from an Ozon seller account through the OOMOL-connected Ozon connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Ozon seller account information, products, prices, stock quantities, and FBS or rFBS postings without handling raw Ozon credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query data from a connected Ozon seller account through OOMOL.

Mitigation: Install and use it only when account data access is expected, and review connector schemas before running actions.

Risk: Future connector actions could add write-capable behavior even though the current security evidence describes this release as read-only.

Mitigation: Require explicit user confirmation and schema review before running any action tagged write or destructive.

## Reference(s):

- [ClawHub Ozon Skill](https://clawhub.ai/oomol/skills/oo-ozon)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Ozon](https://www.ozon.ru)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
