## Description:

A Chinese composition coaching agent that helps students develop their own essay ideas, check outlines, revise drafts, and practice argumentation without writing the essay for them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, guardians, and education assistants use this skill for Chinese essay brainstorming, outline checks, first-reader feedback, targeted revision coaching, and debate-based argument practice. It is designed to keep student authorship central while offering structured questions, critique, and consent-gated writing-style memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student drafts, feedback state, and optional writing-style profiles may contain sensitive information, especially when used with minors.

Mitigation: Use only where students and guardians understand stored data; enforce host controls for memory, cross-skill sharing, parent sharing, reminders, and deletion.

Risk: Composition topics may surface crisis signals that exceed writing-coach support.

Mitigation: Apply the bundled crisis referral protocol and locale-specific resources before continuing any routine coaching flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-writing-coach)
- [Writing 5-step state machine](references/writing-5step-statemachine.md)
- [Writing rubric](references/writing-rubric.md)
- [Debate script guide](references/debate-script-guide.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown or plain text coaching responses with optional structured profile and handover records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consent-gated memory and profile updates; no executable install behavior.]

## Skill Version(s):

2.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
