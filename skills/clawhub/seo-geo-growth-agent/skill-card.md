## Description:

Read-only SEO and GEO opportunity analysis with evidence-backed backlog output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anhdn](https://clawhub.ai/user/anhdn)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, growth, and content teams use this agent to analyze supplied or allowlisted read-only sources for SEO/GEO audits, competitor gaps, opportunities, and content briefs. It returns evidence-backed recommendations and reviewable backlog artifacts without publishing or changing systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search, analytics, or source connectors could expose broader access than the skill needs.

Mitigation: Before installation, allow only read-only connectors scoped to the intended site, competitors, or supplied sources.

Risk: Backlog drafts or content recommendations could be mistaken for approved publishing or data-changing actions.

Mitigation: Use outputs as reviewable proposals only and route any write, CMS, backlog, analytics, or publishing action through an explicitly authorized downstream workflow.

Risk: Insufficient evidence can lead to unsupported SEO or GEO recommendations.

Mitigation: Require source-backed observations, record unavailable signals in limitations, and return SKIP when the evidence boundary is not sufficient.

## Reference(s):

- [Capability detection](references/capability-detection.md)
- [Growth backlog template](templates/growth-backlog.md)
- [Backlog item template](templates/backlog-item.md)
- [ClawHub skill page](https://clawhub.ai/anhdn/skills/seo-geo-growth-agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Structured text and Markdown backlog artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recommendations only; returns SKIP when the target, evidence, or read-only capability boundary is insufficient.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
