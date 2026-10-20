## Description:

Helps agents browse and purchase prepaid gift cards, check Snaplii Cash balances, pay bills, and send money to other Snaplii users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapliiai](https://clawhub.ai/user/snapliiai)

### License/Terms of Use:

MIT-0

## Use Case:

Snaplii users can ask an agent to explore gift cards, check their prepaid balance, purchase cards, pay bills, or transfer funds to another user's phone number.

### Deployment Geography for Use:

United States and Canada

## Known Risks and Mitigations:

Risk: Gift-card purchases, bill payments, and transfers can spend real prepaid funds.

Mitigation: Use narrowly scoped API keys with a low daily spending limit, and review quotes, payees, recipients, and transfer details before proceeding.

Risk: Exposing an API key could allow unauthorized payments within its permissions and limits.

Mitigation: Enter the key only through the secure credential dialog, never in chat.

## Reference(s):

- [Snaplii AI Agent Cashback Payment on ClawHub](https://clawhub.ai/snapliiai/skills/snaplii-a2m-payment)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with transaction summaries and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include gift-card redemption details when requested.]

## Skill Version(s):

1.14.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
