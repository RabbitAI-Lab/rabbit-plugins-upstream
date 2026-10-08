## Description:

引导初高中学生分步解读历史材料、依据史料组织答案，并分析历史错题的原因。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向学习中国大陆初高中历史的学生，帮助他们阅读史料出处、提取信息、联系所学并形成有依据的材料题答案；也可在学生同意后分析历史错题。

### Deployment Geography for Use:

中国大陆课程适用；其他地区使用前需核对教学适用性与未成年人保护要求。

## Known Risks and Mitigations:

Risk: 未成年人的学习记录可能经跨技能共享、档案回写或提醒流转。

Mitigation: 部署前核查平台是否执行逐项同意及监护人同意要求；未经授权仅处理当前题目。

Risk: 中国大陆课程内容在其他教学环境中可能不适用。

Mitigation: 仅向需要简体中文、中国大陆课程辅导的用户提供，并在其他地区部署前核对课程和安全要求。

Risk: 错误或虚构的史料依据可能误导学生。

Mitigation: 核对史料出处和教材依据；无法确认时说明不确定性，不编造引文。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-history-source-analyzer)
- [历史材料解析题四步法](references/source-analysis-guide.md)
- [历史错因维度表](references/history-error-dimension-table.md)
- [高中历史必修概念对照](references/history-hs-concepts-required.md)
- [高中历史选择性必修概念对照](references/history-hs-concepts-elective.md)
- [高中历史必修材料题样板](references/history-hs-sources-required.md)
- [高中历史选择性必修材料题样板](references/history-hs-sources-elective.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown]

**Output Format:** [中文分步讲解与分点作答建议]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按学生尝试逐级提示；经同意后可提供错因分析和复习建议。]

## Skill Version(s):

2.11.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
