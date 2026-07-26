## Description: <br>
Manage AIUSD trading, staking, withdrawals, balance checks, gas top-ups, and transaction history via authenticated backend calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaunceyliu](https://clawhub.ai/user/chaunceyliu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an OpenClaw or ClawdBot assistant check balances, manage accounts, and place AIUSD trading, staking, withdrawal, gas top-up, and transaction-history requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate high-impact financial actions such as trades, withdrawals, staking, and gas top-ups. <br>
Mitigation: Require explicit user confirmation for every trade, withdrawal, staking action, gas top-up, and credential-cache deletion; use a wallet or account with limited funds and permissions. <br>
Risk: Installer files extract an embedded package and run npm install. <br>
Mitigation: Install only if the publisher is trusted, inspect the embedded package and package.json before use, and avoid running npm install scripts blindly. <br>
Risk: Re-authentication behavior can clear local credential caches. <br>
Mitigation: Confirm re-authentication and cache deletion before running it, and verify the intended wallet or account is active afterward. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chaunceyliu/skills/trade-with-aiusd) <br>
- [AIUSD Official Website](https://aiusd.ai) <br>
- [AIUSD Agent Reference](artifact/SKILL.md) <br>
- [AIUSD Skill README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and tool-use guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires authentication and live tool schema discovery before account actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact build metadata reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
