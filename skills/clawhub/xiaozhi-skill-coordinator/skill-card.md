## Description:

Routes Chinese K-12 learning requests to the appropriate Xiaozhi skills and, with consent, compiles authorized summaries into system health checks or monthly panoramic reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents, and learning-support agents use this skill to route a learning request to the right Xiaozhi learning skill, avoid duplicate coordination, and generate consent-bounded summaries such as system health checks or monthly panoramic reports.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Cross-skill coordination can expose or update student profile data beyond the current task if platform controls are weak.

Mitigation: Install only where consent, authenticated sender identity, allowed sender-recipient routes, and strict field allowlists are enforced at receiving and persistence layers.

Risk: The shared handover schema is permissive for cross-skill student profile updates.

Mitigation: Review receiving-skill authorization and persistence behavior before deployment; do not treat schema validation alone as authorization.

Risk: Monthly reports and health checks can overstate historical performance when cross-session statistics are unavailable.

Mitigation: Limit reports to user-provided or authorized summary fields and clearly state when a report only covers the current session.

Risk: The skill is designed for Mainland China K-12 scenarios, including curriculum assumptions, consent defaults, and crisis referral paths.

Mitigation: Localize emergency contacts, curriculum mappings, and minor-data consent requirements before using it in other regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week linkage record](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception](shared/crisis-exception.md)
- [Shared vocabulary and consent fields](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance and structured JSON handover payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are consent-bounded summaries, routing decisions, and handover records rather than direct tutoring, root-cause analysis, or reminder delivery.]

## Skill Version(s):

2.1.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
