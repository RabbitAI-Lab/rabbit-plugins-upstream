## Description:

Helps assess financial AI systems against an LGD rubric for registration, supporting evidence, and approval gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Financial AI developers and compliance reviewers use this skill to self-assess advisory, risk-control, or anti-money-laundering systems and identify missing evidence before a human release decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated gate decisions could approve or block consequential financial activity without operator safeguards.

Mitigation: Use audit-only defaults and require explicit human approval, documented rollback procedures, and scoped permissions before any production action.

Risk: Broad requested agent tools may expose sensitive financial data or allow unintended changes.

Mitigation: Grant only the minimum read and execution permissions needed for the review; keep production writes and publishing outside the skill's authority.

Risk: Rubric or keyword-based scores may be mistaken for proof of licensing or compliance.

Mitigation: Have qualified reviewers verify the underlying records and applicable requirements rather than relying on the score or gate result alone.

## Reference(s):

- [lgd-fin-guard ClawHub listing](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-fin-guard)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text or JSON rubric scores, gate result, and missing-evidence list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Heuristic self-assessment or supplied-answer scoring; not a regulatory certification]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata; bundled documentation states 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
