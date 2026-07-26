## Description: <br>
longbridge provides a LongPort OpenAPI CLI for stock quotes, account balances and positions, order management, and market data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[frankxiong](https://clawhub.ai/user/frankxiong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent run LongBridge CLI commands for market data, portfolio and account review, order lookup, and optional limit order submission or cancellation when trading is explicitly enabled. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent access to LongBridge brokerage credentials and account data can expose sensitive financial information. <br>
Mitigation: Install only when brokerage access is intended, use paper-trading or least-privilege credentials where possible, and avoid storing brokerage .env files in shared or untrusted project directories. <br>
Risk: Live buy, sell, or cancel commands can submit brokerage actions when trading is enabled, and buy or sell can bypass confirmation with --yes/-y. <br>
Mitigation: Keep LONGBRIDGE_TRADE_ENABLED unset or false by default, require human review for live trades, and avoid --yes/-y outside controlled paper-trading or audited workflows. <br>


## Reference(s): <br>
- [LongPort OpenAPI](https://open.longportapp.com/) <br>
- [ClawHub skill page](https://clawhub.ai/frankxiong/skills/longbridge-kit) <br>
- [Publisher profile](https://clawhub.ai/user/frankxiong) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, JSON, Configuration guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; command results may be text tables or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [All commands support --json for structured output; trading commands require LONGBRIDGE_TRADE_ENABLED=true.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter and server release metadata; pyproject.toml reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
