## Description:

Data-grade-checker is a zero-dependency decision-support CLI that classifies data under GB/T 43697-2024 and emits JSON IR for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance teams, and security reviewers use this skill to get an initial data classification and obligation summary for data scenarios. Results are decision support only and should be manually checked against current official rules before operational or legal use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Data classification output may be mistaken for compliance proof or legal advice.

Mitigation: Treat output as decision support and verify classifications against current official rules and qualified advice before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/data-grade-checker)
- [LGD theory ledger](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands]

**Output Format:** [JSON IR with result, warnings, return code, and AIGC metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI returns rc=0 for completed classification, rc=1 when warnings are present, and rc=2 for insufficient input.]

## Skill Version(s):

1.0.0 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
