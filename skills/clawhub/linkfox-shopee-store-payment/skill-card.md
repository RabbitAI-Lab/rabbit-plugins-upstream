## Description:

Helps agents work with authorized Shopee store payment workflows, including escrow, payouts, wallet transactions, installments, and income reports through LinkFox-provided scripts and API references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers managing authorized Shopee stores use this skill to query payment settlement, escrow, payout, wallet, installment, billing, and income-report information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive Shopee payment, account, credential, and billing data through LinkFox services.

Mitigation: Use it only when comfortable sending that data through LinkFox, and treat API keys, phone codes, and payment data as secrets.

Risk: The skill can run set_* installment operations that may change store or item installment status.

Mitigation: Explicitly confirm the intended store, item, and status before running any set_* operation.

Risk: Saved response files may retain financial or account data after the task is complete.

Mitigation: Delete saved linkfox response files when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-payment)
- [Shopee Payment API index](https://open.shopee.com/documents/v2/v2.payment.get_escrow_detail?module=97&type=1)
- [Payment module API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Payment endpoint references](references/apis/)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON files and stdout JSON or summaries, with Markdown guidance for setup and troubleshooting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a linkfox session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
