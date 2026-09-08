## Description:

Collects structured public Kuaishou data by keyword search, creator posts, or video comments for trend, competitor, and sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content, marketing, MCN, and data analysis users can use this skill through an agent to fetch public Kuaishou search results, creator posts, and video comments for content research, competitor monitoring, KOL screening, and sentiment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile or video URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only where that data sharing is approved, store the token as a secret environment variable, and avoid sending sensitive internal research terms.

Risk: Generated logs may contain sensitive research data.

Mitigation: Keep logs out of source control and shared folders, and redact them before reuse or external sharing.

Risk: Fetches can return empty or error statuses instead of usable data.

Mitigation: Check status and error_code before summarizing results, and do not treat empty or failed responses as evidence.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-rank-data-fetcher)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Structured JSON with status and error fields, plus optional concise Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful and failed fetches may create local timestamped logs.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, changelog; artifact frontmatter lists 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
