## Description:

A local checker for treasury and bill worksheets that runs 14 built-in checks per object directory and reports one conclusion line per object with source file and line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance operators, treasury staff, accountants, and outsourced bookkeeping teams use this skill during month-end close, cash counts, bill maturity review, and bank reconciliation to check treasury and bill worksheets locally. It helps identify arithmetic and reconciliation issues, missing materials, not-run checks, and source-line evidence for follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the worksheet checks as an audit opinion, approval decision, or business authorization.

Mitigation: Use the output as a local checking aid and review findings against contracts, approvals, source documents, and formal audit or finance processes.

Risk: Not-run or withheld checks may be mistaken for passed checks.

Mitigation: Review the reported not-run and withheld checks before relying on a result, especially when materials cover only part of the 14-check scope.

Risk: Financial worksheets may contain sensitive business data.

Mitigation: Only run the skill on files the user intends it to read and keep the local input directory under appropriate access controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/treasury-bill-pack-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [Skill README](artifact/SKILL.md)
- [Sample input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Console text or JSON summary with per-object check results and source file and line citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided worksheet materials; no network use, persistence, credential access, or hidden mutation was reported by the security evidence.]

## Skill Version(s):

1.0.23 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
