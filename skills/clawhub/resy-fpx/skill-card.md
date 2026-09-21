## Description:

Query and act on Resy restaurant reservations from a shell by using curl against api.resy.com, with fpx only for one-time token bootstrap when Resy email and password credentials are not available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and advanced users use this skill to search Resy venues, inspect availability, manage favorites and Priority Notify, and create or cancel reservations through shell commands. It is best suited for workflows where an agent proposes or executes Resy API calls for the user's own account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may book or cancel real reservations, change favorites or notify subscriptions, or expose account and payment-related data.

Mitigation: Use the skill only with the user's own Resy account, keep RESY_PASSWORD and RESY_TOKEN private, prefer read-only commands, and require explicit confirmation of venue, date, time, party size, operation, and payment method before any mutating command.

## Reference(s):

- [Resy API ready-to-run requests](references/resy-api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that read account data or mutate live Resy reservations, favorites, and notify subscriptions.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
