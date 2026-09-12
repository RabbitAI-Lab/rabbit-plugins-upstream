## Description:

热门标讯挖掘助手-火标网，当用户需要进行行业热度分析、统计Top采购商或聚合近期高频中标记录时调用，调用多维度聚合统计接口，呈现特定行业的市场热度与集中度趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users, business analysts, procurement teams, and agents use this skill to search and aggregate tender, award, company, purchaser, supplier, brand, price, and account data from the Huobiaowang/Zhiliaobiaoxun service. It is most useful for market heat analysis, opportunity discovery, competitor research, and recent high-frequency award summaries.

### Deployment Geography for Use:

Global; data coverage and workflows are focused on Chinese tender and procurement records.

## Known Risks and Mitigations:

Risk: The skill depends on the provider's hosted APIs and may store an API key under ~/.zlbx/config.json.

Mitigation: Install only if the provider relationship is acceptable, prefer a manually configured ZLBX_API_KEY, and avoid exposing API keys in conversation output.

Risk: The opt-in auto-registration flow sends a hashed MAC-derived device identifier for trial deduplication.

Mitigation: Use manual API-key configuration when possible, avoid auto-registration on shared machines, and require user consent before collecting device features.

Risk: The skill handles contact data and service-returned masked phone numbers.

Mitigation: Display contact data only as returned by the service, do not attempt to deanonymize masked values, and avoid bulk contact export.

Risk: Generated responses may include promotional links or broadened company scopes.

Mitigation: Review generated output for promotional content and confirm company scope before acting on market or company analysis.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/liu-jiapeng/skills/trending-miner-huobiaowang)
- [Skill overview and tool list](artifact/SKILL.md)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration flow reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with tables, concise summaries, JSON REST request bodies, and inline shell commands when setup is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or an opt-in registration flow; responses may include service links, masked contact data, and account status guidance.]

## Skill Version(s):

2.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
