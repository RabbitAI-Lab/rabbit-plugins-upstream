## Description:

Screens Chinese-language contracts for missing breach, dispute, and jurisdiction terms and flags selected potentially risky clauses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and methodology)

## Use Case:

People reviewing Chinese-language contracts use this skill to quickly identify missing clause keywords and selected potentially risky terms before seeking legal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyword screening can miss legal issues or give a misleading impression of contract safety.

Mitigation: Use findings only as an initial checklist and obtain qualified legal review before signing.

Risk: Sensitive contract text may be exposed through a surrounding agent workflow.

Mitigation: Review that workflow's data handling before sharing confidential contracts; use local processing where appropriate.

## Reference(s):

- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/contract-clause-check)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text checklist or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports missing required keywords and risky terms; returns a pass/fail status.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
