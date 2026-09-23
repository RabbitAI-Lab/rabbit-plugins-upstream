## Description:

A Chinese English-grammar coaching skill that uses Socratic prompts to help upper-primary and middle-school learners identify grammar errors and, with consent, track recurring weak points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 learners use this skill to practice English grammar through guided questioning, focused correction, short diagnostic summaries, and consent-gated grammar weakness tracking.

### Deployment Geography for Use:

China mainland by default; localize school-policy, minor-consent, and crisis-referral assumptions before deployment elsewhere.

## Known Risks and Mitigations:

Risk: The skill is designed for a Chinese K12 tutoring context and includes region-specific school-policy, minor-consent, and crisis-referral assumptions.

Mitigation: Use it in that intended context or localize the school-policy, consent, and crisis-resource content before deploying it elsewhere.

Risk: The skill may handle minors' learning records and grammar weakness profiles.

Mitigation: Require the host platform to enforce profile consent, guardian-consent rules, cross-skill sharing controls, and profile deletion/export controls before using persistent records.

Risk: Longitudinal progress summaries can be misleading if persistent memory or cross-session statistics are unavailable.

Mitigation: Degrade to current-session analysis only and avoid historical counts when the required platform memory or statistics capability is absent.

Risk: Crisis-support guidance depends on local emergency and youth-support channels.

Mitigation: Confirm the learner's region before giving crisis contacts and replace China mainland channels with local resources for other deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-grammar-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [English Error Dimension Table](references/english-error-dimension-table.md)
- [Grammar Patterns](references/grammar-patterns.md)
- [Platform Conventions](shared/platform-conventions.md)
- [Crisis Exception](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational Markdown with short analyses, guided questions, practice prompts, and optional profile-update handoff JSON examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are concise student-facing Chinese tutoring responses; persistent tracking is consent-gated and degrades to current-session analysis when memory or statistics are unavailable.]

## Skill Version(s):

2.2.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
