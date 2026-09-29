## Description:

Forklift expert helps agents answer forklift and industrial vehicle questions across brands, selection, maintenance, standards, market trends, sales rankings, tender briefings, and safety management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangpf6698](https://clawhub.ai/user/yangpf6698)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and operations teams use this skill to generate forklift-domain guidance, structured comparisons, standards lookups, maintenance and safety advice, market summaries, and tender briefings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live lookup results for standards, sales, market, and tender information can be incomplete, outdated, or source-dependent.

Mitigation: Require retrieval dates and source links, prefer authoritative standards and industry sources, and review generated summaries before use.

Risk: Tender-broadcast requests may create a persistent HTML report in /workspace that includes the query topic and public tender details.

Mitigation: Review generated reports before sharing and remove unnecessary query context or sensitive operational notes.

Risk: Forklift safety, maintenance, and compliance guidance can affect operational decisions.

Mitigation: Use the skill output as guidance and require qualified human review before applying it to equipment, safety, procurement, or compliance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangpf6698/skills/forklift)
- [README](README.md)
- [Usage guide](usage-guide.md)
- [Forklift standards](references/standards.md)
- [Online standard lookup](references/standard-retrieval.md)
- [Safety regulation](references/safety-regulation.md)
- [Safety management](references/safety-management.md)
- [Market trends](references/market-trends.md)
- [Sales news](references/sales-news.md)
- [Tender broadcast](references/tender-broadcast.md)
- [SVG chart output](references/svg-chart.md)
- [Multilingual behavior](references/i18n.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Files]

**Output Format:** [Markdown with tables, source links, inline SVG code, and self-contained HTML for tender broadcasts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use live web lookup for current standards, sales, market, and tender information; tender-broadcast requests may create a persistent HTML report in /workspace.]

## Skill Version(s):

2.0.6 (source: ClawHub release metadata; artifact frontmatter lists 2.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
