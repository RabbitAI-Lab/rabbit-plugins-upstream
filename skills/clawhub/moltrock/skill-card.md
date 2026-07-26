## Description: <br>
MoltRock provides command-line agent workflows for contributing USDC to a planned Base vault, checking portfolio and progress data, distinguishing vault shares from a pump.fun hype token, and generating anti-scam or promotional text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sloof13](https://clawhub.ai/user/sloof13) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External agent operators use this skill to interact with MoltRock-related vault, portfolio, progress, verification, and promotional commands. The skill is most relevant to agents evaluating or coordinating on-chain crypto participation and should be used with explicit human review before any movement of funds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can encourage USDC deposits or cross-chain asset movement before the vault address and transaction safety checks are clearly established. <br>
Mitigation: Require explicit human confirmation for any asset movement and independently verify the deployed vault contract, backend API, fees, risks, and exact transaction details before use. <br>
Risk: The skill promotes a pump.fun token that is separate from vault ownership and may be confused with real MROCK vault shares. <br>
Mitigation: Use the skill's token distinction and verification commands, and independently confirm the official pump.fun mint before any promotion or trading activity. <br>


## Reference(s): <br>
- [MoltRock ClawHub skill page](https://clawhub.ai/sloof13/skills/moltrock) <br>
- [Official pump.fun MROCK hype token page](https://pump.fun/coin/7GWc8fiF7jYkigboNCoHuZPwAhk7zqmht2EWFDCipump) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API calls, guidance] <br>
**Output Format:** [Plain text and JSON-like command output from shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Some commands call a configurable MoltRock API endpoint and may require curl or jq for full output formatting.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
