## Description:

文言文与古诗词专项：通过古人角色扮演、背诵练习、诗词鉴赏和文言答题规范，帮助初中学生理解并运用古诗文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and tutoring agents use this skill for Chinese classical literature support: role-play explanations of authors and works, memorization practice, writing quotation matching, classical Chinese basics, and exam-style poetry or prose answer guidance.

### Deployment Geography for Use:

China mainland by default; Global only after localizing curriculum assumptions, minor-data consent requirements, and crisis-referral channels.

## Known Risks and Mitigations:

Risk: The skill can record limited classical-literature progress and error-type notes when profile sharing is enabled.

Mitigation: Use the provided view, correct, delete, pause, export, and sharing controls; keep cross-skill sharing gated on explicit consent.

Risk: The artifact is designed for China mainland Chinese K12 contexts, including curriculum assumptions and crisis referral channels.

Mitigation: Localize curriculum scope, minor-data consent rules, and emergency or youth-support contacts before use in other regions.

Risk: Role-play about exile, war, death, or separation may surface real student distress.

Mitigation: Exit role-play immediately on crisis signals, avoid diagnosis or detailed probing, and route to trusted adults and local emergency support according to the bundled crisis protocol.

Risk: Generated memorization, translation, or poetry-analysis exercises may contain inaccurate source text or overhelp on assessed tasks.

Mitigation: Run the artifact's item self-check before generating exercises, tell users when source wording is uncertain, and use the hint ladder so full examples precede student attempts without directly giving original-task answers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/chinese-classical-revival)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [重点古人历史背景与情感档案库](references/classical-author-profiles.md)
- [语文错因维度表](shared/chinese-error-dimension-table.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机例外](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown or plain text tutoring responses with optional structured handoff JSON when profile sharing is enabled]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate consent-gated learning progress notes, reminder handoff requests, and classical-literature practice prompts.]

## Skill Version(s):

1000000.10.0 (source: ClawHub release metadata; artifact frontmatter lists 2.1.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
