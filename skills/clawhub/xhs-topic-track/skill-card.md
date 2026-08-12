## Description:

xhs-topic-track helps agents search Xiaohongshu public notes by keyword, fetch note details and comments, and retrieve creator post lists for reputation monitoring, content research, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, content operators, and analysts use this skill to collect structured Xiaohongshu public-data results for keyword research, note and comment review, creator monitoring, and downstream summaries or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu links, and the GUAIKEI_API_TOKEN are sent to the guaikei.com API.

Mitigation: Install and run the skill only when the user accepts that external API data flow and has authorization to use the token.

Risk: Generated log files may contain sensitive business research data or collected public-content results.

Mitigation: Treat the logs directory as sensitive, limit access to appropriate users, and remove retained result files when they are no longer needed.

## Reference(s):

- [Skill page](https://clawhub.ai/engheng-art/skills/xhs-topic-track)
- [Guaikei API service](https://www.guaikei.com)
- [Options and usage reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON result objects with concise status text and markdown command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes result JSON to a local logs directory.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
