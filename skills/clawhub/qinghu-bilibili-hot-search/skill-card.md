## Description:

获取哔哩哔哩实时热搜榜，帮助用户了解当前热门话题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

用户和内容运营人员用此技能查询哔哩哔哩热搜榜，并获取热门话题的简要总结或表格。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 自动安装或升级 Node/npm 工具及 qhkit 可能引入未经审核的依赖。

Mitigation: 仅在信任该软件包时安装；优先预装经过审核且固定版本的 qhkit。

Risk: 配置 qhkit 时会保存服务令牌。

Mitigation: 优先使用权限受限或临时令牌，并在安装前审查其保存方式。

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-bilibili-hot-search)
- [青虎 qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [简要文字总结；较大结果可交付表格文件]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [付费查询前告知预计积分并征得同意；结果标明实际积分消耗。]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
