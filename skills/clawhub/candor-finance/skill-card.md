## Description:

Helps users organize financial records, review spending and investments, track approved budgets and goals, and follow up on potential savings using their Candor workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

People managing their personal finances use this skill to inspect account and transaction evidence, evaluate financial decisions, and maintain approved plans and follow-up in Candor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated access can expose and change sensitive financial records and persist notes, rules, budgets, goals, or imports.

Mitigation: Limit requests to the intended scope, authorize changes deliberately, and review the resulting records.

Risk: Broad reviews may save raw transaction pages locally without clear retention or deletion controls.

Mitigation: Check where raw pages are stored and how they are deleted before running a broad review.

Risk: Scheduled checks can continue accessing financial information after the initial request.

Mitigation: Schedule only user-requested checks; confirm their scope, frequency, and stop condition.

## Reference(s):

- [Candor setup and access](https://candor.money/START.md)
- [Candor Finance skill listing](https://clawhub.ai/candor/skills/candor-finance)
- [Evidence handling](references/evidence.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May make authorized changes to the financial workspace and set user-requested scheduled checks.]

## Skill Version(s):

0.1.152 (source: ClawHub release; skill frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
