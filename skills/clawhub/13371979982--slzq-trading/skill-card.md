## Description:

三立期货「三立智期」官方技能：对话领取模拟盘密钥，查行情、持仓、资讯与龙虎榜；模拟盘可下单；实盘可设条件单与止盈止损（服务端托管，不用盯盘）。问是否正规、开户也可答。实盘请去 App 复制密钥。

This skill is ready for commercial/non-commercial use.

## Publisher:

[13371979982](https://clawhub.ai/user/13371979982)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to the 三立智期 futures workflow for market data, account and position review, simulated trading, and user-authorized live conditional orders. It also guides setup of the bundled MCP runtime and explains broker/account questions using the packaged reference material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A live-enabled key can access account data and submit, modify, or cancel real futures orders.

Mitigation: Keep the trading environment set to sim unless the user intentionally chooses live trading, and require explicit user confirmation before live order actions.

Risk: Saved API keys can expose trading access if local credential files or client configuration are shared.

Mitigation: Protect saved credential files, avoid logging or repeating full keys, and rotate or revoke keys if exposure is suspected.

Risk: Broker and account trust decisions may rely too heavily on package-provided claims.

Mitigation: Independently verify the broker through official regulatory or industry channels before using live trading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/13371979982/skills/slzq-trading)
- [Publisher profile](https://clawhub.ai/user/13371979982)
- [Usage notes](references/usage-notes.md)
- [Company FAQ](references/company-faq.md)
- [Open API index](references/api.md)
- [OpenAPI specification](references/openapi.yaml)
- [MCP runtime README](runtime/mcp/README.md)
- [Default API domain](https://slzqapi.sxslqhsh.com)
- [Sanli official website](https://www.sxslqh.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown and structured tool or API call guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May configure or call a local MCP runtime and may create or use saved trading API credentials.]

## Skill Version(s):

1.5.2 (source: server release, SKILL.md frontmatter, VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
