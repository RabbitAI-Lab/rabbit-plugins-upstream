## Description:

Technical SEO audit with GEO-specific checks for crawlability, indexability, security, performance, server-side rendering, and AI crawler access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

SEO, growth, and web engineering teams use this skill to audit public website pages for technical search visibility and GEO readiness. It guides an agent through URL collection, HTTP and raw HTML checks, scoring, and a Markdown audit report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to make HTTP requests to websites selected for audit.

Mitigation: Use it only for sites the operator is authorized to assess, and review target URLs before allowing fetches.

Risk: Recommendations about allowing AI crawlers can affect content licensing and data-use preferences.

Mitigation: Review crawler-access recommendations against the organization's licensing, robots.txt, and AI training policies before applying changes.

Risk: The generated audit may contain incorrect or outdated SEO guidance if applied without review.

Mitigation: Have a qualified SEO or web engineering reviewer validate findings before changing production site configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/geo-technical)
- [ClawHub publisher profile](https://clawhub.ai/user/asale-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown audit report with tables, findings, recommendations, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local GEO-TECHNICAL-AUDIT.md report after fetching the user-specified website pages.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
