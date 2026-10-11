## Description:

Helps agents browse and purchase prepaid gift cards, check Snaplii Cash balances, pay bills, and send phone-number transfers through Snaplii.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapliiai](https://clawhub.ai/user/snapliiai)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can browse and buy gift cards, check their Snaplii Cash balance, pay bills, or transfer funds to another person's phone number.

### Deployment Geography for Use:

Canada and United States

## Known Risks and Mitigations:

Risk: Gift-card purchases and transfer creation can spend prepaid funds without a fresh confirmation for each transaction.

Mitigation: Set narrow API-key permissions and low spending and transfer limits in the Snaplii app; review the amount and recipient before acting.

Risk: A bill payment to the wrong biller or account may be irreversible.

Mitigation: Check the biller, account, and amount, and obtain explicit current-turn confirmation before payment.

Risk: API keys, phone numbers, gift-card codes, and PINs are sensitive.

Mitigation: Use secure credential entry for keys and avoid disclosing sensitive details unless the user requests them.

## Reference(s):

- [Snaplii skill release on ClawHub](https://clawhub.ai/snapliiai/skills/snaplii-a2m-payment)
- [Snaplii AI Payment](https://aipayment.snaplii.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown transaction summaries and redemption guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain sensitive payment details or gift-card redemption codes; disclose them only when requested.]

## Skill Version(s):

1.13.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
