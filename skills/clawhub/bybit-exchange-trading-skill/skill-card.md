## Description: <br>
Bybit AI Trading Skill helps agents trade on Bybit using natural language across spot, derivatives, earn, and other exchange workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[victorwu-bybit](https://clawhub.ai/user/victorwu-bybit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an AI assistant check Bybit markets, manage account data, and prepare or execute exchange actions after the required confirmations. It covers trading, earn products, bots, copy trading, fiat/P2P, OAuth authorization, and related Bybit workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can trade or manage real funds through Bybit API access. <br>
Mitigation: Prefer testnet or a dedicated capped subaccount, keep withdrawals disabled, and require explicit human confirmation before mainnet write operations. <br>
Risk: The skill handles API keys, OAuth tokens, and signing material. <br>
Mitigation: Store credentials in local environment variables or a self-hosted secret file when possible, mask displayed key material, and avoid pasting keys into hosted chat platforms. <br>
Risk: The skill includes self-update and module-loading behavior that can fetch remote instructions or code. <br>
Mitigation: Review or disable automatic updates and the OAuth helper before using the skill with real funds; rely on checksum and path validation for any enabled update flow. <br>


## Reference(s): <br>
- [Bybit AI Subaccount Help](https://www.bybit.com/en/help-center/article/Introduction-to-the-AI-Subaccount) <br>
- [Bybit API Management](https://www.bybit.com/app/user/api-management) <br>
- [Bybit TradFi Integration Docs](https://bybit-exchange.github.io/docs/v5/tradfi-integration) <br>
- [ClawHub Skill Page](https://clawhub.ai/victorwu-bybit/skills/bybit-exchange-trading-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown with inline shell commands, API request guidance, and structured confirmation cards] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Bybit API call plans, credential setup guidance, market/account summaries, and mainnet confirmation prompts before write operations.] <br>

## Skill Version(s): <br>
1.5.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
