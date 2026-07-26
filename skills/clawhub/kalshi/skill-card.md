## Description: <br>
Read-only Kalshi prediction market integration for viewing markets, checking portfolio positions, analyzing prediction opportunities, and finding high-payoff/high-certainty trades. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[henrik-openclaw](https://clawhub.ai/user/henrik-openclaw) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and Kalshi users use this skill to inspect public market data, view authenticated portfolio information, and generate read-only opportunity analysis from Kalshi prediction markets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Portfolio commands require local Kalshi API credentials and can reveal balances, positions, orders, and trade history to the session. <br>
Mitigation: Protect files under ~/.kalshi, use the least-privileged key available, and run portfolio commands only in sessions where account data exposure is acceptable. <br>
Risk: Opportunity analysis is speculative and could be mistaken for financial advice. <br>
Mitigation: Treat opportunity output as informational, verify it independently, and apply the user's financial, legal, and compliance requirements before acting. <br>
Risk: The skill relies on local Python dependencies for market and portfolio access. <br>
Mitigation: Verify Python dependencies before installing and keep the runtime environment scoped to the intended Kalshi viewer use case. <br>


## Reference(s): <br>
- [Kalshi API Reference](references/api.md) <br>
- [Kalshi Trade API v2](https://api.elections.kalshi.com/trade-api/v2) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and read-only command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include authenticated portfolio data when credentials are configured; does not execute trades.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
