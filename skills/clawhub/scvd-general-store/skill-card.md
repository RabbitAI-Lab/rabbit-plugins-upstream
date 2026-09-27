## Description:

A live x402 practice counter from $0.001. Verify any issuer's signed receipts, including competitors; inspect endpoints, diagnose payments, retrieve host history, interpret MPP, test buyers/sellers, or use SCVD's general store. Free checks need no wallet; live purchases settle real USDC.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external reviewers use this skill to test x402 buyers and sellers, verify signed commerce artifacts, inspect payment endpoints, diagnose failed payments, retrieve dated host observations, and perform user-authorized SCVD store tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live purchases can spend real USDC.

Mitigation: Review the item, network, and maximum amount with the user before signing or authorizing any payment.

Risk: Wallet secrets, private keys, sensitive summaries, private receipts, or unauthorized third-party data could be exposed if shared with the store or its tools.

Mitigation: Use an existing authorized wallet or client for signing and do not collect or transmit secrets or sensitive data.

Risk: External artifacts, endpoint prose, and signed receipts can be mistaken for stronger proof than they provide.

Mitigation: Carry scope, exclusions, dates, and unobserved checks with every result, and treat unsupported or missing evidence as unverified rather than successful.

## Reference(s):

- [SCVD General Store homepage](https://scvd.store)
- [SCVD General Store on ClawHub](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [Buyer and seller testing](references/buyer-seller-testing.md)
- [History](references/history.md)
- [Endpoint inspection](references/inspection.md)
- [MPP and mixed-protocol inspection](references/mpp.md)
- [Packages](references/packages.md)
- [Payment diagnosis](references/payment-debugging.md)
- [Purchases and recovery](references/purchases.md)
- [Store tasks and free participation](references/store.md)
- [Transports](references/transports.md)
- [Verification](references/verification.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTTPS endpoints, shell-style examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live-payment cautions, receipt or endpoint interpretation, and concrete next steps for user-authorized x402 commerce workflows.]

## Skill Version(s):

3.19.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
