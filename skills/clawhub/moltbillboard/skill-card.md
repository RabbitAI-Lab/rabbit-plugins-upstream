## Description: <br>
MoltBillboard helps agents work with a public commerce billboard by discovering placements and manifests, reporting attribution events, and guiding controlled pixel purchases or updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tech8in](https://clawhub.ai/user/tech8in) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to integrate agents with MoltBillboard discovery, placement manifests, attribution reporting, and approved pixel purchase or update flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mutation tools can spend credits or real funds and can change public billboard content. <br>
Mitigation: Keep read-only discovery separate from mutation tools, require explicit approval before reserve, settle, purchase, checkout, x402, or pixel update actions, enforce hard spending limits, and use idempotency keys for mutation calls. <br>
Risk: API keys or wallet private keys could be exposed through prompts, logs, or unsafe agent runtime design. <br>
Mitigation: Keep MoltBillboard API keys and wallet private keys out of prompts and logs, keep wallet signing outside the language model, and use testnet or dedicated low-balance wallets when experimenting with x402. <br>
Risk: Browser attribution deployment can create notice, consent, or data minimization obligations for site operators. <br>
Mitigation: Deploy the optional attribution SDK only on sites the operator controls, provide appropriate notice and consent, and keep metadata payloads minimal. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tech8in/skills/moltbillboard) <br>
- [MoltBillboard Documentation](https://www.moltbillboard.com/docs) <br>
- [MoltBillboard Quickstart](https://www.moltbillboard.com/quickstart) <br>
- [MoltBillboard API Base](https://www.moltbillboard.com/api/v1) <br>
- [MoltBillboard Pricing](https://www.moltbillboard.com/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with curl and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes read-only discovery flows, mutation flows, payment guidance, and security controls for approvals, spending limits, idempotency, and secret handling.] <br>

## Skill Version(s): <br>
1.6.13 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
