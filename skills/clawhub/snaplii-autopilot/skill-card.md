## Description:

Helps an agent buy a Snaplii gift card, redeem it through a merchant website, and complete the user's order with browser automation and final approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapliiai](https://clawhub.ai/user/snapliiai)

### License/Terms of Use:

MIT-0

## Use Case:

People asking an agent to purchase a gift card with their Snaplii balance and use it to complete a merchant or delivery order, subject to checkout confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A gift-card purchase charges the user's prepaid balance before the merchant order is placed.

Mitigation: Use a spending-limited API key, review the quote before purchase, and check the gift-card list rather than retrying an uncertain purchase.

Risk: Browser checkout could place an incorrect order or use an unintended delivery address.

Mitigation: Confirm the delivery address and review items, tip, and total with the user; require explicit approval before the final order action.

Risk: API credentials and redemption codes could be exposed.

Mitigation: Enter the API key only through secure credential entry and avoid disclosing redemption codes in chat unless requested.

## Reference(s):

- [Snaplii Autopilot on ClawHub](https://clawhub.ai/snapliiai/skills/snaplii-autopilot)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quote and order summary before checkout; order confirmation or manual redemption steps when applicable.]

## Skill Version(s):

1.6.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
