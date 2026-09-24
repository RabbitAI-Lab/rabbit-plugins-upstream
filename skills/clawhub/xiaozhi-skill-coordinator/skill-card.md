## Description:

学习系统协调器用于判断一次学习问题应由哪个小智学习 SKILL 接手，并在用户同意时汇总授权摘要生成全景月报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Students, parents, teachers, and learning agents use this skill to route K12 learning requests to the right specialized skill, prevent duplicate coordination, and compile consent-gated monthly learning-system summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cross-skill coordination may combine student learning summaries beyond the user's expectations.

Mitigation: Use only the minimum authorized fields needed for the current task, honor consent flags, and support view, correction, deletion, pause, export, and sharing-control requests.

Risk: The skill is designed for a Chinese K12 learning context and may be unsuitable without localization.

Mitigation: Install it only for the intended context or localize grade bands, terminology, consent expectations, and referral channels before use.

Risk: Crisis or safety signals in student conversations could be mishandled if treated as ordinary learning coordination.

Mitigation: Stop routing and reporting flows when crisis signals appear, disclose AI limits, involve trusted adults, and use the relevant local emergency or support channels.

Risk: Reminder handoffs could create unwanted or excessive notifications.

Mitigation: Create reminder enqueue payloads only when reminder consent is enabled, and defer timing and send budgets to the reminder skill.

## Reference(s):

- [One-week linkage record](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception](shared/crisis-exception.md)
- [Vocabulary and consent conventions](shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance, structured text summaries, and JSON handover payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces route recommendations, consent-gated monthly report text, reminder enqueue handoffs, and schema-validated cross-skill handover records.]

## Skill Version(s):

2.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
