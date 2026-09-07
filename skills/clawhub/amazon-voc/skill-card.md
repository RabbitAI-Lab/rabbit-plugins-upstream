## Description:

Amazon-VOC collects Amazon reviews through ARI and produces VOC insight reports covering negative-review pain points, buying motivations, customer personas, use cases, trends, competitor comparisons, and listing optimization suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to turn collected Amazon review data into concise VOC summaries, full insight reports, trend checks, competitor comparisons, and listing improvement guidance. The skill is intended for agent-assisted product operations workflows where users provide an ASIN, marketplace, and analysis goal in natural language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits automatically when account rules allow paid actions without a prompt.

Mitigation: Set the ARI account to ask before every paid action or use quote-only workflows before running paid analysis.

Risk: The skill can export reports or review data to arbitrary local paths.

Mitigation: Use non-sensitive export directories, review target paths before export, and avoid overwriting existing files.

Risk: The skill sends product and review requests to ARI.

Mitigation: Install only when sharing the relevant product and review data with ARI is acceptable for the intended workflow.

## Reference(s):

- [Amazon-VOC ClawHub Listing](https://clawhub.ai/funewa/skills/amazon-voc)
- [Amazon-VOC README](README.md)
- [Amazon-VOC Usage Instructions](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Web Application](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown summaries and reports, inline shell commands, JSON-backed CLI results, and optional Markdown, HTML, or CSV exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on ARI-collected Amazon review samples and may include report links, sample scope, credit usage, account balance, and export paths when returned by the service.]

## Skill Version(s):

1.4.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
