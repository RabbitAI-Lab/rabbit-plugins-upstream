## Description: <br>
Verify agents, wallets, tokens, and EVM transactions before payment using free safety checks and paid ProofLayer trust scores through the Spraay x402 gateway. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to screen counterparties, wallets, tokens, and transactions before sending funds, choosing whether to pay directly, use escrow, or decline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The configured gateway controls all external API calls. <br>
Mitigation: Confirm SPRAAY_GATEWAY_URL points to the Spraay gateway or another gateway the user explicitly trusts before installation or use. <br>
Risk: The trust-score endpoint can trigger a small x402 payment. <br>
Mitigation: Review HTTP 402 payment details before retrying with proof, and reserve paid checks for agent counterparties or larger transactions. <br>
Risk: A favorable trust score reduces risk but does not guarantee a safe counterparty or transaction. <br>
Mitigation: Use trust scores as one signal alongside free safety screening, transaction decoding, and escrow for meaningful amounts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/plagtech/skills/spraay-trust) <br>
- [Spraay app](https://spraay.app) <br>
- [Spraay docs](https://docs.spraay.app) <br>
- [Spraay x402 gateway](https://gateway.spraay.app) <br>
- [ProofLayer](https://prooflayer.net) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls, text] <br>
**Output Format:** [Markdown with inline bash commands and plain-language recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include free endpoint calls and an optional x402 payment retry flow for the trust-score endpoint.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
