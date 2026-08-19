## Description:

Retrieves public Xiaohongshu/RedNote search results, note details, comments, and creator posts for content research and social media analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as content creators, marketers, analysts, and operators use this skill to collect public Xiaohongshu content, comments, interaction metrics, and creator posts for topic research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com during use.

Mitigation: Install and run only when the user is comfortable sharing those inputs with the third-party API provider.

Risk: Generated logs may contain sensitive research topics, account links, comments, or competitive monitoring data.

Mitigation: Review, protect, or delete the logs directory after use when outputs include sensitive information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-note-detail-guaikei)
- [Guaikei API and token site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; command results are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command output may also be saved under a local logs directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
