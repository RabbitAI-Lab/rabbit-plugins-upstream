## Description:

Helps landlords and tenants assess US security deposit return deadlines, deductions, interest, refunds, and potential penalties, with cited rules and a draft itemized statement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tektolo](https://clawhub.ai/user/tektolo)

### License/Terms of Use:

MIT-0

## Use Case:

Landlords and property managers use this skill to assess deposit returns after move-out; tenants use it to check deadlines, deductions, and amounts owed. It also provides state and selected city deposit rules.

### Deployment Geography for Use:

United States (50 states and Washington, DC; selected city ordinances)

## Known Risks and Mitigations:

Risk: Deposit-settlement details are shared with Tektolo's external service.

Mitigation: Share only information needed for the calculation; omit names, addresses, and other unnecessary identifiers unless the user explicitly wants to provide them.

Risk: Missing dates or disputed deductions may make a refund or deadline assessment uncertain.

Mitigation: Ask for missing dates, relay assumptions and uncertainty, and present statutory penalties as exposure rather than a legal verdict.

## Reference(s):

- [Tektolo deposit settlement capability](https://tektolo.com/capabilities/deposit-settlement)
- [Tektolo capability catalog and schemas](https://tektolo.com/catalog.json)
- [ClawHub skill release](https://clawhub.ai/tektolo/skills/deposit-settlement)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summary and draft itemized statement]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites applicable rules; flags uncertain deductions, assumptions, and missing information. Not legal advice.]

## Skill Version(s):

1.0.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
