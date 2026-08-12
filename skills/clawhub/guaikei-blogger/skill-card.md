## Description:

Searches Xiaohongshu public content, note details, comments, and creator posts through the Guaikei API and returns structured data for analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketers, analysts, and operations teams use this skill to collect public Xiaohongshu keyword results, note details, comments, and creator post data for content research, competitor monitoring, trend analysis, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu links, and the GUAIKEI_API_TOKEN are sent to the third-party guaikei.com API.

Mitigation: Use the skill only when the user accepts that data sharing, and configure the token only in trusted environments.

Risk: Collected content, target URLs, and execution results may remain in local log files after a run.

Mitigation: Treat logs as potentially sensitive, review retention requirements, and delete or protect logs when they are no longer needed.

Risk: The skill is intended for public Xiaohongshu data and does not support private, hidden, or login-only content.

Mitigation: Restrict use to public keywords, note links, and creator profile links, and avoid requests for non-public data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/engheng-art/skills/guaikei-blogger)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Structured JSON results with command status messages and local log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes collected results to logs/.]

## Skill Version(s):

1.0.0 (source: server release evidence, artifact frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
