## Description:

Record buying, holding, and selling a home or rental property in a local Beancount ledger through bea, with entries proposed first and written only after confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Help users record a property purchase, mortgage payments, rental activity, or sale in an existing Beancount ledger, using the figures they provide and presenting a proposal for approval before writing entries.

### Deployment Geography for Use:

Global; no geographic restrictions are identified in the available evidence.

## Known Risks and Mitigations:

Risk: The skill's hosted-ledger fallback conflicts with its stated local-ledger scope and could lead to access to a connected online ledger.

Mitigation: Before installation, remove the hosted-ledger fallback or require separate approval naming the online service, ledger, and allowed operations. Review each proposed entry and destination, and keep a ledger backup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/puncsky/skills/beancount-property)
- [Project skills directory](https://github.com/bex-co/beancount-io/tree/main/skills)

## Skill Output:

**Output Type(s):** [text, code, guidance]

**Output Format:** [Proposed Beancount directives and transactions, with explanatory text.]

**Output Parameters:** [Property-event details supplied by the user, including dates, amounts, currencies, accounts, and transaction descriptions.]

**Other Properties Related to Output:** [Proposals are reviewed before any ledger write; approved entries are checked against the ledger.]

## Skill Version(s):

1.0.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
