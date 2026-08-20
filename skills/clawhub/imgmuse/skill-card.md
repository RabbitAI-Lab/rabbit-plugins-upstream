## Description:

通用型图像Prompt生成器。输入主题描述，AI自主分析主体特征、决定艺术风格、推荐配色构图，输出结构化Prompt。

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn a theme or visual concept into structured image-generation prompts with coherent subject, style, composition, lighting, quality, and negative constraints. It is especially useful for illustration, poster, infographic, and educational visual design workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill declares file read, write, and edit tools, so user-directed saves or edits could change prompt files in the workspace.

Mitigation: Confirm target paths before writing, keep generated prompts in intended files, and review changes before using or sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/imgmuse)
- [Reference document](artifact/reference.md)
- [Prompt examples](artifact/examples.md)
- [Visual CS educator profile](artifact/知识可视化专家.md)
- [C++ contest poster prompt](artifact/assets/智国创玩C++月赛宣传图-prompt.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured Markdown and JSON prompt descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces image-generation prompts and content design guidance; it does not generate images by itself.]

## Skill Version(s):

2.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
