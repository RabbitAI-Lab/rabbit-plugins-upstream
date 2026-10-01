## Description:

Provides a Chinese-language LGD checklist and gate assessment for AI systems used in finance and licensed institutions, including investment advice, risk control, and anti-money-laundering workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); All rights reserved (documentation and theory)

## Use Case:

Developers and compliance reviewers at financial or licensed institutions can use this skill to self-check an AI system's identity, supporting evidence, and approval gates. Its results are a review aid, not a legal determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A checklist pass or fail may be mistaken for legal or regulatory approval.

Mitigation: Treat results as a self-check; confirm applicable requirements against official rules and qualified professional advice.

Risk: Keyword-based assessment of a system description may miss gaps or overstate evidence.

Mitigation: Review underlying documents and evidence with a human before relying on a gate result.

Risk: The documented remote installation commands fetch code from an external source.

Mitigation: Verify the remote source before running npx or git installation commands.

## Reference(s):

- [lgd-fin-guard on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-fin-guard)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Chinese-language checklist, text assessment, or JSON rubric and scores]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scores for three LGD principles, a pass/fail gate decision, and missing evidence items.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
