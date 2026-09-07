## Description:

乙方投标助手使用知了标讯招中标数据接口，帮助投标方查询招标和中标公告、分析竞争对手、寻找合作方与供应商，并以表格或图表输出投标决策依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query Chinese tender and award data, analyze bidder competitors and market pricing, identify potential suppliers or partners, and support bid decisions from a vendor-side perspective.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration can send a stable device fingerprint derived from platform, CPU architecture, and a hashed MAC address to the vendor service.

Mitigation: Use a managed ZLBX_API_KEY or local API key configuration when possible, and require explicit user consent before automatic registration or device feature collection.

Risk: The skill can store a bearer API key in a local configuration file.

Mitigation: Prefer environment-managed secrets, do not expose API keys in chat output, and review local credential storage before installation.

Risk: Bid and company queries may return project contact data from the service.

Mitigation: Show contact data only as returned by the service, respect masked contact responses, and avoid bulk export or attempts to unmask contact information.

Risk: Responses may include vendor promotional or referral links.

Mitigation: Review generated answers for unnecessary promotional material and keep links limited to user-relevant account, documentation, or workflow needs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/bidding-yifangbao)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with tables or charts, plus REST request payloads and command snippets when setup or API access is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local API key configuration; may query account usage and bid contact data returned by the vendor service.]

## Skill Version(s):

2.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
