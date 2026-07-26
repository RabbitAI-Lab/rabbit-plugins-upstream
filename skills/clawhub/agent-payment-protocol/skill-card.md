## Description: <br>
Facilitates agent-to-agent payments in IRC channels by creating quotes, preparing Solana payment approvals, recording settlements, and maintaining local audit ledgers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vortitron](https://clawhub.ai/user/vortitron) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to coordinate quoted work between agents, approve Solana payments, record confirmed transactions, and review local payment history for IRC-based agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-driven Solana payment approval can move real funds if connected to a funded wallet. <br>
Mitigation: Use testnet or a small dedicated wallet, require explicit confirmation before every transfer, and verify the quote ID, recipient wallet, amount, and payment intent before settlement. <br>
Risk: Automated payments may exceed intended spend if safeguards are not configured. <br>
Mitigation: Set spending limits, allowlists, or other approval controls before enabling routine payment workflows. <br>
Risk: Local JSONL ledgers can contain financial history and chat-derived context. <br>
Mitigation: Store, review, and retain the ledgers according to the operator's data handling requirements. <br>


## Reference(s): <br>
- [Agent Payment Protocol on ClawHub](https://clawhub.ai/vortitron/skills/agent-payment-protocol) <br>
- [Publisher profile: vortitron](https://clawhub.ai/user/vortitron) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown documentation with JavaScript examples and CLI command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces quote, payment, history, and statistics objects; writes local JSONL ledgers for quotes and payments.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
