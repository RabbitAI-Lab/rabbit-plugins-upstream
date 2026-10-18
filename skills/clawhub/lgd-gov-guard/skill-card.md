## Description:

Scores government and public-sector AI systems against the LGD registration, evidence, and gate rubric and returns a self-assessment verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and public-sector teams can use the rubric to review a system description or supplied evidence answers before making governance decisions. The resulting score is a self-assessment, not proof of legal authorization or regulatory approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Permissions and instructions conflict about network, file, execution, and logging behavior in sensitive workflows.

Mitigation: Use only as an offline, review-only rubric until the publisher clarifies permissions and documents log handling and redaction; do not grant unnecessary WebFetch or Write access.

Risk: The documentation claims automatic downstream release or blocking, which could be mistaken for an authorized government decision.

Mitigation: Require explicit human approval before any downstream release or blocking decision; do not treat the rubric verdict as regulatory approval.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-gov-guard)
- [Skill overview and licensing notes](artifact/README.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [JSON or plain-text CLI report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scores across three rubric areas, a pass/fail gate verdict, and missing evidence items.]

## Skill Version(s):

1.0.4 (source: ClawHub release; source SKILL.md lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
