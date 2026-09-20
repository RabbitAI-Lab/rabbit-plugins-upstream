## Description:

基于用户输入的主题或产品关键词，查询小红书热门笔记数据并生成 10 个带匹配指数、参考爆款和推荐理由的标题候选。

This skill is ready for commercial/non-commercial use.

## Publisher:

[if530770](https://clawhub.ai/user/if530770)

### License/Terms of Use:

MIT-0

## Use Case:

小红书创作者、品牌运营、电商团队、MCN 和文案策划人员用它根据产品、话题或内容需求生成可筛选的小红书标题方案。该技能适合需要将近期热门笔记样本转化为标题灵感、A/B 测试候选或内容选题方向的对外创作场景。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key.

Mitigation: Provide REDFOX_API_KEY through the environment, confirm its scope and revocation path, and avoid exposing it in prompts, logs, source files, or generated output.

Risk: Keyword topics are sent to redfox.hk for trend data.

Mitigation: Use the skill only for topics that are acceptable to share with the RedFox service and avoid submitting confidential campaign details unless approved.

Risk: The release evidence flags broad network and file access plus unsafe command or file-writing instructions.

Mitigation: Review before installing, run the Python script through argument arrays, restrict outputs to a dedicated directory, and pin the requests dependency.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/if530770/skills/xhs-title-copywriter)
- [RedFoxHub](https://redfox.hk)
- [Xiaohongshu note link pattern](https://www.xiaohongshu.com/explore/{photoId})

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown title recommendations with match scores, reference links, rationale, and optional generated Markdown data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates 10 title candidates per request and requires REDFOX_API_KEY for RedFoxHub-backed trend data.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
