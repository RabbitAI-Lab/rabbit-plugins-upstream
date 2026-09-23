## Description:

学习DNA is a Chinese K12 learning-profile memory skill that helps agents create, inspect, correct, export, delete, and selectively use consent-controlled student learning profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, guardians, teachers, and education agents use this skill to maintain a long-term student learning profile with explicit consent, per-field sharing controls, and student-accessible review, correction, export, and deletion. It supports personalized tutoring context without turning ordinary Q&A into default long-term memory.

### Deployment Geography for Use:

China mainland Chinese K12 contexts by default; other regions require localized emergency contacts and minor-data consent review before deployment.

## Known Risks and Mitigations:

Risk: The skill handles sensitive long-term profiles for minors, including learning emotion, parent-visible summaries, teacher writeback, and cross-skill sharing.

Mitigation: Enable long-term profile features only where the host platform enforces per-student isolation, explicit consent checks, field-level access control, and user export, correction, deletion, and pause controls.

Risk: Crisis referral behavior and emergency contact guidance are designed around Chinese K12 contexts and China mainland channels.

Mitigation: Before deployment outside that context, localize crisis referral channels and review minor-data consent requirements for the target region.

Risk: The included schema validator checks profile structure but does not enforce runtime privacy, consent, or access-control behavior.

Mitigation: Treat validation as a data-shape check and implement consent, access control, retention, and audit enforcement in the host platform.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [学习DNA JSON Schema](schemas/README.md)
- [学习DNA模板](references/dna-template.md)
- [成长里程碑参考标准](references/growth-milestones.md)
- [跨学科概念关联标准模板库](references/cross-subject-connections.md)
- [危机识别与转介协议](references/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Configuration]

**Output Format:** [Chinese-language Markdown guidance and JSON-compatible learning-profile records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consent-gated profile reads and writes; schema validation is available for profile structure but is not runtime privacy enforcement.]

## Skill Version(s):

2.2.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
