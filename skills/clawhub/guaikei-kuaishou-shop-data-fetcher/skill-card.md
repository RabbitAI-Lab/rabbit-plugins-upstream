## Description:

Fetches public Kuaishou data for video keyword search, creator public posts, and video comments, returning structured JSON for analysis and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketing teams, MCN operators, and analysts use this skill to collect public Kuaishou search results, creator posts, and video comments for content research, competitor monitoring, KOL discovery, trend analysis, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Kuaishou search terms, profile or video URLs, and the GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use only when the user is comfortable with that data transfer and keep the API token protected in the execution environment.

Risk: Collected public results and query context may be written to the local logs/ directory.

Mitigation: Delete or restrict access to generated logs in shared workspaces.

Risk: The skill is limited to public Kuaishou data and may return empty or error statuses for unavailable, private, deleted, or unsupported inputs.

Mitigation: Check the returned status and error code before summarizing results, and do not treat empty or failed responses as successful evidence.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-shop-data-fetcher)
- [Guaikei API service](https://www.guaikei.com)
- [Complete option reference](references/options.md)
- [Release changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON results from the skill scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful runs can save collected results and query context under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
