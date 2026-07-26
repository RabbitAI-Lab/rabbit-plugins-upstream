## Description: <br>
招投标大数据 AI 分析平台，用自然语言完成市场分析、商机研判与趋势预测：多维聚合统计（月/季/年/省份/行业/品牌）、Top采购单位/中标单位/中标品牌、历史中标价格走势、潜在中标候选预测。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External procurement, sales, and business development users use this skill to analyze bidding markets, identify purchasers and suppliers, review price trends, and produce opportunity reports from Zhiliaobiaoxun bidding data. <br>

### Deployment Geography for Use: <br>
Global; the service and source data focus on Chinese bidding and procurement markets. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically register a device with a remote service, sending host identifiers and writing a returned API key to ~/.zlbx/config.json. <br>
Mitigation: Prefer a manually provided ZLBX_API_KEY and review the automatic registration behavior before allowing first-use registration. <br>
Risk: Company contact lookups may expose sensitive personal or business contact data. <br>
Mitigation: Use contact lookup results only for legitimate, authorized business needs and avoid sharing them beyond approved workflows. <br>
Risk: Locally stored API keys may be exposed through filesystem access, backups, or shared machines. <br>
Mitigation: Protect ~/.zlbx/config.json with normal credential-handling controls and rotate the provider API key if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-data-platform) <br>
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun) <br>
- [Bidding search API reference](references/api-search.md) <br>
- [Company analysis API reference](references/api-company.md) <br>
- [Market analysis API reference](references/api-market.md) <br>
- [Automatic registration flow](references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown reports with API request summaries, structured findings, and occasional JSON snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote Zhiliaobiaoxun APIs, use ZLBX_API_KEY or ~/.zlbx/config.json, and create a local API key config during automatic registration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
