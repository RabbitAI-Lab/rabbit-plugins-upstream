## Description:

Searches Xiaohongshu (RedNote/xhs) public notes, retrieves note details and comments, and lists a creator's public posts for trend, content, and competitive research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, analysts, and agent developers use this skill to collect public Xiaohongshu search results, note details, comments, and creator posts, then summarize trends, topics, engagement signals, and audience feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, URLs, and a GUAIKEI API token to guaikei.com.

Mitigation: Confirm the external data sharing and token use are acceptable before installing or running the skill.

Risk: Local logs can contain saved research results, URLs, comments, and creator metadata.

Mitigation: Periodically clean or protect the logs directory according to the user's data retention and access-control requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-trend-pulse)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful runs can save JSON result files under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
