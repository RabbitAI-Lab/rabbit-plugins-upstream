## Description:

Provides 34 investment research modules for macro, fixed income, industry, company, strategy, and quantitative workflows that generate report outlines and research drafts with source, methodology, and human-review checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Investment research employees and external analysts use this skill to choose an appropriate research module, structure financial research briefs, and draft markdown reports for human review. It supports macro, fixed income, industry, company, strategy, and quantitative analysis using user-authorized data sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to query authorized financial data services or public web sources during research workflows.

Mitigation: Use only approved data services or public sources, minimize sensitive data, cite source and timestamp, and cross-check critical values.

Risk: Some workflows describe recurring or scheduled report generation.

Mitigation: Require explicit user approval before saving, sending, or setting up recurring reports, and preview the full output first.

Risk: Generated research can resemble investment advice or overstate confidence.

Mitigation: Treat outputs as draft research only, preserve non-advice disclaimers, and require review by qualified personnel before real-world use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/investment-researcher-digital-employee)
- [Publisher profile](https://clawhub.ai/user/gechengling)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration]

**Output Format:** [Markdown research reports, report outlines, tables, checklists, and illustrative command or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-supplied target, asset, and time window; outputs require qualified human review and explicit confirmation before saving, sending, or scheduling.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
