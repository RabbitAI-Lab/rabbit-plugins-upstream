## Description: <br>
Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, ETFs, indices, financial statements, announcements, research reports, news, macroeconomics, sectors, and related datasets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kenneth-bro](https://clawhub.ai/user/kenneth-bro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and investment researchers use this skill to retrieve structured Chinese market data for research, comparison, export, and downstream analysis. It is not intended for direct trading advice, automated order execution, or replacing independent review of financial decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API credentials may be exposed if placed directly in shell commands, logs, or shared terminal history. <br>
Mitigation: Use trusted local configuration or secret handling, avoid pasting API keys into reusable commands, and rotate credentials if they are exposed. <br>
Risk: The skill can send financial query text to an external InvestToday service through the CLI. <br>
Mitigation: Avoid submitting confidential portfolio, client, or account details unless the provider and data-handling terms are approved for that use. <br>
Risk: Using --skip-verify can bypass normal initialization checks. <br>
Mitigation: Reserve --skip-verify for controlled troubleshooting and prefer verified initialization for normal use. <br>
Risk: Returned analysis, trading signals, or reference data may be incomplete, stale, unreliable, or under-disclosed. <br>
Mitigation: Treat outputs as research data, verify important figures against official sources, and do not use the skill for direct buy/sell decisions or automated trading. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data) <br>
- [English skill instructions](artifact/SKILL_EN.md) <br>
- [English API reference index](artifact/docs/references-index.en.md) <br>
- [API reference index](artifact/docs/references-index.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured data summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May depend on Node.js 18+, the @investoday/investoday-api package, network access, API credentials, and endpoint-specific parameters.] <br>

## Skill Version(s): <br>
1.8.53 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
