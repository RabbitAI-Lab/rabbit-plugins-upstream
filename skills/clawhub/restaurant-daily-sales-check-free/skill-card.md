## Description:

Checks restaurant daily sales report tables for row-level arithmetic, total reconciliation, duplicate rows, blanks, and negative amounts, with each finding tied to source evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Restaurant finance, cashier, and operations staff use this skill to check daily sales report submissions before closing, reconciliation, or month-end review. It helps identify arithmetic mismatches, total-row issues, duplicate store-day rows, missing placeholders, and negative values within the free-version scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may rely on the free version for checks it does not perform, including platform-fee arithmetic and other withheld checks.

Mitigation: Review the executed and withheld checks in the output, and verify any out-of-scope sales, fee, tax, or timing questions separately before acting.

Risk: The skill and its outputs are primarily Chinese-language, which can lead to misunderstanding if reviewers are not comfortable with the language or restaurant-report terminology.

Mitigation: Use reviewers who can read the report language and confirm that source table columns match the expected restaurant daily sales report fields.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/restaurant-daily-sales-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or structured JSON containing executed checks, withheld checks, findings, summary, and cited line-level evidence.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; accepts a JSON file or pasted table text containing the restaurant daily sales report.]

## Skill Version(s):

1.0.43 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
