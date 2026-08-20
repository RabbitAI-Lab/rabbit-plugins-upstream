## Description:

Fetches read-only public Douyin search results, author posts, video comments, and hot-list data through Guaikei API commands for marketing analysis, account operations, topic research, and public-opinion monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve structured public Douyin data for keyword research, competitor monitoring, comment analysis, author-post tracking, and trend reporting. It is not intended for private account data, authenticated Douyin actions, or content publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, video URLs, author URLs, and GUAIKEI_API_TOKEN are sent to the third-party guaikei.com API.

Mitigation: Use the skill only when that data flow is acceptable, avoid confidential monitoring terms or proprietary targets, and protect the token as a secret.

Risk: Returned public Douyin data may be saved under the skill's local logs directory.

Mitigation: Review stored logs for sensitivity and delete them when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-author-posts)
- [Guaikei API website](https://www.guaikei.com)
- [Complete option reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, text, guidance]

**Output Format:** [Markdown guidance with command examples; executed commands return JSON and may save local JSON logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; stdout is JSON while logs and status messages use stderr.]

## Skill Version(s):

1.0.0 (source: release metadata, package.json, skill metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
