## Description:

GET https://delvorn.site/api/x402/test-asset, HTTP 402, 1 USDC on Base, public receipt. No API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mranderson323](https://clawhub.ai/user/mranderson323)

### License/Terms of Use:

MIT-0

## Use Case:

External agents use this skill to complete a Delvorn x402 test-asset receipt workflow: request the asset endpoint, handle the 402 payment challenge for 1 USDC on Base, retry with a payment signature, and check public receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes an undeclared script that reads a local Telegraph access token and edits a remote public page.

Mitigation: Review before installing; require the publisher to remove or clearly document that script and its credential use, and do not run it unless remote page editing is intended.

Risk: The skill asks an agent to complete a live payment flow for 1 USDC on Base.

Mitigation: Use only an independent wallet, verify the endpoint, network, amount, and recipient before signing, and confirm the resulting public receipt.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mranderson323/skills/delvorn-register)
- [Delvorn Public Receipt Writeup](https://telegra.ph/Delvorn-register-1-test-public-receipt-08-26)
- [Delvorn x402 Discovery](https://delvorn.site/.well-known/x402)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls]

**Output Format:** [Markdown with HTTP request and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl; instructs agents to use independent wallets and verify public receipts.]

## Skill Version(s):

1.0.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
