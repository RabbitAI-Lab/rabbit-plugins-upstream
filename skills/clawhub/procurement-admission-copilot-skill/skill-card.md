## Description:

Shadow-mode copilot for B2B procurement admission that checks supplier material-package completeness and consistency, tracks approval-case stalls and gaps, and leaves admission decisions to human reviewers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and supplier-management teams use this skill to review supplier admission material packages and approval case queues for completeness, consistency, stalls, and gaps. It produces review artifacts for human reviewers and does not draft contract terms or make admission decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may consolidate supplier legal identifiers, financial summaries, compliance details, and reviewer status.

Mitigation: Process only authorized materials, redact unnecessary sensitive fields, and store outputs under procurement confidentiality controls.

Risk: Review artifacts could be mistaken for an admission decision if used without human oversight.

Mitigation: Keep P0/P1 disposition and approval or rejection decisions with the procurement committee or buyer.

## Reference(s):

- [Qualification checklist](references/qualification-checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [JSON readiness checks and Markdown material packages, readiness reports, and case dashboards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review-only outputs; no supplier document edits, contract terms, or admission decisions.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
