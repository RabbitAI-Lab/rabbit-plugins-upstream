## Description: <br>
Safe agent-to-agent commerce via Spraay x402 escrow for creating, funding, monitoring, releasing, or canceling on-chain escrows after verified delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to coordinate escrowed USDC payments for agent-to-agent work, including milestone funding, status review, release after verified delivery, or cancellation when delivery fails. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create, fund, release, and cancel operations can affect real escrowed USDC. <br>
Mitigation: Require explicit user confirmation of the counterparty, amount, release conditions, and current escrow status before each fund-moving action. <br>
Risk: Released escrow funds cannot be recovered through this skill. <br>
Mitigation: Release funds only after the user confirms that delivery has been verified. <br>
Risk: Paid x402 endpoints charge USDC fees per API call. <br>
Mitigation: Confirm the user's intent to pay and use an x402-capable wallet before retrying paid requests with payment proof. <br>
Risk: Using an untrusted gateway URL could route escrow requests to the wrong service. <br>
Mitigation: Use the trusted SPRAAY_GATEWAY_URL expected by the release, and verify the endpoint before performing escrow actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/plagtech/skills/spraay-escrow) <br>
- [Spraay app](https://spraay.app) <br>
- [Spraay docs](https://docs.spraay.app) <br>
- [Spraay x402 gateway](https://gateway.spraay.app) <br>
- [Publisher GitHub profile](https://github.com/plagtech) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SPRAAY_GATEWAY_URL, curl, jq, and an x402-capable wallet for paid endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
