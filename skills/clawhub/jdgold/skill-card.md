## Description: <br>
京东黄金ToC智能助手提供实时金价查询、持仓收益与诊断、交易记录与条件单、黄金综合分析、行情资讯、大V排行和黄金模拟交易支持。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xuqingyuan0902-dot](https://clawhub.ai/user/xuqingyuan0902-dot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External JD Gold users can use this skill through an agent to query public gold prices and news, inspect their logged-in account holdings and income, review trade records and conditional orders, and use simulated gold trading workflows. The skill is intended for account assistance and market information, not as personalized financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access JD Gold account data and store financial login tokens locally. <br>
Mitigation: Install only in an environment where the user accepts that access, prefer OS-backed secure credential storage, and never expose authorization codes, tokens, session data, or sensitive authorization-link parameters in user-visible output. <br>
Risk: The skill includes upgrade behavior that can replace its own files. <br>
Mitigation: Review update notices, release hashes, and changed files before applying upgrades, especially in managed or shared environments. <br>
Risk: Persistent automated simulated trading and market-timing output may be mistaken for personalized financial advice or real-money trading. <br>
Mitigation: Keep simulated trading clearly framed as virtual practice, require explicit user confirmation before trade actions, and treat analysis as informational rather than financial advice. <br>


## Reference(s): <br>
- [Agent operations](references/agent-ops.md) <br>
- [Safety and response rules](references/iron-rules.md) <br>
- [OAuth integration](references/oauth-integration.md) <br>
- [Gold and precious-metals search](references/jdjr-gold-search.md) <br>
- [Gold advanced analysis search](references/jdjr-gold-analysis-search.md) <br>
- [News search](references/jdjr-news-search.md) <br>
- [Blogger trend search](references/jdjr-blogger-trend-search.md) <br>
- [Output templates](references/output-templates.md) <br>
- [Price unique-code enum](references/price-uniquecode-enum.md) <br>
- [Gold holdings diagnosis](references/黄金持仓诊断.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and plain text with structured market, account, news, and simulated-trading summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires login authorization for account-specific holdings, income, trade records, conditional orders, and automated simulated trading; public price and news queries can run without account login.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and artifact/version.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
