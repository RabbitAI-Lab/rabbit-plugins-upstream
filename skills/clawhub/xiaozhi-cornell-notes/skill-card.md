## Description:

帮助中国大陆小学高段至高中学生将课堂笔记整理为康奈尔格式，并按学科和课题检索、复习。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆小学高段至高中学生，将拍照或文字形式的课堂笔记整理成线索问题、内容和一句话总结，并按需检索相关笔记。启用档案后可根据学生请求生成笔记使用情况报告。

### Deployment Geography for Use:

中国大陆；其他地区须先本地化求助渠道、学制和未成年人数据同意要求

## Known Risks and Mitigations:

Risk: 学生笔记可能在缺少独立档案同意的情况下被长期保存。

Mitigation: 每次持久保存前明确取得档案同意；未获同意时仅在当前会话整理。

Risk: 未成年人的笔记可能被未经授权的人读取或修改。

Mitigation: 对低龄学生核实监护人同意和使用者身份后，才允许读取或写入档案。

Risk: 跨技能共享或复习提醒可能超出学生预期。

Mitigation: 默认关闭共享和提醒，仅在分别取得同意后启用；共享时不传笔记全文。

## Reference(s):

- [康奈尔笔记 ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-cornell-notes)
- [康奈尔笔记格式与学科模板](references/cornell-format-guide.md)
- [学习 DNA 档案结构](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文康奈尔笔记、检索提示及按需生成的笔记使用报告]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [图片无法识别时可改用文字输入；没有跨会话记忆时仅整理当前会话的笔记。]

## Skill Version(s):

2.4.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
