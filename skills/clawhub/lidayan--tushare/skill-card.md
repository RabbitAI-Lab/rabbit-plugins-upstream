## Description: <br>
面向中文自然语言的 Tushare 数据研究技能。用于把“看看这只股票最近怎么样”“帮我查财报趋势”“最近哪个板块最强”“北向资金在买什么”“给我导出一份行情数据”这类请求，转成可执行的数据获取、清洗、对比、筛选、导出与简要分析流程。适用于 A 股、指数、ETF/基金、财务、估值、资金流、公告新闻、板块概念与宏观数据等研究场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lidayan](https://clawhub.ai/user/lidayan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn Chinese natural-language finance research requests into Tushare data retrieval, cleaning, comparison, screening, export, and concise analysis workflows for equities, indices, funds, financials, valuation, capital flow, disclosures, news, sectors, and macro data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Tushare token for market-data retrieval. <br>
Mitigation: Install only when the user is comfortable granting token-backed Tushare access, and keep the token in the TUSHARE_TOKEN environment variable rather than embedding it in generated code or outputs. <br>
Risk: Portfolio save and delete APIs are present in the referenced Tushare interface list without clear confirmation rules. <br>
Mitigation: Require explicit user confirmation before allowing any account portfolio save or delete operation. <br>
Risk: Generated exports and cache files can contain user-requested financial datasets. <br>
Mitigation: Create exports only as a user-directed action and report the file path, data scope, and any partial failures. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lidayan/skills/tushare) <br>
- [Tushare API interface reference](references/数据接口.md) <br>
- [Tushare registration](https://tushare.pro/register) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with tables, inline Python or shell commands when needed, and optional CSV, parquet, or PNG file paths for exported results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires access to Tushare data services for live retrieval; some interfaces may require account permissions or points.] <br>

## Skill Version(s): <br>
1.1.18 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
