## Description:

帮助中国初高中衔接阶段学生诊断数学、物理、化学、英语的基础缺口，并生成暑假到高一开学初期的周计划和转交建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, families, and education operators use this skill to plan the transition from the end of middle school to the first weeks of high school. It diagnoses bridge gaps across four subjects, sequences foundation review before light preview, and routes detailed subject work to companion skills.

### Deployment Geography for Use:

Mainland China Chinese-language K12 deployments

## Known Risks and Mitigations:

Risk: The skill is designed around mainland China K12 curriculum, consent assumptions, and crisis referral channels.

Mitigation: Deploy in Chinese-language mainland China K12 settings, or localize curriculum assumptions, consent rules, and crisis referral contacts before use elsewhere.

Risk: Profile data and reminder queues could expose student information if used without explicit consent.

Mitigation: Require explicit consent before reading profile fields or generating reminder handoffs, and keep both gates off by default.

Risk: The skill may encounter student crisis or safety signals during learning conversations.

Mitigation: Stop normal planning flow when crisis signals appear, explain AI limits, direct the student to a trusted adult, and provide region-appropriate emergency or youth support channels.

Risk: Plan persistence could be mistaken for this skill writing directly to a long-term profile.

Mitigation: Keep this skill read-only for profile data and route plan writes or execution tracking through the dedicated planning skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-bridge-planner)
- [Initial-to-high-school bridge checklists](artifact/references/bridge-checklists.md)
- [Platform conventions and localization guidance](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese-language Markdown or plain text planning guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces diagnostic questions, weekly bridge plans, consent-gated profile reads, reminder handoff instructions, and referrals to subject-specific skills.]

## Skill Version(s):

2.2.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
