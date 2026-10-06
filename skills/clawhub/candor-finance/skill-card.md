## Description:

Helps Candor-connected agents organize personal finances, review spending and investments, track approved plans, and preserve evidence and follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

People using a Candor-connected agent can review their accounts and transactions, investigate savings opportunities, plan budgets and goals, and maintain authorized financial follow-up. An authenticated Candor workspace and an active subscription are required for service access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses sensitive account and transaction history and may retain financial notes and follow-ups.

Mitigation: Install only for an intended Candor-connected financial workspace; limit access to the user's authorized tasks and review saved context.

Risk: Internal record changes can misstate approved financial decisions if made without authority or verification.

Mitigation: Require user authorization for changes, inspect their effective result, and preserve a way to undo them.

Risk: Financial guidance could be mistaken for authorization to make external payments, trades, filings, elections, cancellations, or messages.

Mitigation: Keep separate user control over these real-world actions and request appropriate authority before taking them.

## Reference(s):

- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Candor getting started](https://candor.money/START.md)
- [Candor setup](artifact/references/setup.md)
- [Candor evidence handling](artifact/references/evidence.md)
- [Candor monitoring](artifact/references/monitoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Financial guidance]

**Output Format:** [Markdown with supported amounts, dates, uncertainties, and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create authorized notes, follow-ups, and reversible internal record changes in the user's financial workspace.]

## Skill Version(s):

0.1.162 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
