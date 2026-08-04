## Description: <br>
x402-client guides AI agents through handling HTTP 402 payment challenges, paying with supported wallets, retrying with a PAYMENT-SIGNATURE, and consuming pay-per-request APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marketingkioldenburg](https://clawhub.ai/user/marketingkioldenburg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to help agents consume x402-enabled pay-per-request APIs and reason through payment, retry, service discovery, and idempotency steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to make irreversible crypto payments or duplicate payments during automatic retries. <br>
Mitigation: Use a dedicated low-balance wallet, require explicit approval or strict spending limits, and inspect payment state before retrying any failed payment call. <br>
Risk: Untrusted or incorrect service manifests and payment requirements can cause funds to be sent to the wrong recipient or for the wrong amount. <br>
Mitigation: Use trusted service manifests and verify the network, asset, amount, payTo address, timeout, and refund or dispute terms before signing. <br>


## Reference(s): <br>
- [x402 homepage](https://www.x402.org) <br>
- [ClawHub skill page](https://clawhub.ai/marketingkioldenburg/skills/x402-client) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides payment-flow guidance for HTTP 402 responses, including retry, manifest discovery, and idempotency considerations.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
