## Description:

A Simplified Chinese K12 writing coach that guides students through brainstorming, logic checks, drafting, feedback, and revision while preserving the student's own authorship.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary and middle school use this skill to develop Chinese composition ideas, test essay logic, receive focused feedback, and revise their own writing without AI ghostwriting. Primary-school use requires adult presence, and profile-memory features require consent.

### Deployment Geography for Use:

Mainland China by default; other regions require localization of crisis contacts, school-stage assumptions, and consent rules before student-facing deployment.

## Known Risks and Mitigations:

Risk: Profile memory, cross-skill sharing, parent sharing, or reminders could expose student writing patterns or learning data without proper consent.

Mitigation: Confirm profile, cross-skill sharing, parent-sharing, and reminder consent before using those features; default to current-session guidance when consent is absent.

Risk: Deploying outside mainland China could provide mismatched crisis contacts, school-stage assumptions, or minor-consent rules.

Mitigation: Localize crisis channels, grade-band assumptions, and consent requirements before non-mainland-China deployment.

Risk: Students could attempt to use the skill as an essay ghostwriter.

Mitigation: Use the five-step workflow, require student-authored ideas and drafts, and limit assistance to questions, direction, and feedback.

Risk: Student essays may include self-harm, bullying, family safety, or other crisis signals.

Mitigation: Stop ordinary writing coaching, follow the crisis referral protocol, direct the student to trusted adults and local emergency support, and avoid storing sensitive crisis details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-writing-coach)
- [Writing 5-Step State Machine](references/writing-5step-statemachine.md)
- [Writing Rubric](references/writing-rubric.md)
- [Debate Script Guide](references/debate-script-guide.md)
- [Platform Conventions](shared/platform-conventions.md)
- [Crisis Referral Protocol](shared/crisis-referral-protocol.md)
- [DNA Profile Schema](shared/dna-profile.schema.json)
- [Handover Protocol Schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, JSON]

**Output Format:** [Markdown or plain text coaching responses with optional JSON handoff payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consent-gated profile writebacks; no direct essay ghostwriting.]

## Skill Version(s):

2.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
