## Description: <br>
Polymarket prediction market CLI - Browse markets, check prices, execute trades, and manage portfolio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aplanckfish](https://clawhub.ai/user/aplanckfish) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to browse Polymarket prediction markets, inspect prices and portfolio balances, and place buy or sell orders from an agent-accessible CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit real Polymarket trades with wallet credentials and does not require an explicit confirmation step before posting an order. <br>
Mitigation: Install only when live trading is intended, use a dedicated limited-funds wallet, and require explicit operator confirmation before invoking buy or sell commands. <br>
Risk: Wallet private keys and derived API credentials are available to the local agent environment or credential files. <br>
Mitigation: Protect credential files with restrictive permissions, avoid sharing the agent environment, and rotate credentials if the workspace or host is exposed. <br>
Risk: Broad natural-language triggers for trading phrases could cause unintended order placement. <br>
Mitigation: Avoid automatic invocation for trading phrases and route trade requests through a review or allowlist policy. <br>
Risk: Dependency ranges are not pinned, which can change trading behavior after installation. <br>
Mitigation: Pin and review dependency versions before deployment. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/aplanckfish/skills/polymarket-autotrade) <br>
- [Polymarket events API](https://gamma-api.polymarket.com/events/pagination) <br>
- [Polymarket positions API](https://data-api.polymarket.com/positions) <br>
- [Polymarket CLOB API](https://clob.polymarket.com) <br>
- [Polygon RPC](https://polygon-rpc.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, API calls] <br>
**Output Format:** [Plain text CLI output with configuration examples and command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May perform network API requests and submit live Polymarket orders when wallet credentials are configured.] <br>

## Skill Version(s): <br>
1.2.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
