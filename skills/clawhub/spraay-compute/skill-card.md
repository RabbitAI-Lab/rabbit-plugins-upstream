## Description: <br>
Spraay Compute & Futures helps agents use Spraay's paid x402 gateway for GPU rental, model inference, and prepaid compute credits with USDC payments on Base or Solana. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when a user explicitly wants Spraay or x402-based paid compute for GPU jobs, model inference, or prepaid compute-futures workflows. The skill emphasizes cost estimation and human approval before paid operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid Spraay x402 calls and compute-futures deposits can spend real USDC from a funded wallet. <br>
Mitigation: Use a limited wallet, estimate costs before paid calls, and require explicit human confirmation before deposits or any operation that spends USDC. <br>
Risk: Compute-futures deposits lock funds and settled on-chain payments may not be reversible. <br>
Mitigation: Confirm the deposit amount and refund path with the user before depositing, and prefer free planning endpoints before committing funds. <br>
Risk: Requests sent to the gateway may contain user prompts, files, or other sensitive workload data. <br>
Mitigation: Send only data the user has approved for third-party processing and avoid including unnecessary secrets or private content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/plagtech/skills/spraay-compute) <br>
- [Spraay gateway](https://gateway.spraay.app) <br>
- [Spraay x402 discovery catalog](https://gateway.spraay.app/.well-known/x402.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP examples, shell commands, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should disclose expected USDC costs and approval requirements before paid calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
