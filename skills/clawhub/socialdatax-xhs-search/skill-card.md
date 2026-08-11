## Description:

用于小红书数据分析、小红书笔记搜索、关键词检索、内容调研、竞品分析和趋势研究。覆盖 Xiaohongshu / XHS / RedNote note search，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search XHS/RedNote notes for keyword research, content planning, competitor research, market observation, and trend scanning through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and filters are sent to SocialDataX using SOCIALDATAX_API_KEY.

Mitigation: Use the skill only when SocialDataX XHS/RedNote research is intended, and confirm sensitive keywords or filters before sending them to the service.

Risk: Generic market or competitor research requests may not always intend XHS/RedNote as the data source.

Mitigation: Confirm that XHS/RedNote is the desired source before invoking the skill for broad research requests.

Risk: Search results are bounded by requested pages and filters, so they may not represent complete platform coverage.

Mitigation: State the fetched page count or time window and separate visible evidence from interpretation in the final response.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-search)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown summaries with CLI commands and SocialDataX search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and Node.js/npm for direct CLI use; preserves returned note URLs and pagination tokens exactly.]

## Skill Version(s):

0.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
