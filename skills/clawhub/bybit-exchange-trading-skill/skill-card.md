## Description:

Bybit AI Trading Skill - Trade on Bybit using natural language. Covers spot, derivatives, earn, and more. Works with Claude, ChatGPT, OpenClaw, and any AI assistant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[victorwu-bybit](https://clawhub.ai/user/victorwu-bybit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent guide or execute Bybit trading workflows, including account checks, market data lookup, spot and derivatives trading, Earn products, OAuth setup, and trading-bot operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle live Bybit trading credentials, move funds, store OAuth secrets, and place or change orders.

Mitigation: Use testnet or a capped sub-account, keep withdrawal permission disabled, prefer local environment variables over pasted secrets, and require a clear confirmation card before every mainnet action that affects funds, debt, Earn enrollment, copy trading, or orders.

Risk: The skill can update itself or load modules from remote sources before being used with live credentials.

Mitigation: Review self-update and module download behavior before deployment and verify checksums before accepting updated files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/victorwu-bybit/skills/bybit-exchange-trading-skill)
- [Bybit AI Subaccount Help Article](https://www.bybit.com/en/help-center/article/Introduction-to-the-AI-Subaccount)
- [Bybit API Management](https://www.bybit.com/app/user/api-management)
- [Bybit Mainnet API Endpoint](https://api.bybit.com)
- [Bybit Testnet API Endpoint](https://api-testnet.bybit.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with inline shell, code, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include trading confirmations, credential setup guidance, simulated examples when live calls are unavailable, and API request details.]

## Skill Version(s):

1.5.3 (source: server release metadata; artifact frontmatter reports 1.5.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
