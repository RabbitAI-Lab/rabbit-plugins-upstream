## Description:

建筑工人工资专户发放核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External construction payroll and project finance users can run this skill before monthly wage disbursement to check a construction worker wage special-account table for arithmetic mismatches, total-row inconsistencies, duplicate rows, missing placeholders, and negative input values. It supports local review of table consistency but does not determine lawful wages, deduction legality, local minimum-wage rules, or withheld paid-version checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags an embedded paid upgrade and install flow that uses an unpinned runtime package and repeated purchase prompts.

Mitigation: Use the free local checker without running the paid upgrade flow unless the package, version, publisher, and payment steps have been independently verified.

Risk: The free version does not perform payout-total reconciliation even though artifact text may imply broader reconciliation.

Mitigation: Treat payout-total reconciliation and other withheld checks as not performed by this release; verify them separately before relying on disbursement decisions.

Risk: The skill checks table consistency and does not decide lawful wages, deduction legality, or local minimum-wage compliance.

Mitigation: Use qualified payroll, legal, or project-labor review for wage entitlement, deduction, and regional labor-law questions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/construction-wage-special-account-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON findings, with cited source rows and runnable Node.js command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; returns insufficient-input status instead of a conclusion when required table evidence is missing.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
