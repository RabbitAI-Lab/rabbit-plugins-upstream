## Description:

A Xiaohongshu public-data insight skill for keyword search, note details, comments, and creator post lists, supporting content research, competitor analysis, KOL screening, and trend discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, content operators, marketers, and analysts use this skill to fetch structured Xiaohongshu public data for content ideation, competitor monitoring, comment analysis, KOL screening, and trend reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note URLs, profile URLs, and the GUAIKEI_API_TOKEN to a third-party API service.

Mitigation: Use only in environments where sharing those inputs with the third-party service is approved, and keep the API token scoped, private, and out of shared logs.

Risk: Fetched social-media results are automatically stored in local JSON log files.

Mitigation: Treat generated logs as sensitive, limit access on shared machines, and remove logs when they are no longer needed.

Risk: The server security verdict is suspicious because token and query data are sent through third-party API URL parameters.

Mitigation: Review the skill before installation and confirm that API-token handling and data retention meet the target environment's policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-insight-generate)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and structured JSON results from CLI execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI tools write fetched results to local JSON log files under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
