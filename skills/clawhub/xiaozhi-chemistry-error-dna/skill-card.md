## Description:

初中到高中必修起点的化学错题根因分析与档案，做化学六维（符号/微观/宏观概念/读题/实验/计算）子类型定位与弱项报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Students, families, and education support agents use this skill to analyze Chinese-language K12 chemistry mistakes, identify six-dimensional chemistry error patterns, and produce scoped weak-point reports or profile updates with consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill analyzes chemistry mistakes and may write learning-profile data for K12 students.

Mitigation: Use only on platforms with the expected consent, profile, handoff, and reminder controls; keep profile writes scoped to chemistry fields.

Risk: The skill is written for Chinese-language K12 chemistry support and includes mainland-China-specific crisis referral defaults.

Mitigation: For use outside mainland China, localize curriculum terms, student-data rules, and crisis referral contacts before deployment.

Risk: A student may ask for help during an active exam or test.

Mitigation: Do not explain the current problem or provide hints during a stated exam; ask the student to return after the assessment for review.

Risk: Student distress or self-harm signals can exceed the skill's learning-support scope.

Mitigation: Stop the skill flow on crisis signals and follow the bundled crisis exception protocol, including referral to trusted adults or local emergency channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-error-dna)
- [chemistry-error-dimension-table.md](references/chemistry-error-dimension-table.md)
- [handover-protocol.schema.json](shared/handover-protocol.schema.json)
- [dna-profile.schema.json](shared/dna-profile.schema.json)
- [lab-safety.md](shared/lab-safety.md)
- [crisis-exception.md](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown text with JSON-compatible handover and chemistry profile records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write scoped chemistry profile data only with consent; reminders are queued through a separate handoff rather than promised directly.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
