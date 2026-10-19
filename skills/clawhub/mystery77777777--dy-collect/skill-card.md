## Description:

Collects engagement metrics for public Douyin videos in batches and exports the results as CSV.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and analysts use this paid service to collect likes, comments, saves, shares, and views for public Douyin videos, then summarize campaign results or export them to CSV.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default HTTP service endpoint may expose login tokens in transit.

Mitigation: Use a trusted HTTPS endpoint before logging in; avoid untrusted networks while the default HTTP endpoint is active.

Risk: Locally saved tokens, migrated settings, or insecure TLS options may compromise account access.

Mitigation: Protect the local token file, review migrated configuration, and do not enable insecure TLS.

Risk: Collecting videos consumes paid credits, including some unsuccessful or forced repeat requests.

Mitigation: Confirm the user's intended batch and available credits before submission; review failures before retrying.

## Reference(s):

- [dy-collect ClawHub listing](https://clawhub.ai/mystery77777777/skills/dy-collect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, CSV files]

**Output Format:** [Markdown summaries of JSON results, with optional CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 50 videos per batch; unavailable metrics may be blank rather than zero.]

## Skill Version(s):

1.0.0 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
