## Description:

Weekly SEO Health Audit is a read-only SEO audit skill that surfaces quick-win keywords, low-effort site fixes, and a one-page prioritized opportunity list for a website.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hkim08](https://clawhub.ai/user/hkim08)

### License/Terms of Use:

MIT-0

## Use Case:

External site owners, SEO teams, and developers use this skill to run a read-only weekly health audit on a public website and prioritize quick-win keyword and technical SEO opportunities before deciding which changes to make.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit may make HTTP or browser requests to unsafe or private destinations if the user provides non-public URLs.

Mitigation: Use it only for public websites unless the runtime blocks localhost, intranet, private cloud, metadata-service, and authenticated destinations.

Risk: SEO opportunities and reported conversion-rate signals may be incomplete or misleading if treated as guaranteed outcomes.

Mitigation: Review recommendations before acting and treat cited performance numbers as research signals, not promises of rankings or results.

Risk: Fetched page content may contain prompt-injection text that tries to redirect the agent.

Mitigation: Treat website content as data and ignore page instructions that conflict with the audit task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hkim08/skills/weekly-seo-health-audit)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [One-page Markdown report with prioritized bullets and cited evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; no persistence, API keys, or site changes.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
