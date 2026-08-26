## Description:

Guides agents through Amazon product opportunity research, from demand and niche filtering to benchmark products, review pain mining, IP checks, and a final go/no-go report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pangolinfo](https://clawhub.ai/user/pangolinfo)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, product managers, and e-commerce researchers use this skill to evaluate whether an Amazon category or product idea is worth entering. It helps them move from a seed idea to a concise market profile, benchmark comparison, risk check, and go/no-go recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Pangolinfo API key and sends product-research queries through Pangolinfo tools.

Mitigation: Install only if you trust Pangolinfo with the API key and research queries, keep the key scoped to this service where possible, and avoid sending sensitive product plans unless permitted.

Risk: Full-mode review and search steps can consume external lookup credits.

Mitigation: Review the skill's budget prompts before approving higher-cost steps and stop when Fast-mode evidence is sufficient.

Risk: IP clearance output is a preliminary risk radar rather than formal legal advice.

Mitigation: Use the IP section to identify areas for review and consult a qualified IP professional before opening molds or committing to large inventory.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pangolinfo/skills/pangolinfo-amazon-product-explorer)
- [Pangolinfo website](https://www.pangolinfo.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown reports with tables, sourced metrics, and concise recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fast and Full modes; higher-cost review collection requires a budget prompt before proceeding.]

## Skill Version(s):

4.0.0 (source: server release evidence; artifact frontmatter says 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
