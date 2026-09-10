## Description:

Fetches public Kuaishou search results, creator post lists, and video comments through the Guaikei API so agents can return structured data for content research, competitor monitoring, KOL screening, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, marketers, MCN teams, and analysts use this skill to gather public Kuaishou data for topic research, competitor monitoring, creator analysis, and comment insight workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search terms, post URLs, comment URLs, and the GUAIKEI_API_TOKEN are sent to the third-party Guaikei API service.

Mitigation: Install and use the skill only when that data transfer is acceptable, and scope the token to the intended use where possible.

Risk: Generated logs may contain scraped public comments, URLs, creator data, and business research results.

Mitigation: Review, retain, or delete the logs directory according to the user's data handling policy.

Risk: The skill is limited to public Kuaishou data and may return empty or error results for deleted, private, login-required, or unsupported content.

Mitigation: Check the returned status and error code before using results in analysis or reports.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-public-post-fetcher)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON results from executed scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes fetched results to a local logs directory.]

## Skill Version(s):

1.0.0 (source: release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
