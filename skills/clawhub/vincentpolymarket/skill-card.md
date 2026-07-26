## Description: <br>
Polymarket prediction market trading for agents to create wallets, browse markets, place bets, manage positions, and withdraw funds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glitch003](https://clawhub.ai/user/glitch003) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate a Vincent-backed Polymarket wallet: create or relink wallet access, inspect markets, place and manage bets, redeem resolved positions, and withdraw USDC.e under server-side policy controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent real-money trading and fund-movement authority, with weak default controls before the wallet is claimed. <br>
Mitigation: Claim the wallet before funding it, set strict spending limits, require approvals for sensitive transactions, and configure withdrawal controls. <br>
Risk: Trading and withdrawals can lose funds or send funds to the wrong destination. <br>
Mitigation: Use only funds the user can afford to lose, verify market token IDs and recipient addresses, and fund Polymarket wallets only with bridged USDC.e on Polygon. <br>
Risk: Using @vincentai/cli@latest can change command behavior between reviews. <br>
Mitigation: Prefer a pinned or reviewed CLI version for production use. <br>
Risk: Re-link tokens grant renewed API access if exposed before use. <br>
Mitigation: Avoid sharing re-link tokens in ordinary chat when possible, consume them promptly, and revoke or rotate credentials if exposure is suspected. <br>


## Reference(s): <br>
- [Vincent homepage](https://heyvincent.ai) <br>
- [ClawHub skill page](https://clawhub.ai/glitch003/skills/vincentpolymarket) <br>
- [Publisher profile](https://clawhub.ai/user/glitch003) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use @vincentai/cli and may create stored wallet API credentials under the declared agentwallet config paths.] <br>

## Skill Version(s): <br>
1.0.70 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
