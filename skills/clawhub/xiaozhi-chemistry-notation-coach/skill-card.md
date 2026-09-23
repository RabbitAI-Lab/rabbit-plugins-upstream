## Description:

A Chinese-language K12 chemistry notation coach for element symbols, valence, chemical formulas, equation writing, and equation balancing from junior high through required senior high foundations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, teachers, and learning agents use this skill to practice Chinese K12 chemistry notation, identify notation error types, and guide students through short exercises without replacing broader chemistry problem-solving or experiment coaching.

### Deployment Geography for Use:

China Mainland Chinese-language K12 contexts by default; localize language, curriculum assumptions, minor-consent rules, and crisis-support channels before use elsewhere.

## Known Risks and Mitigations:

Risk: Use outside the intended Chinese-language Mainland China K12 context may provide mismatched curriculum, consent, or crisis-support guidance.

Mitigation: Localize curriculum assumptions, language, minor-consent rules, and emergency or youth-support contacts before deployment in another region.

Risk: The skill can use learner profile memory, sharing, parent-view output, and reminders when platform consent is enabled.

Mitigation: Keep profile and reminder actions opt-in, honor view/correct/delete/pause/export controls, and review sharing and parent visibility settings before use.

Risk: Generated chemistry exercises or equations could be incorrect or pedagogically inappropriate if not checked.

Mitigation: Use the bundled notation rules and item self-check protocol before presenting exercises, keep practice sets short, and mark teacher-facing AI-generated items for human verification.

Risk: Student crisis or safety disclosures can appear during tutoring conversations.

Mitigation: Stop the tutoring flow, avoid diagnosis, encourage contact with a trusted adult, and provide localized emergency guidance only for the confirmed region.

## Reference(s):

- [化学用语规则手册](artifact/references/chemistry-notation-rules.md)
- [化学错因维度表](artifact/shared/chemistry-error-dimension-table.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)
- [危机例外](artifact/shared/crisis-exception.md)
- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-notation-coach)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational Markdown with short practice prompts, checks, explanations, handoff guidance, and consent-gated profile or reminder entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are scoped to chemistry notation practice, use short exercise sets, and include privacy, reminder, and crisis-response controls when relevant.]

## Skill Version(s):

2.2.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
