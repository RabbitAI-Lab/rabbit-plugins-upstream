## Description:

Chinese writing coach for upper-primary and middle-school learners that helps students develop their own ideas, check writing logic, draft independently, receive focused feedback, and improve revisions without having the agent write the essay for them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, guardians, and education platforms use this skill to coach Chinese composition practice through guided questioning, outline review, first-draft feedback, revision support, debate practice, and age-appropriate writing strategies. It is intended to strengthen the student's own writing process rather than produce finished essays on the student's behalf.

### Deployment Geography for Use:

Global, with localization required before use outside Chinese mainland K-12 contexts.

## Known Risks and Mitigations:

Risk: The skill can create or update persistent writing profiles for minors without clear guardian authorization.

Mitigation: Deploy only with guardian-consent checks for minors before profile creation or update, and reject profile writes when memory is paused or consent is unresolved.

Risk: The profile writeback schema is too permissive for unreviewed updates.

Mitigation: Validate writebacks against the documented Chinese writing fields and discard data outside the allowed profile scope.

Risk: Crisis support content includes China-specific emergency and support channels.

Mitigation: Localize crisis referral channels before deployment outside Chinese mainland contexts, and ask the user's region before giving country-specific numbers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-writing-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Writing 5-step state machine](artifact/references/writing-5step-statemachine.md)
- [Writing rubric](artifact/references/writing-rubric.md)
- [Debate script guide](artifact/references/debate-script-guide.md)
- [Hint ladder](artifact/shared/hint-ladder.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [DNA profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, text, configuration]

**Output Format:** [Markdown and structured guidance in Chinese, with optional profile writeback data when platform consent controls allow it.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce coaching questions, focused feedback, revision directions, debate prompts, crisis referrals, and consent-gated writing profile updates.]

## Skill Version(s):

2.1.10 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
