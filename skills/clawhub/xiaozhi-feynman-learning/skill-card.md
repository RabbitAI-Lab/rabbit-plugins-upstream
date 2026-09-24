## Description:

用“讲给小智听”的方式检验学生是否真正掌握一个知识点，并输出掌握度判定和卡住位置。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K-12 learners and their learning-support agents use this skill to test whether a student can explain, apply, transfer, and critically check a concept after studying it. It is suited to post-lesson self-checks, mistake-review follow-ups, and preparation for explaining a topic to another person.

### Deployment Geography for Use:

Mainland China by default; other regions require localization of language, curriculum assumptions, guardian-consent rules, and crisis resources before deployment.

## Known Risks and Mitigations:

Risk: The skill is designed for Chinese-language K-12 study support and includes mainland China crisis-resource assumptions.

Mitigation: Localize the language, curriculum assumptions, guardian-consent rules, and crisis resources before deploying outside mainland China.

Risk: The workflow can involve student learning records or reminder handoffs.

Mitigation: Use only the documented consent-gated profile and reminder controls; when consent is absent, keep results within the current conversation.

Risk: Student frustration signals can overlap with safety concerns.

Mitigation: Run the crisis-signal check before study-support fallback and route urgent safety content to trusted-adult and local emergency guidance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Feynman 4+1 Jump State Machine](references/feynman-5jump-statemachine.md)
- [Feynman Dialogue Patterns](references/feynman-dialogue-patterns.md)
- [Grade Bands](shared/grade-bands.md)
- [Crisis Exception](shared/crisis-exception.md)
- [AI Item Check Protocol](shared/ai-item-check.md)
- [Handover Protocol Schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Chinese-language conversational guidance and assessment summaries in Markdown-like text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe consent-gated handoff data for understanding records and reminder requests; otherwise defaults to current-session guidance.]

## Skill Version(s):

2.3.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
