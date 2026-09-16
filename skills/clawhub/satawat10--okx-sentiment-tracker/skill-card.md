## Description: <br>
Provides agent guidance for using the OKX CLI to retrieve crypto news, coin sentiment, social trend data, and macroeconomic calendar information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[satawat10](https://clawhub.ai/user/satawat10) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to map crypto market-news, sentiment, and macroeconomic-calendar requests to read-only OKX CLI commands and concise briefing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires live OKX API credentials, and some workflows may inspect positions, balances, leverage, or P&L for personalized trading guidance. <br>
Mitigation: Use read-only API key permissions, request explicit user intent before account-specific checks, and avoid trade execution or account-changing commands. <br>
Risk: Crypto sentiment and news outputs can be incomplete, sparse, or misleading if treated as trading advice. <br>
Mitigation: Present results as market intelligence, identify OKX versus web-search sources, and ask the user before producing personalized trading guidance. <br>


## Reference(s): <br>
- [Cross-Skill Workflows & MCP Tool Reference](artifact/references/workflows.md) <br>
- [OKX](https://www.okx.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/satawat10/skills/okx-sentiment-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OKX CLI credentials; web-search fallback may be used when OKX news data is sparse.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact metadata version is 1.4.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
