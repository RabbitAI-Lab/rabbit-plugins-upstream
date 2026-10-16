## Description:

Helps users purchase targeted business leads or prepaid prospect follow-up from Alpha Ceema using USDC on Base, with explicit consent before payment or sharing order details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alphaceema](https://clawhub.ai/user/alphaceema)

### License/Terms of Use:

MIT-0

## Use Case:

External users who explicitly request a lead pack or weekly prospect follow-up use this skill to authorize payment and send their business details and target-customer criteria to Alpha Ceema for fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may spend USDC using an x402-capable wallet.

Mitigation: Require explicit purchase confirmation and verify the service price, Base network, USDC asset, and approved destination before signing.

Risk: The order shares business contact details and target-customer criteria with the provider.

Mitigation: Present the privacy notice, obtain explicit data-transmission consent, and send the request only to leads@alphaceema.com after successful payment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/alphaceema/skills/leads)
- [Alpha Ceema website](https://alphaceema.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown purchase confirmation or an email draft when the agent cannot send email]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes the service, payment proof, fulfillment recipient, and next steps.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
