## Description:

帮助抖音电商运营、直播团队和短视频创作者通过 qhkit/LinkPix 生成竖屏带货短视频、直播间切片、口播带货、剧情反转、好物测评和热点跟拍内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce operators, and agent users use this skill to plan and run qhkit/LinkPix workflows for Douyin-focused product videos. It helps choose available video models, prepare prompts and media, estimate credits, submit generation tasks after confirmation, poll status, and deliver completed video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask the agent to install or upgrade npm and Node-based tooling, including global installs and PATH changes.

Mitigation: Require explicit approval for global installs or PATH changes, prefer pinned qhkit package versions, and verify downloaded tooling before execution.

Risk: The workflow can upload selected media and prompts to the qhkit/LinkPix service using a qhkit API key.

Mitigation: Use only approved media, avoid secrets or sensitive personal data in prompts and uploads, and scope or revoke qhkit API keys when appropriate.

Risk: The skill references upgrade commands that may come from tool output.

Mitigation: Do not automatically run upgrade commands copied from tool output; review the command and package version before upgrading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-douyin-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit task IDs, credit estimates, status summaries, and generated video URLs when used with a configured qhkit API key.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
