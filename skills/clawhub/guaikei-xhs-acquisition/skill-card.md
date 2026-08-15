## Description:

Searches public Xiaohongshu notes by keyword, retrieves note details, comments, and public profile posts, and returns structured engagement data for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External marketers, content creators, analysts, and agents use this skill to collect public Xiaohongshu notes, comments, engagement metrics, and profile-post lists for topic research, trend monitoring, competitor review, and report generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords or links, including query parameters, are sent to guaikei.com using GUAIKEI_API_TOKEN.

Mitigation: Use only authorized public inputs and confirm data-sharing approval before running the skill.

Risk: Generated logs may contain sensitive research targets, profile links, comments, or returned public content.

Mitigation: Review, restrict access to, or delete generated logs after use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-acquisition)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [JSON results with status and error fields, plus Markdown guidance and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save JSON logs locally under logs/ and requires GUAIKEI_API_TOKEN for API access.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
