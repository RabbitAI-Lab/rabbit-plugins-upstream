## Description:

输入作者确认的世界规则清单（编号、触发条件、代价、例外）及最多10个待审短场景，输出逐条对应原文、成立/冲突/无法判定表、判断依据与需作者批准的修订选项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

面向小说作者及编辑，依据作者已批准的设定核对章节片段中的触发条件、代价和例外，定位证据并整理需作者批准的修订选项。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted rules or scenes may include text the user does not want shared with their model provider.

Mitigation: Provide only writing the user is comfortable sharing with that provider.

Risk: The documented npx installation example does not pin an installer version or skill revision.

Mitigation: Review the installer version and skill revision before using the installation example.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xxjrq/skills/novel-world-rule-check-cn)
- [Worldbuilding reference cited for the business use case](https://github.com/danjdewhurst/story-skills/blob/main/skills/worldbuilding/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown table with quoted evidence, verdicts, reasoning, revision options, and missing information]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 20 rules and 10 short scenes; proposed revisions require author approval.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
