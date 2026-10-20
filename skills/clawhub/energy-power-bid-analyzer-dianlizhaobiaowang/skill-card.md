## Description:

检索中国能源电力行业招投标信息，汇总国网、南网等采购项目并分析设备及工程的中标集中度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

采购、销售与市场分析人员可检索中国电力及新能源项目，追踪招中标动态，并比较供应商与品牌的中标情况。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Account setup may create a local API key and register a trial account using a hashed device identifier.

Mitigation: Supply your own ZLBX_API_KEY to avoid automatic registration; otherwise review the requested device data and consent before registration.

Risk: The API key stored in ~/.zlbx/config.json grants access to an account and could be exposed if the file is shared.

Mitigation: Keep the key and local configuration private; avoid including credentials in reports or shared files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thuanlynham-stack/skills/energy-power-bid-analyzer-dianlizhaobiaowang)
- [Search API reference](artifact/references/api-search.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account setup and registration reference](artifact/references/auto-register.md)
- [Skill setup documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with summaries, tables and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available bid data, selected filters and account access.]

## Skill Version(s):

1.0.10 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
