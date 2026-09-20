## Description:

Performs a local deterministic check of Chinese bank loan interest and repayment schedule tables, with each finding citing the source row.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill during month-end close, reconciliation, or inventory checks to re-calculate bank loan interest and repayment schedule rows, verify totals, and identify duplicates, blanks, placeholders, and negative values. The free release only performs the included local checks and reports insufficient input instead of making unsupported conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive finance data from bank loan schedules.

Mitigation: Provide only the exported table needed for the check and avoid including unrelated confidential records.

Risk: The free release omits several loan-review checks that are listed as outside the included tier.

Mitigation: Review the executed and withheld check lists in the output before relying on results, and use a fuller review process for contract, tax, LPR, or accounting-policy judgments.

Risk: Incomplete or malformed input can otherwise lead to false confidence.

Mitigation: Treat insufficient-input responses as no conclusion; add the missing headers or rows and rerun the check.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bank-loan-interest-check-free)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, JSON, analysis, shell commands, guidance]

**Output Format:** [Human-readable text or JSON containing executed checks, withheld checks, cited findings, and insufficiency guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; the reviewed artifact does not use network access or persistent storage.]

## Skill Version(s):

1.0.52 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
