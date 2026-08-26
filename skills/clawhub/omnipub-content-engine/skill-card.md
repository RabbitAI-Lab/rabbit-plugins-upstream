## Description:

AI-driven content lifecycle management skill for topic research, content generation, fact checking, visual planning, GEO optimization, WeChat and Toutiao publishing preparation, and post-publication analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mikogeyu-cell](https://clawhub.ai/user/mikogeyu-cell)

### License/Terms of Use:

MIT

## Use Case:

Content teams, creators, and operators use this skill to manage a gated Chinese-language publishing workflow from topic selection through platform-specific formatting, draft publication, and analytics review. It is especially focused on WeChat Official Account and Toutiao workflows that need human approval before public posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles publishing credentials and public-posting workflows.

Mitigation: Review before installation, use a dedicated low-privilege WeChat or Toutiao account where possible, and test publish or delete flows on disposable drafts before using production accounts.

Risk: Credential values, token material, or local credential paths may be exposed during setup or execution.

Mitigation: Keep credentials out of prompts, logs, and committed config files, avoid committing config.yaml, and remove token-printing behavior before real account use.

Risk: Automated publishing can post or prepare content that has not received human approval.

Mitigation: Preserve the documented gate workflow, especially final publication authorization, and require human review before any platform publish step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mikogeyu-cell/skills/omnipub-content-engine)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [Topic research workflow](references/01-topic-research.md)
- [Content generation workflow](references/02-content-generation.md)
- [Fact-checking workflow](references/03-fact-checking.md)
- [Charts and infographics workflow](references/04-charts-infographics.md)
- [Footer and style workflow](references/05-footer-styles.md)
- [GEO optimization workflow](references/06-geo-optimization.md)
- [Publishing workflow](references/07-publishing.md)
- [Analytics workflow](references/08-analytics.md)
- [WeChat CSS constraints](references/wechat-css-constraints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text guidance with Python CLI commands, configuration snippets, HTML output, and platform-specific publishing artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces drafts, reports, prompts, sanitized HTML, publishing preparation files, and analytics summaries depending on the selected workflow stage.]

## Skill Version(s):

2.0.0 (source: release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
