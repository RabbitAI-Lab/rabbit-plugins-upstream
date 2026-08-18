## Description:

Audits Next.js applications for Core Web Vitals, bundle size, rendering strategy, image optimization, data-fetching issues, and provides actionable TypeScript fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and frontend engineers use this skill to audit slow Next.js applications and prioritize fixes for Core Web Vitals, bundle size, rendering, images, and data fetching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rendering-strategy, caching, and dependency recommendations can change application behavior if applied without review.

Mitigation: Review each suggested fix before applying it and validate behavior, routing, caching, and Core Web Vitals in a staging environment.

Risk: Projected performance improvements may not match real-world results because the skill does not run Lighthouse or PageSpeed Insights.

Mitigation: Confirm projected gains with field or lab measurements after implementing changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/nextjs-perf-optimizer)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown reports with TypeScript code snippets and prioritized recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations should include current and fixed code, distinguish App Router from Pages Router, and order fixes by impact and ease.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
