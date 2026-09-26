## Description:

Helps short-video operators analyze popular Douyin, TikTok, and Xiaohongshu videos, rewrite them around their own products, and use qhkit with Seedance 2.0 to generate product-marketing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, e-commerce operators, and marketing teams use this skill to convert reference short-video links into adapted product scripts and Seedance 2.0 video-generation jobs through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt users to share a qhkit API key in chat.

Mitigation: Configure the qhkit token through an environment variable or local secret store, and avoid pasting secrets into chat.

Risk: The skill includes broad automatic installation steps for npm, npx, pip, Node, and shell profile changes.

Mitigation: Review the skill before installing and explicitly approve package installs, downloads, and shell profile edits before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-seedance-2-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rewritten video scripts, model-selection guidance, estimate/status commands, and generated video delivery links returned by qhkit.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
