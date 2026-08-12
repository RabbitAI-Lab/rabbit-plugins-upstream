## Description:

guaikei-xhs-insight retrieves public Xiaohongshu notes, note details, comments, and creator post lists by keyword or URL for content research, competitor monitoring, KOL screening, and trend insight without account login or publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External content strategists, marketers, analysts, and agent developers use this skill to collect structured public Xiaohongshu data for topic research, competitor monitoring, KOL screening, comment analysis, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords or URLs are sent to guaikei.com with the configured GUAIKEI_API_TOKEN.

Mitigation: Use the skill only when the user is comfortable with this data externalization and has authorization to query the public data through the third-party API.

Risk: Returned datasets can be saved under the skill's logs directory and may contain sensitive business research.

Mitigation: Protect or delete generated logs according to the user's data handling requirements.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-insight)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples; CLI execution returns structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; API results may be saved under the skill logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
