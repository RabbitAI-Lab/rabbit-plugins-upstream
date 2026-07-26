## Description: <br>
查询场外指数基金和 ETF 联接基金的基础信息、规模费率、风险等级、基金经理、持仓、分红、区间收益、跟踪误差，并支持关键词筛选和批量比较。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[e-fintech](https://clawhub.ai/user/e-fintech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer Chinese natural-language questions about off-exchange index funds and ETF feeder funds with factual fund data, comparisons, and risk context. It is intended for information lookup and comparison, not investment advice or account operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can save the API key persistently in plaintext shell profile and local configuration files. <br>
Mitigation: Use a low-privilege key where possible, review or edit the installer before use, and remove saved ETF_API_KEY and fallback-key entries when they are no longer needed. <br>
Risk: The installer replaces the installed open-fund-query skill directory. <br>
Mitigation: Back up any existing open-fund-query installation or install to a separate skills directory before running the installer. <br>
Risk: Fund information and comparisons could be mistaken for investment advice if the answer omits boundaries. <br>
Mitigation: Keep outputs factual, include data dates or report periods, avoid buy or sell recommendations, and preserve the required user-facing disclaimer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/e-fintech/skills/open-fund-query) <br>
- [场外指数基金信息查询 — 接口字段权威参考](references/catalog-oef.md) <br>
- [Index Hub API service](https://www.etf.com.cn/api/etf-api-service) <br>
- [AI Skills access documentation](https://cdn.efunds.com.cn/eda/h5/itcenter/pd/ai-skills-doc/readme.pdf) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Chinese Markdown answer with concise conclusions, data tables or lists, data dates, and risk disclosure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires API authorization; final answers should omit credentials, raw responses, and internal implementation details.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
