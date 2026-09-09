## Description:

为曲阜师范大学学生提供校园生活、教务学业、奖助资助、信息系统、校区服务与 GPA 估算等事务的问答指引。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zexuan2008](https://clawhub.ai/user/zexuan2008)

### License/Terms of Use:

MIT-0

## Use Case:

External users, primarily 曲阜师范大学 students, use this skill to get practical campus guidance, official lookup paths, and GPA or eligibility estimates for academic and student-life decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes HTTP login portal links for school systems.

Mitigation: Prefer HTTPS official homepages or verified navigation paths before entering credentials, and avoid entering passwords on HTTP pages.

Risk: The skill includes predictable new-student credential guidance.

Mitigation: Treat default or initial-password formulas as sensitive and avoid broad reuse or sharing.

Risk: Campus dates, amounts, quotas, office contacts, and policy details may change by year or department.

Mitigation: Use the official lookup paths in the skill and verify dynamic details with the current school or department notice before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zexuan2008/skills/qfnulife)
- [学业与教务](artifact/references/academic.md)
- [校园服务与信息系统](artifact/references/campus-services.md)
- [奖助学金与资助](artifact/references/funding.md)
- [校园生活：校区、食宿、交通、作息](artifact/references/living.md)
- [官方网址与电话速查表](artifact/references/official-links.md)
- [曲阜师范大学主页](https://www.qfnu.edu.cn)
- [曲阜师范大学教务处](https://jwc.qfnu.edu.cn)
- [曲阜师范大学网络信息中心](https://net.qfnu.edu.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise instructions and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the bundled GPA script for local estimates; official school systems remain authoritative.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
