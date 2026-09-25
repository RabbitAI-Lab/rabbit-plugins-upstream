## Description:

通过循序追问帮助学生发现并纠正英语语法错误，并在获得同意后记录语法弱项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆的小学高年级及初中英语学习者，提供语法错误分析、引导式纠错和定语从句练习；小学学段需家长或老师陪同。

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Minor learners' grammar profiles or summaries could be retained or shared without appropriate consent.

Mitigation: Enforce platform consent flags before persistent profile writes, cross-skill sharing, reminders, or parent-visible summaries; otherwise keep analysis within the session.

Risk: Crisis referrals and consent practices may be inappropriate outside Mainland China.

Mitigation: Localize emergency resources and minor-consent rules before use in other regions; refer crisis signals to trusted adults and local emergency services.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-grammar-coach)
- [English error dimension table](references/english-error-dimension-table.md)
- [Grammar patterns](references/grammar-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text and structured progress summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional learner-profile updates require consent; historical progress reports require platform support.]

## Skill Version(s):

2.4.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
