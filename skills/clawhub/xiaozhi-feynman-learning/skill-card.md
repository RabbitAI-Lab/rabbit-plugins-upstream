## Description:

Guides Chinese-speaking students through explaining, illustrating, and applying a concept to identify their level of understanding and where they get stuck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use guided teach-back questions to check their understanding of a school subject and receive a formative mastery rating and next-step suggestions. Parents or teachers can support younger students during use.

### Deployment Geography for Use:

Global; designed for mainland China, with language, curriculum, and crisis-help channels localized before use elsewhere.

## Known Risks and Mitigations:

Risk: Student records, reminders, or parent sharing could expose a minor's learning information without appropriate consent.

Mitigation: Check student and guardian consent settings before enabling records, reminders, parent sharing, or cross-skill features; otherwise keep results in the current session.

Risk: Mainland China crisis-help channels may be inappropriate for students in other regions.

Mitigation: Localize crisis-help channels before deployment elsewhere, confirm the student's region when uncertain, and direct immediate danger to local emergency services.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Five-step assessment state machine](references/feynman-5jump-statemachine.md)
- [Dialogue patterns](references/feynman-dialogue-patterns.md)
- [Crisis response and localization](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text with a structured mastery assessment]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session-only by default; optional consent-gated record sharing and reminders.]

## Skill Version(s):

2.9.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
