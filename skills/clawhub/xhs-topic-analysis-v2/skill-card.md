## Description:

当用户需要做小红书选题、小红书内容选题、小红书选题策划、爆款选题拆解、内容角度规划或选题素材整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营、品牌调研人员和创作者使用该 skill 基于关键词或选题方向搜索小红书内容样本，并整理话题模式、内容角度、受众反馈和可继续追问的方向。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the SocialDataX npm package and requires a user-provided SOCIALDATAX_API_KEY.

Mitigation: Install only in environments where running that package is acceptable, and provide the API key through the environment rather than embedding it in skill files or prompts.

Risk: Returned Xiaohongshu note URLs may include full tracking or access query parameters that are useful for the workflow but potentially sensitive outside it.

Mitigation: Keep full URLs intact for traceability when needed, but share them only with the intended audience and avoid unnecessary redistribution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/xhs-topic-analysis-v2)
- [SocialDataX AI and API key management](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with shell command examples and prose analysis guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js/npm and SOCIALDATAX_API_KEY; CLI results may include full Xiaohongshu URLs, content IDs, and pagination tokens.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
