## Description:

通过 okdata API 查询 B 站公开视频、评论、用户资料和趋势数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

AI agents and people researching Bilibili content can search public videos, inspect engagement and comments, check current rankings, and look up creator profiles or uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and the skill sends requests to the external api.okdata.online service using an API key.

Mitigation: Before installing, consider whether you trust api.okdata.online and are comfortable using an API key with its service. Keep the key in the OKDATA_API_KEY environment variable rather than sharing it in chat.

Risk: API calls are billed per request.

Mitigation: Estimate the number and cost of calls before using the skill, and set max_price for calls where supported.

## Reference(s):

- [okdata Bilibili API documentation](https://okdata.online/zh/apis/bilibili/)
- [ClawHub skill release](https://clawhub.ai/conn-ho/skills/okdata-bilibili)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown, Analysis]

**Output Format:** [Structured API data with conversational or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by selected Bilibili data endpoint and may be paginated.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
