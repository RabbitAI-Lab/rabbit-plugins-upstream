## Description:

Generates a website GEO and SEO audit across AI citability, platform readiness, technical infrastructure, content quality, and schema markup, with a composite GEO score and prioritized action plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and site operators use this skill to audit a public website's readiness for discovery, citation, and recommendation by AI systems. It produces a prioritized improvement plan for GEO, SEO, technical accessibility, content quality, and structured data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated audit report may recommend website, SEO, or schema changes that affect public content or search visibility.

Mitigation: Review GEO-AUDIT-REPORT.md before implementing recommendations, especially changes to schema, robots directives, page content, or technical infrastructure.

Risk: The skill fetches and analyzes pages from a user-provided website.

Mitigation: Use it only on sites you are authorized to audit and keep the artifact's bounded crawl behavior in place, including robots.txt checks, page limits, timeouts, and rate limiting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/geo-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report written as GEO-AUDIT-REPORT.md]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a composite GEO score, category scores, prioritized findings, quick wins, a 30-day action plan, and an appendix of analyzed pages.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
