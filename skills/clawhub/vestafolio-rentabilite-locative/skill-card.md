## Description:

Compute gross and net rental yield and monthly cash-flow for a French buy-to-let investment from acquisition cost, rent and annual charges using Vestafolio's simulator API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to estimate gross yield, net yield, and average monthly cash-flow for a French rental-property investment before financing and tax effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Property and investment financial inputs are sent to a third-party Vestafolio API.

Mitigation: Tell users before transmitting values and avoid sending sensitive details unless they agree; offer the interactive simulator or a local calculation mode when preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-rentabilite-locative)
- [Vestafolio rentabilite locative API](https://www.vestafolio.com/api/tools/v1/rentabilite-locative)
- [Vestafolio interactive simulator](https://www.vestafolio.com/simulateurs/rentabilite-locative)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown text with API request examples and calculated rental-yield results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responds in French when the user writes in French; results should be grounded in the Vestafolio API response and should state that financing and rental-income taxation are excluded.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
