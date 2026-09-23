## Description:

作业设计师 helps Chinese-language K-12 teachers turn homework requests into tiered, time-boxed assignment cards with grading rubrics, feedback templates, and completion-summary handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K-12 teachers use this skill to design differentiated homework, grading criteria, and review-ready feedback. It is intended for teacher-reviewed drafts and class-level homework records, not automatic grading or direct student evaluation.

### Deployment Geography for Use:

China mainland Chinese-language K-12 settings by default; localize curriculum terms, emergency guidance, consent rules, and parent-facing text before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill is localized for Chinese-language K-12 homework workflows and may be unsuitable in other regions without adaptation.

Mitigation: Localize curriculum terms, emergency guidance, consent rules, and parent-facing text before use outside the intended setting.

Risk: AI-generated exercises may contain incorrect, unsolvable, or age-inappropriate items.

Mitigation: Require teacher review and human calculation checks before generated questions enter formal homework or resource banks.

Risk: Homework feedback and class records can expose student information or sensitive comparisons.

Mitigation: Use aliases or seat numbers, keep feedback aggregated where possible, avoid rankings and real names, and honor sharing and memory controls.

Risk: The skill can provide scoring criteria but does not perform authoritative grading.

Mitigation: Use generated rubrics and feedback templates as teacher-reviewed drafts; do not treat them as automatic grading results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer)
- [Assignment rubric and tiered task-card template](references/assignment-rubric.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI-generated item self-check protocol](shared/ai-item-check.md)
- [Platform localization and fallback conventions](shared/platform-conventions.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown task cards, grading rubrics, feedback templates, and structured homework-record field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include estimatedMinutes, estimatedTotalMinutes, completion-summary guidance, consent-aware feedback text, and teacher review labels for AI-generated questions.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
