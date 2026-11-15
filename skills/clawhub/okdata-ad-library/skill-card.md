## Description:

通过 okdata API 查询 Meta 广告库和 Google 广告透明中心中的公开广告及广告主信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

广告研究人员和营销团队可按关键词或广告主查找 Meta 与 Google 平台上的公开广告，用于竞品观察和投放素材调研。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries go to an external API and may disclose the submitted search terms or advertiser identifiers; calls can incur fees.

Mitigation: Review query content before sending it, estimate the number of calls, set a max_price limit, and keep OKDATA_API_KEY out of chat.

Risk: The security assessment is marked partial, with medium confidence.

Mitigation: Review the skill and decide whether you trust the named API before installing or using it.

## Reference(s):

- [okdata Meta API documentation](https://okdata.online/zh/apis/meta/)
- [ClawHub release page](https://clawhub.ai/conn-ho/skills/okdata-ad-library)
- [okdata remote MCP endpoint](https://api.okdata.online/mcp)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [List results may be paginated; API calls are billed per request.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
