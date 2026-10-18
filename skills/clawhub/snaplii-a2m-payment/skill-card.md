## Description:

Helps agents browse and buy gift cards with prepaid Snaplii Cash, check balances, pay bills, and transfer funds to another person's phone number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapliiai](https://clawhub.ai/user/snapliiai)

### License/Terms of Use:

MIT-0

## Use Case:

Snaplii users and their agents browse and purchase gift cards, review balances and owned cards, pay bills, and send prepaid funds to a confirmed phone number.

### Deployment Geography for Use:

Canada and the United States (account-specific catalog and currency)

## Known Risks and Mitigations:

Risk: Important authentication instructions are hidden in an HTML comment and may be missed during review.

Mitigation: Review the hidden Auth block before installing or using the skill.

Risk: Reusable API keys can authorize payments and transfers if exposed or granted excessive permissions.

Mitigation: Use the narrowest necessary permissions and daily limits, enter keys only through secure credential input, and revoke them in the Snaplii app when no longer needed.

Risk: Bill payments cannot be reversed, and uncertain payment outcomes can lead to duplicate charges if retried.

Mitigation: Confirm biller and account details before paying; check the payment outcome before any retry.

## Reference(s):

- [Snaplii skill listing](https://clawhub.ai/snapliiai/skills/snaplii-a2m-payment)
- [Snaplii app for iOS](https://apps.apple.com/app/snaplii/id1596924498)
- [Snaplii app for Android](https://play.google.com/store/apps/details?id=com.snaplii.app)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text and Markdown with payment summaries and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include gift-card quotes, balance and transaction status, masked card details, and redemption instructions.]

## Skill Version(s):

1.14.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
