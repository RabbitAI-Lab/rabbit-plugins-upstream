## Description:

Provides command-line access to Douyin public content search, hot list lookup, creator post retrieval, and comment collection for social media analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, analysts, and developers use this skill to collect public Douyin content signals for topic discovery, competitor monitoring, public-comment review, hot-trend tracking, and downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin search terms, target URLs, and the GuaiKei API token to www.guaikei.com.

Mitigation: Install only when that data transfer is acceptable, keep the token in a protected local environment variable, and rotate the token if exposure is suspected.

Risk: Collected public user, creator, and comment data may be saved in a local logs directory.

Mitigation: Avoid shared or synced workspaces for sensitive analyses, review generated logs before sharing outputs, and delete logs when retention is not needed.

Risk: The security verdict is suspicious because token handling and local collection of public social data require review before installation.

Mitigation: Review the security guidance and deployment context before enabling the skill, especially for commercial or team use.

## Reference(s):

- [Server-resolved source repository](https://github.com/why20261/douyin-subscribe-analysis)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-subscribe-analysis)
- [GuaiKei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON data from Node.js command-line tools, with human-facing guidance or Markdown summaries when the agent explains results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0 or later and GUAIKEI_API_TOKEN; logs and result files may be written locally by the skill.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
