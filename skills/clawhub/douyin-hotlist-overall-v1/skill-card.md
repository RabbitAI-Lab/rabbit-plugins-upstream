## Description:

Helps agents query Douyin public content, hot lists, creator posts, and comments for short-video trend, competitor, and public-opinion analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and marketing or operations analysts use this skill to collect structured public Douyin data for content discovery, hot-list tracking, competitor monitoring, creator post review, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, creator identifiers, video identifiers, requested limits, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use only when that data transfer is acceptable, keep the API token secret, and rotate or revoke the token if exposure is suspected.

Risk: Collected Douyin results can be saved locally, including comment datasets or competitive research outputs.

Mitigation: Avoid shared or synced workspaces for sensitive runs, protect the logs directory, and delete or de-identify saved result files when they are no longer needed.

Risk: Returned public data can include usernames, public posts, and comment text that may be sensitive in reports or redistribution.

Mitigation: Use the data for authorized analysis only and de-identify user-facing reports when publishing or sharing results.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/why20261/douyin-hotlist-overall-v1)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-hotlist-overall-v1)
- [抖音数据获取官网](https://www.guaikei.com)
- [完整选项参数说明](references/options.md)
- [更新日志](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; invoked CLIs emit structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; some commands save JSON result files under a local logs directory.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
