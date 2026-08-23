## Description:

Deep Research guides an agent through scoped, parallel web research with citation discipline, confidence tracking, conflict surfacing, and a cited Markdown report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill when they need an agent to research a topic across many web sources and produce a sourced report. It is suited for market, domain, technical, competitive, product, academic, person or organization, financial, legal, trend, and community research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports about people, companies, employee complaints, or social sentiment may expose private or identifying details or overstate uncorroborated public claims.

Mitigation: Keep the research scope explicit, avoid private or identifying personal details, and treat forum or social claims as low-confidence unless independently corroborated.

Risk: Broad web research can produce misleading conclusions when sources conflict or when critical figures come from weak evidence.

Mitigation: Require source URLs, accessed dates, confidence labels, multiple independent sources for critical claims, and explicit discussion of source conflicts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/deep-research)
- [OpenClaw Homepage](https://github.com/samber/cc-skills)
- [Report Template](assets/report-template.md)
- [Citation Rules](references/citations.md)
- [Parallel Search](references/parallel-search.md)
- [Market Research Guide](references/market.md)
- [Domain Research Guide](references/domain.md)
- [Technical Research Guide](references/technical.md)
- [Competitive Research Guide](references/competitive.md)
- [Product Research Guide](references/product.md)
- [Academic Research Guide](references/academic.md)
- [Person and Organization Research Guide](references/org.md)
- [Financial Research Guide](references/financial.md)
- [Legal Research Guide](references/legal.md)
- [Trend Research Guide](references/trend.md)
- [Community Research Guide](references/community.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown report with inline source links, accessed dates, confidence labels, and optional PDF export guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a local research report and may propose shell commands for fetching source material or exporting Markdown to PDF.]

## Skill Version(s):

1.2.0 (source: server release evidence and artifact frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
