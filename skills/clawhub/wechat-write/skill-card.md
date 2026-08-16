## Description:

This skill helps users search RedFox WeChat Official Account viral article data by keyword, analyze traffic patterns, and generate publish-ready WeChat Official Account articles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content operators, MCN teams, and brand planners use this skill to research recent WeChat viral article patterns, adapt those patterns to a topic or product recommendation, and produce a complete article draft with titles, tags, and source pattern notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends WeChat article keywords and date ranges to redfox.hk.

Mitigation: Use only topics that are appropriate to share with RedFox and avoid confidential client, campaign, or regulated subject matter unless approved.

Risk: The workflow asks users for personal writing samples to adapt style.

Mitigation: Provide short sanitized excerpts instead of diaries, private notes, client material, regulated data, or confidential drafts.

Risk: The helper script may print an unrelated RedFox sales contact line in its output.

Mitigation: Review generated article drafts and remove unrelated contact or promotional text before publication.

Risk: Generated articles may reflect incorrect, misleading, or overly promotional conclusions from trend analysis.

Mitigation: Review the cited viral-pattern notes and article draft for accuracy, brand fit, and WeChat community compliance before publishing.

## Reference(s):

- [公众号爆款数据格式说明](artifact/references/gzh_trend_data_format.md)
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=github)
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-write)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown article draft with recommended titles, body copy, core viewpoint, tags, viral-pattern source notes, and optional differentiation analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; uses keyword and date-range inputs for RedFox trend lookup, defaulting to recent data and expanding the query window when results are sparse.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
