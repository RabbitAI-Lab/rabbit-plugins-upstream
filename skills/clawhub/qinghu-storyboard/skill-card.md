## Description:

自动生成完整视频分镜方案，包含镜头设计、运镜建议、文案脚本及分镜图，提升视频制作效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to create video storyboard scripts, shot designs, camera movement suggestions, and storyboard image generation workflows through the Qinghu qhkit CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The qhkit CLI receives storyboard prompts and uploaded media.

Mitigation: Use the skill only when sharing those inputs with Qinghu/qhkit is acceptable.

Risk: The install and upgrade flow grants a third-party CLI local execution authority with weak version pinning.

Mitigation: Install a pinned, reviewed qhkit version in a constrained environment and review CLI-printed upgrade commands before running them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-storyboard)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated storyboard image URLs or media returned by qhkit.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
