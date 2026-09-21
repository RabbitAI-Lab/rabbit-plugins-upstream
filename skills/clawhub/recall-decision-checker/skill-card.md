## Description:

recall-decision-checker is a zero-dependency CLI that provides preliminary, rule-based medical-device recall level decision support with JSON IR output for the TH-MED-003 domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, compliance operators, and reviewers use this skill to run a local Chinese-language helper for preliminary medical-device recall level triage. Its output is decision support only and must be checked against current official rules and expert review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Regulatory output is simplified and may not reflect the complete current medical-device recall decision process.

Mitigation: Use the output only as preliminary triage and verify current official rules with qualified compliance or legal experts.

Risk: The security guidance notes that use_phase is ignored by the implementation.

Mitigation: Do not rely on use_phase-sensitive conclusions without separate review or implementation changes.

Risk: The artifact describes broader medical-device lifecycle coverage than the implemented local recall-level helper provides.

Mitigation: Limit use to recall-level helper scenarios and avoid treating it as full lifecycle compliance coverage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/recall-decision-checker)
- [LGD theory page](https://medxpert.cn/theory)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, guidance]

**Output Format:** [JSON IR and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI reports rc status codes and includes GB45438-2025 AIGC metadata in normal JSON output.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
