## Description:

Generates A-share limit-up and Dragon-Tiger research reports with a four-layer L1 to L2.5 to L3 screening funnel, wealth-password strategy scoring, and HTML/PDF/PPTX report outputs.

This skill is for research and development only.

## Publisher:

[yjkj999999](https://clawhub.ai/user/yjkj999999)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate A-share Dragon-Tiger board reports, daily market reviews, four-layer screening results, strategy scoring tables, and risk-aware trading checklists. It is framed as education and research material and states that its outputs are not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rendered reports may include unsafe or unescaped content from JSON or upstream market snapshots.

Mitigation: Run in an isolated project or virtual environment and use only trusted data until HTML escaping and a restrictive browser configuration are added.

Risk: Generated PPTX output may contain sample or stale hardcoded data.

Mitigation: Verify report dates and source data manually before sharing or relying on generated PPTX files.

Risk: Finance report outputs could be mistaken for actionable investment advice.

Mitigation: Keep the education/research disclaimer visible and review data freshness, assumptions, and risk controls before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yjkj999999/skills/a-share-dragon-tiger-report)
- [Publisher profile](https://clawhub.ai/user/yjkj999999)
- [Project homepage](https://github.com/yjkj999999/a-share-dragon-tiger-strategy)
- [README](README.md)
- [Wealth Password Strategy Guide](docs/wealth-password-strategy.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands plus generated HTML, PDF, and PPTX report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may use local sample data when live market sources are unavailable; generated reports should display data date, source, and delay.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
