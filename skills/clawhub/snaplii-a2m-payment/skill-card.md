## Description:

Helps agents browse and buy gift cards, manage Snaplii Cash, pay bills, and transfer funds using a pre-funded balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapliiai](https://clawhub.ai/user/snapliiai)

### License/Terms of Use:

MIT-0

## Use Case:

Snaplii customers use this skill with an agent to browse and purchase gift cards, check their balance, pay bills, and send Snaplii Cash to a phone number.

### Deployment Geography for Use:

United States and Canada (according to the account's country)

## Known Risks and Mitigations:

Risk: Gift-card purchases can spend prepaid Snaplii Cash without a separate per-transaction confirmation.

Mitigation: Use narrowly scoped API-key permissions and low daily spending limits; review the quoted cost before buying and revoke the key when no longer needed.

Risk: Creating a transfer can schedule funds to be sent after its cancellation window without a separate confirmation.

Mitigation: Set a low transfer limit, check the recipient and amount, and disclose the cancellation deadline promptly.

## Reference(s):

- [Snaplii skill on ClawHub](https://clawhub.ai/snapliiai/skills/snaplii-a2m-payment)
- [Snaplii app for iOS](https://apps.apple.com/app/snaplii/id1596924498)
- [Snaplii app for Android](https://play.google.com/store/apps/details?id=com.snaplii.app)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown and plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes purchase quotes, transaction status, and gift-card redemption details when requested.]

## Skill Version(s):

1.12.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
