## Description:

为内容运营、品牌调研和创作者提供小红书公开笔记搜索、博主作品查看、笔记详情与评论分析，帮助归纳趋势和选题线索。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

内容运营人员、品牌研究者和创作者可用它检索公开笔记、查看博主公开作品及互动数据、分析笔记详情和评论，以识别趋势、选题方向、竞品动态与受众反馈。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had medium confidence and could not fully inspect some components; searches send keywords and supplied links to a third-party service.

Mitigation: Review the partially inspected components before installation, check the service's data handling, and use only public, non-sensitive search terms and links.

## Reference(s):

- [小红书趋势洞察服务](https://www.guaikei.com)
- [ClawHub skill listing](https://clawhub.ai/why20261/skills/xiaohongshu-trends-insights)
- [Command routing guide](artifact/references/routing.md)
- [Output contract](artifact/references/contract.md)
- [Options reference](artifact/references/options.md)
- [Error handling guide](artifact/references/errors.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Text]

**Output Format:** [Structured JSON data with concise natural-language trend and content insights]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only access to public Xiaohongshu data; results depend on the service response.]

## Skill Version(s):

1.2.2 (source: SKILL.md frontmatter, package.json, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
