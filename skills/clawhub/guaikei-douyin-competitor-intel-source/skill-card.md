## Description:

Fetches public Douyin search results, creator posts, video comments, and hot-list data through Guaikei-backed CLI commands for content research, competitor analysis, sentiment monitoring, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to collect structured public Douyin data for content planning, competitor monitoring, comment analysis, and trend tracking. It is intended for user-requested Douyin research workflows, not publishing, editing, downloading, or private account access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Douyin URLs, and request metadata are sent to the third-party guaikei.com service with the configured token.

Mitigation: Use the skill only for explicit Douyin research requests, avoid sensitive topics or personal data, and ensure token use is approved for the task.

Risk: Successful search, comment, and account runs save full JSON logs locally, which may contain sensitive research topics or personal data.

Mitigation: Review generated logs after use and delete or retain them according to the user's approved data-handling process.

Risk: The skill can activate on broad short-video research phrasing even when the user does not explicitly name Douyin.

Mitigation: Confirm Douyin is the intended source before running commands for ambiguous short-video, competitor, or trend-research requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-competitor-intel-source)
- [Usage Documentation](readme.md)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei Service Site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Pure JSON on stdout with operational logs on stderr; successful search, comment, and account runs also save JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=16.14 and GUAIKEI_API_TOKEN; individual commands support limits up to 10000 returned records.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, constants.js, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
