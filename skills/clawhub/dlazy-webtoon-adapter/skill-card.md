## Description:

帮助用户将网络小说改编为条漫剧本，并通过 dLazy CLI 调用托管服务进行图像生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

面向创作者和编剧，用于把网络小说拆解为分集剧情并撰写条漫剧本。该技能还包含通过 dLazy CLI 生成图像的流程。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports unclear activation and undisclosed authentication, CLI, and image-generation actions that conflict with the stated conversation-only workflow. When the CLI is used, prompts and local media may be sent to dLazy hosted services.

Mitigation: Before installing or invoking the CLI, confirm with the publisher when it runs, how authentication works, and what data is sent; avoid submitting sensitive prompts or media until those details are clear.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Chinese-language Markdown and structured text; shell commands for optional image generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation requires a dLazy account and API key; prompts and supplied local media may be sent to dLazy hosted services.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
