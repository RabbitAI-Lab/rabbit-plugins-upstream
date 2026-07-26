## Description: <br>
Use this skill to safely create a wallet the agent can use for transfers, swaps, and any EVM chain transaction, with support for raw signing and Polymarket betting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glitch003](https://clawhub.ai/user/glitch003) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent operators use this skill to create and manage agent-controlled wallets for token transfers, swaps, EVM contract calls, raw signatures, and Polymarket trading within owner-defined policies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent-operated wallet can control funds, signatures, and betting actions. <br>
Mitigation: Fund only intentionally, claim the wallet before use, and set strict address, token, function, spending-limit, and manual-approval policies. <br>
Risk: API keys and re-link tokens can grant wallet control. <br>
Mitigation: Treat API keys and re-link tokens as wallet-control secrets, avoid shared workspaces, and rotate or recover access through the documented owner flow when needed. <br>
Risk: Raw signing and arbitrary contract calls can create irreversible or hard-to-review consequences. <br>
Mitigation: Use raw signing and arbitrary calldata only when a human can independently review the exact payload, target, and financial impact. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/glitch003/skills/vincent) <br>
- [Vincent API](https://heyvincent.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl examples and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces API request patterns and operational guidance; actual wallet actions require external API calls and bearer-token credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
