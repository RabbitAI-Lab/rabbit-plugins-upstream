## Description:

Business Data Analyst helps agents structure business analysis, data-quality checks, market research, reporting, and decision recommendations for growth, funnel, retention, revenue, efficiency, and operating diagnosis questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phoenixlucky](https://clawhub.ai/user/phoenixlucky)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, analysts, and business teams use this skill to turn operating or market questions into analysis plans, metric definitions, evidence checks, root-cause diagnostics, business reports, recommendations, and validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential business details could be exposed if they are sent to external search or public fact-checking tools.

Mitigation: Keep sensitive internal data out of web searches and separate private analysis from external source verification.

Risk: Business recommendations may be misleading if metric definitions, data quality, time windows, or source dates are not checked.

Mitigation: Require metric definitions, source traceability, data-quality checks, and explicit labels for facts, assumptions, inferences, and risks.

Risk: The lightweight router uses keyword matching and its confidence is not a calibrated probability.

Mitigation: Treat routing output as a prompt hint and validate the selected analysis path against the user's actual decision question.

## Reference(s):

- [Business reporting guide](references/business-reporting.md)
- [Business data analysis examples](references/examples.md)
- [Market research manual](references/market-research.md)
- [Metric and decomposition playbook](references/metric-playbook.md)
- [Router design and implementation](references/router-design.md)
- [Wei Liaozi business analysis framework](references/wei-liaozi-business-framework.md)
- [Wei Liaozi: Zhi Tan](https://ctext.org/wei-liao-zi/zhi-tan/zh)
- [Wei Liaozi: Bing Tan](https://ctext.org/wei-liao-zi/bing-tan/zhs)
- [Wei Liaozi: Gong Quan](https://ctext.org/wei-liao-zi/gong-quan/zhs)
- [Wei Liaozi: Tian Guan](https://ctext.org/wei-liao-zi/tian-guan/zhs)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code]

**Output Format:** [Markdown prose with tables, checklists, and optional structured routing fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not connect to business data sources; data, calculations, and web search are supplied by the host environment.]

## Skill Version(s):

1.6.0 (source: SKILL.md frontmatter, CHANGELOG.md, package.json, and server release metadata; released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
