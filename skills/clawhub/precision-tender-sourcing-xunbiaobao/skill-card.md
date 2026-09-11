## Description:

精准寻标与获客引擎-寻标宝，当用户需要通过招投标数据进行客户拓展、寻找潜在采购单位或分析企业上下游时调用，重点调用企业合作客户及供应商查询接口，输出清晰的获客目标列表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, procurement, and market-analysis users use this skill to find tender opportunities, identify likely purchasers and suppliers, analyze company bidding relationships, and produce concise lead lists from Zhiliaobiaoxun tender data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional auto-registration can send a hashed device identifier to the vendor and persist an API key in a local plaintext config file.

Mitigation: Prefer setting ZLBX_API_KEY directly; if auto-registration is used, obtain user consent first, disclose the collected device fields, and protect the local config file.

Risk: Quota recovery and payment flows can surface vendor auto-login or referral links.

Mitigation: Show billing or recovery links only when account state requires them, and make clear that the link goes to the vendor account portal.

Risk: Contact information may be masked by account tier and could be sensitive when returned.

Mitigation: Display contact fields only as returned by the API, do not attempt to bypass masking, and avoid bulk export of contact records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/precision-tender-sourcing-xunbiaobao)
- [API search reference](references/api-search.md)
- [API company reference](references/api-company.md)
- [API market reference](references/api-market.md)
- [API account reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)
- [Zhiliaobiaoxun data API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account portal](https://ai.zhiliaobiaoxun.com/?ch=s29)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown summaries with tables and JSON-shaped REST request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-consented auto-registration; account tier can affect whether contact fields are masked.]

## Skill Version(s):

2.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
