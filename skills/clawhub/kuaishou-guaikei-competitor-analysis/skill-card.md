## Description:

Searches public Kuaishou videos by keyword, retrieves public creator post lists and video comments, and returns structured JSON for competitor analysis, KOL selection, trend insight, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External content creators, brand marketers, MCN teams, and data analysts use this skill to collect public Kuaishou search results, creator posts, and comments for topic discovery, competitor monitoring, KOL screening, sentiment review, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Kuaishou keywords, profile or video URLs, and GUAIKEI_API_TOKEN to the Guaikei API service.

Mitigation: Confirm the external API service and token-sharing model are acceptable before installation or execution.

Risk: Local logs can retain search terms, profile URLs, comments, or analysis outputs that reveal sensitive business research.

Mitigation: Review and periodically delete the local logs directory when collected data should not persist.

Risk: The skill is limited to public Kuaishou data and depends on a third-party API service.

Mitigation: Use it only for public-data workflows and handle API errors, rate limits, and empty results without inventing conclusions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/kuaishou-guaikei-competitor-analysis)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API Calls, JSON]

**Output Format:** [Markdown guidance with shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful calls return public Kuaishou data as JSON; local logs may contain search terms, profile or video URLs, comments, and analysis outputs.]

## Skill Version(s):

1.0.0 (source: package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
