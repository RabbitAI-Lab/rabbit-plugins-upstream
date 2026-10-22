## Description:

Records user-described one-off entries in a local Beancount ledger, proposing them for approval before writing and checking the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

People maintaining a local Beancount ledger use this skill to record purchases, income, transfers, and other one-off directives from natural-language requests or receipt text. It proposes entries for confirmation and validates the ledger after writing.

### Deployment Geography for Use:

Global; intended for use with a locally accessible Beancount ledger.

## Known Risks and Mitigations:

Risk: An interruption during account opening can leave the approved account without its required first transaction and leave the ledger with validation errors.

Mitigation: Prefer validating and writing the account opening and first transaction together, or stop when strict validation fails. Keep a ledger backup and inspect the exact proposed entries and destination before writing.

## Reference(s):

- [ClawHub release](https://clawhub.ai/puncsky/skills/beancount-add)
- [Project skill index](https://github.com/bex-co/beancount-io/tree/main/skills)

## Skill Output:

**Output Type(s):** [Beancount directives, Text, Shell commands]

**Output Format:** [Proposed Beancount entries with brief explanations, followed by verified ledger changes after approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Appends approved entries to an included local ledger file; does not edit existing entries.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
