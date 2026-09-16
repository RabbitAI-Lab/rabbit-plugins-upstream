## Description:

A free local checker that reviews overdue-interest worksheets for interest recalculation, day-count consistency, totals, duplicates, and blank fields, with line-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, legal, collections, and operations users can use this skill to check copied overdue-interest worksheet text before month-end closing, collection letters, or litigation preparation. It recalculates interest and day counts from supplied rows and reports missing data instead of filling defaults.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation and default output can direct users toward a paid install flow that runs unpinned external code and newly installed agent instructions.

Mitigation: Use the free checker through `node scripts/run.mjs` for local-only operation; do not run the SkillPay install command or paste the purchase prompt unless you independently trust the package and intentionally want the paid flow.

Risk: The free checker omits several validations and should not be treated as a complete legal or compliance review.

Mitigation: Review the omitted and out-of-scope checks, and independently verify legal rate limits, date anomalies, non-positive values, negative interest, debt validity, limitation periods, and contract-specific terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/overdue-interest-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON findings from local Node execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input exits without conclusions.]

## Skill Version(s):

1.0.14 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
