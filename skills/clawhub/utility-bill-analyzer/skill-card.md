## Description:

Analyze electricity, water, and gas bills to detect anomalies, compare usage, forecast costs, and suggest savings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to track monthly electricity, water, and gas bills, detect unusual usage or cost changes, forecast future bills, and generate savings guidance from local bill history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Utility usage and cost history may contain household or business expense patterns stored in a local JSON database.

Mitigation: Use the default database path or a dedicated --db file, and avoid pointing --db at files that should not be overwritten.

## Reference(s):

- [Utility Savings Checklist](references/utility-savings-checklist.md)
- [Rate Analysis Guide](references/rate-analysis-guide.md)
- [Server-resolved GitHub repository](https://github.com/voronindenis5/utility-bill-analyzer)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/utility-bill-analyzer)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and terminal text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The included script stores user-entered bill records in a local JSON file.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
