## Description: <br>
Wallets for AI agents with x402 payment signing, referral rewards, and policy-controlled actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[microchipgnu](https://clawhub.ai/user/microchipgnu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to connect AI agents to server-side wallets, call x402 APIs, check balances and activity, and perform policy-controlled wallet actions such as transfers, contract calls, and message signing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can spend funds or authorize paid x402 calls through server-side wallet authority. <br>
Mitigation: Set strict spending policies and require dryRun plus explicit approval before paid calls, transfers, contract calls, or signing actions. <br>
Risk: The local configuration stores an API token that grants wallet access. <br>
Mitigation: Protect ~/.agentwallet/config.json, restrict file permissions, avoid committing it, and rotate the token if exposure is suspected. <br>
Risk: Heartbeat instructions can fetch and replace skill files from a remote website without integrity checks. <br>
Mitigation: Avoid self-update commands unless the fetched files are independently reviewed and verified before use. <br>
Risk: Broad wallet-related activation triggers may cause the skill to run in more situations than intended. <br>
Mitigation: Narrow activation triggers where possible and review wallet actions before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/microchipgnu/skills/agentwallet-frames) <br>
- [AgentWallet homepage](https://frames.ag) <br>
- [AgentWallet skill instructions](https://frames.ag/skill.md) <br>
- [AgentWallet heartbeat instructions](https://frames.ag/heartbeat.md) <br>
- [AgentWallet skill metadata](https://frames.ag/skill.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl commands, JSON request and response examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes authenticated wallet API calls, policy settings, x402 payment options, and heartbeat status messages.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
