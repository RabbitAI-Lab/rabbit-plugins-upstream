## Description:

Searches Xiaohongshu public content by keyword or fetches note details, comments, and creator post lists so agents can compare engagement, content formats, posting cadence, and competitor content strategy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, content operators, and analysts use this skill to collect Xiaohongshu public-data search results, note/comment details, and creator post lists for competitor monitoring, topic research, trend analysis, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, links, API token material, and returned public-data results are sent to the third-party Guaikei API service.

Mitigation: Use the skill only with data you are authorized to send to guaikei.com, configure the API token deliberately, and avoid submitting private or sensitive inputs.

Risk: Result files remain in the local logs directory after command execution.

Mitigation: Protect or delete local log files according to the user's data-retention needs, especially when results support confidential business analysis.

Risk: The skill is intended for public Xiaohongshu data and does not support private, hidden, or login-gated content.

Mitigation: Limit usage to publicly accessible Xiaohongshu keywords and links, and do not use the skill to bypass access controls or platform restrictions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-competitor-watch)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with shell command examples and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results are printed as JSON and saved as local JSON files under the skill logs directory.]

## Skill Version(s):

1.0.0 (source: SKILL.md metadata, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
