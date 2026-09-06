## Description:

Fetches public Kuaishou data by searching videos, listing creator posts, and retrieving video comments, with structured JSON results for downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content analysts, marketers, MCN teams, and creators use this skill to collect public Kuaishou search results, creator posts, and video comments for trend research, competitor monitoring, KOL screening, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and target URLs are sent to the third-party guaikei.com API using GUAIKEI_API_TOKEN.

Mitigation: Use the skill only where third-party API use is approved, and provide the token through a protected environment variable.

Risk: Successful fetches may save collected social-media data locally under logs/.

Mitigation: Review, protect, and delete saved logs when no longer needed, especially on shared or corporate machines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-open-data-fetcher)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with command-line usage and structured JSON results from the data-fetching scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful results may be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, and changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
