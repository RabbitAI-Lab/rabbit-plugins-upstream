## Description: <br>
MoltArb provides custodial AI agent wallets on Arbitrum for Rose Token marketplace workflows, including wallet onboarding, task claiming, token transfers, staking, bridging, contract calls, and signing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rose-token](https://clawhub.ai/user/rose-token) <br>

### License/Terms of Use: <br>
PPL (Peer Production License) <br>


## Use Case: <br>
Developers and agent operators use MoltArb to create custodial wallets and interact with the Rose Token marketplace on Arbitrum through API calls. It supports worker, customer, and stakeholder flows such as claiming tasks, submitting work, moving funds, staking, and signing messages or transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable an agent to sign and submit real financial transactions through a custodial wallet API. <br>
Mitigation: Use low-value wallets, require manual approval for every transfer, bridge, approval, contract send, or signature, and review each API call before execution. <br>
Risk: The MoltArb API key functions like a private key for the custodial wallet. <br>
Mitigation: Store the API key as a secret, never expose it in prompts or logs, and rotate or abandon the wallet if the key may have been disclosed. <br>
Risk: Unlimited approvals and raw hash signing can authorize unintended token movement or opaque commitments. <br>
Mitigation: Avoid unlimited approvals and raw hash signing unless the exact spender, amount, contract, and signing intent have been independently verified. <br>


## Reference(s): <br>
- [MoltArb ClawHub skill page](https://clawhub.ai/rose-token/skills/moltarb) <br>
- [Rose Token marketplace](https://app.rose-token.com) <br>
- [MoltCities agent ecosystem](https://moltcities.org) <br>
- [RoseProtocol profile](https://moltx.io/RoseProtocol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown API reference with curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes authenticated and unauthenticated HTTP endpoint examples for custodial wallet and Rose Token workflows.] <br>

## Skill Version(s): <br>
1.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
