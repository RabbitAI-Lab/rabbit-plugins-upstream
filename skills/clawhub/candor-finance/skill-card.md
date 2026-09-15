## Description:

Use Candor for personal finance tasks that touch money, financial records, prior decisions, or approved plans by organizing accounts and spending, remembering budgets and goals, reviewing investments, investigating savings, and keeping evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an authenticated Candor workspace use this skill to investigate personal finance questions, organize financial records, compare options, and make authorized internal updates while keeping evidence and follow-up linked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses authenticated Candor CLI access to a financial workspace.

Mitigation: Install only in a trusted agent environment connected to the intended Candor account, and review financial answers against scoped workspace evidence.

Risk: The skill can make bounded internal updates to financial records or approved state when authorized.

Mitigation: Require clear user authority for changes, keep updates reversible where possible, and verify the effective result before reporting completion.

Risk: Raw financial response files may exist locally during review without guaranteed protection or cleanup.

Mitigation: Use secure temporary-file handling and cleanup controls, and avoid retaining raw financial pages beyond the task need.

## Reference(s):

- [Candor start guide](https://candor.money/START.md)
- [Setup and access](references/setup.md)
- [Evidence handling](references/evidence.md)
- [Continuity](references/continuity.md)
- [Monitoring](references/monitoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and plain text with Candor CLI command recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded internal financial record updates when authorized by the user.]

## Skill Version(s):

0.1.112 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
