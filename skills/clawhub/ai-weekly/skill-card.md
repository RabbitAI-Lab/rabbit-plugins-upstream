## Description:

Generates source-linked weekly AI news as a searchable single-file HTML report or a brief Markdown digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Readers, editors, and developers use this skill to compile recent AI news from public feeds into a cited weekly report or a short conversational briefing. Optional workflows can publish the report or deliver it to Feishu.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional publishing and delivery paths may use account credentials and send a report to external services.

Mitigation: Keep ordinary reports local; enable deployment or Feishu delivery only when needed and use least-privilege, short-lived tokens.

Risk: Optional operations can change GitHub Pages settings or install scheduled jobs.

Mitigation: Review and explicitly approve publishing, Pages configuration changes, and scheduler installation before running them.

## Reference(s):

- [AI Weekly Report on ClawHub](https://clawhub.ai/elisabeth15501/skills/ai-weekly)
- [Project homepage](https://github.com/Elisabeth15501/ai-weekly)
- [Sample AI news report](https://elisabeth15501.github.io/ai-weekly/AI_News_2026-09-07.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML files]

**Output Format:** [Single-file HTML report or Markdown news digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source links accompany news items; optional publishing and Feishu delivery.]

## Skill Version(s):

4.1.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
